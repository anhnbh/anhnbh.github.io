#!/usr/bin/env python3
import json
import random
import os

def load_all_questions():
    """Load all questions from data files"""
    all_questions = []
    
    for day in range(1, 21):
        json_file = f'data/day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                all_questions.extend(questions)
    
    return all_questions

def create_exam_mode():
    """Create exam simulation mode following AWS DOP-C02 format"""
    
    all_questions = load_all_questions()
    
    if not all_questions:
        print("❌ No questions found!")
        return
    
    # AWS DevOps Professional exam format:
    # - 75 questions
    # - 180 minutes (3 hours)
    # - Multiple choice and multiple response
    # - Passing score: 750/1000 (75%)
    
    exam_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS DevOps Professional - Practice Exam</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; }
        .container { max-width: 1000px; margin: 0 auto; padding: 20px; }
        .exam-header { background: #232f3e; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; position: sticky; top: 0; z-index: 100; }
        .timer { font-size: 24px; font-weight: bold; color: #ff9900; }
        .progress-info { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }
        .progress-bar { background: #ddd; height: 8px; border-radius: 4px; flex: 1; margin: 0 20px; }
        .progress { background: #ff9900; height: 100%; border-radius: 4px; transition: width 0.3s; }
        .exam-warning { background: #fff3cd; border: 1px solid #ffeaa7; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        .question-card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .question-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .question-number { background: #232f3e; color: white; padding: 8px 16px; border-radius: 20px; font-weight: bold; }
        .question-type { background: #e3f2fd; color: #1976d2; padding: 6px 12px; border-radius: 15px; font-size: 14px; }
        .question-text { font-size: 18px; line-height: 1.6; margin-bottom: 25px; }
        .options { margin: 20px 0; }
        .option { background: #f8f9fa; border: 2px solid #e9ecef; padding: 18px; margin: 12px 0; border-radius: 8px; cursor: pointer; transition: all 0.3s; position: relative; }
        .option:hover { border-color: #ff9900; background: #fff8e1; }
        .option.selected { border-color: #ff9900; background: #fff3cd; }
        .option.flagged { border-color: #dc3545; background: #f8d7da; }
        .option-checkbox { position: absolute; right: 18px; top: 50%; transform: translateY(-50%); width: 18px; height: 18px; }
        .controls { display: flex; gap: 15px; justify-content: space-between; margin-top: 30px; flex-wrap: wrap; }
        .btn { padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; transition: all 0.3s; }
        .btn-primary { background: #ff9900; color: white; }
        .btn-primary:hover { background: #e68900; }
        .btn-secondary { background: #6c757d; color: white; }
        .btn-secondary:hover { background: #545b62; }
        .btn-danger { background: #dc3545; color: white; }
        .btn-danger:hover { background: #c82333; }
        .btn-warning { background: #ffc107; color: #212529; }
        .btn-warning:hover { background: #e0a800; }
        .btn:disabled { background: #ccc; cursor: not-allowed; }
        .navigation { display: flex; gap: 10px; }
        .question-nav { display: grid; grid-template-columns: repeat(auto-fill, minmax(50px, 1fr)); gap: 8px; margin: 20px 0; }
        .nav-btn { padding: 8px; border: 2px solid #ddd; background: white; border-radius: 6px; cursor: pointer; text-align: center; font-size: 14px; }
        .nav-btn.answered { background: #d4edda; border-color: #28a745; }
        .nav-btn.flagged { background: #f8d7da; border-color: #dc3545; }
        .nav-btn.current { background: #fff3cd; border-color: #ffc107; font-weight: bold; }
        .exam-summary { background: white; padding: 30px; border-radius: 10px; margin-top: 20px; }
        .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }
        .summary-card { background: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; }
        .summary-number { font-size: 28px; font-weight: bold; color: #232f3e; }
        .hidden { display: none; }
        .time-warning { animation: pulse 1s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
        .final-warning { background: #f8d7da; border: 2px solid #dc3545; padding: 20px; border-radius: 10px; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="exam-header">
            <div class="progress-info">
                <div>
                    <h2>🎓 AWS Certified DevOps Engineer Professional</h2>
                    <p>Practice Exam - DOP-C02</p>
                </div>
                <div class="timer" id="examTimer">180:00</div>
            </div>
            <div class="progress-info">
                <span>Question <span id="currentQ">1</span> of <span id="totalQ">75</span></span>
                <div class="progress-bar">
                    <div class="progress" id="progressBar"></div>
                </div>
                <span>Answered: <span id="answeredCount">0</span> | Flagged: <span id="flaggedCount">0</span></span>
            </div>
        </div>

        <div class="exam-warning">
            <strong>⚠️ Exam Instructions:</strong>
            <ul style="margin-left: 20px; margin-top: 10px;">
                <li>75 questions, 180 minutes (3 hours)</li>
                <li>Passing score: 750/1000 points (75%)</li>
                <li>Multiple choice and multiple response questions</li>
                <li>You can flag questions for review</li>
                <li>Submit exam when ready or time expires</li>
            </ul>
        </div>

        <div id="examMode" class="question-card">
            <div class="question-header">
                <div class="question-number" id="questionNumber">Question 1</div>
                <div class="question-type" id="questionType">Single Response</div>
            </div>
            
            <div class="question-text" id="questionText">
                Loading question...
            </div>
            
            <div class="options" id="optionsContainer">
                <!-- Options will be loaded here -->
            </div>
            
            <div class="controls">
                <div class="navigation">
                    <button class="btn btn-secondary" onclick="previousQuestion()" id="prevBtn">⬅️ Previous</button>
                    <button class="btn btn-warning" onclick="flagQuestion()" id="flagBtn">🚩 Flag</button>
                    <button class="btn btn-secondary" onclick="nextQuestion()" id="nextBtn">Next ➡️</button>
                </div>
                <div>
                    <button class="btn btn-danger" onclick="showSubmitConfirm()">📤 Submit Exam</button>
                </div>
            </div>
        </div>

        <div class="question-nav" id="questionNav">
            <!-- Navigation buttons will be generated here -->
        </div>

        <div id="submitConfirm" class="exam-summary hidden">
            <div class="final-warning">
                <h3>⚠️ Submit Exam Confirmation</h3>
                <p>Are you sure you want to submit your exam? This action cannot be undone.</p>
            </div>
            
            <div class="summary-grid">
                <div class="summary-card">
                    <div class="summary-number" id="finalAnswered">0</div>
                    <div>Questions Answered</div>
                </div>
                <div class="summary-card">
                    <div class="summary-number" id="finalUnanswered">75</div>
                    <div>Questions Unanswered</div>
                </div>
                <div class="summary-card">
                    <div class="summary-number" id="finalFlagged">0</div>
                    <div>Questions Flagged</div>
                </div>
                <div class="summary-card">
                    <div class="summary-number" id="finalTime">180:00</div>
                    <div>Time Remaining</div>
                </div>
            </div>
            
            <div class="controls">
                <button class="btn btn-secondary" onclick="hideSubmitConfirm()">↩️ Continue Exam</button>
                <button class="btn btn-danger" onclick="submitExam()">✅ Submit Final Answer</button>
            </div>
        </div>

        <div id="examResults" class="exam-summary hidden">
            <h2>📊 Exam Results</h2>
            <div id="resultsContent"></div>
            <div class="controls">
                <button class="btn btn-primary" onclick="restartExam()">🔄 Retake Exam</button>
                <button class="btn btn-secondary" onclick="reviewAnswers()">📝 Review Answers</button>
                <button class="btn btn-warning" onclick="exportExamResults()">💾 Export Results</button>
            </div>
        </div>
    </div>

    <script>
        // Exam questions (75 random questions from the pool)
        const allQuestions = ''' + json.dumps(all_questions, ensure_ascii=False, indent=8) + ''';
        
        let examQuestions = [];
        let currentQuestionIndex = 0;
        let userAnswers = [];
        let flaggedQuestions = new Set();
        let examStartTime = Date.now();
        let examDuration = 180 * 60 * 1000; // 180 minutes in milliseconds
        let examTimer;
        let isExamSubmitted = false;

        function initializeExam() {
            // Select 75 random questions (AWS exam format)
            const shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
            
            // Ensure good mix: ~30% multiple choice (AWS typical distribution)
            const multipleChoice = shuffled.filter(q => q.type === 'multiple').slice(0, 22);
            const singleChoice = shuffled.filter(q => q.type === 'single').slice(0, 53);
            
            examQuestions = [...multipleChoice, ...singleChoice].sort(() => 0.5 - Math.random());
            
            // Initialize arrays
            userAnswers = new Array(75).fill(null);
            flaggedQuestions.clear();
            
            // Setup UI
            document.getElementById('totalQ').textContent = examQuestions.length;
            generateQuestionNavigation();
            loadQuestion();
            startExamTimer();
            updateStats();
        }

        function generateQuestionNavigation() {
            const nav = document.getElementById('questionNav');
            nav.innerHTML = '';
            
            for (let i = 0; i < examQuestions.length; i++) {
                const btn = document.createElement('div');
                btn.className = 'nav-btn';
                btn.textContent = i + 1;
                btn.onclick = () => goToQuestion(i);
                nav.appendChild(btn);
            }
        }

        function loadQuestion() {
            if (currentQuestionIndex >= examQuestions.length) return;

            const question = examQuestions[currentQuestionIndex];
            
            // Update question display
            document.getElementById('questionNumber').textContent = `Question ${currentQuestionIndex + 1}`;
            document.getElementById('questionText').innerHTML = question.text;
            
            // Set question type
            const typeElement = document.getElementById('questionType');
            if (question.type === 'multiple') {
                typeElement.textContent = `Multiple Response (Select ${question.correct.length})`;
                typeElement.style.background = '#fff3cd';
                typeElement.style.color = '#856404';
            } else {
                typeElement.textContent = 'Single Response';
                typeElement.style.background = '#e3f2fd';
                typeElement.style.color = '#1976d2';
            }
            
            // Load options
            const container = document.getElementById('optionsContainer');
            container.innerHTML = '';
            
            question.options.forEach((option, index) => {
                const optionDiv = document.createElement('div');
                optionDiv.className = 'option';
                optionDiv.innerHTML = `
                    <strong>${String.fromCharCode(65 + index)}.</strong> ${option}
                    ${question.type === 'multiple' ? '<input type="checkbox" class="option-checkbox">' : ''}
                `;
                
                // Restore previous selection
                const previousAnswer = userAnswers[currentQuestionIndex];
                if (previousAnswer && previousAnswer.includes(index)) {
                    optionDiv.classList.add('selected');
                    if (question.type === 'multiple') {
                        optionDiv.querySelector('.option-checkbox').checked = true;
                    }
                }
                
                if (question.type === 'multiple') {
                    optionDiv.onclick = () => toggleMultipleOption(index);
                } else {
                    optionDiv.onclick = () => selectSingleOption(index);
                }
                
                optionDiv.dataset.index = index;
                container.appendChild(optionDiv);
            });

            // Update navigation
            updateQuestionNavigation();
            updateNavigationButtons();
            updateStats();
        }

        function selectSingleOption(index) {
            document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
            document.querySelector(`[data-index="${index}"]`).classList.add('selected');
            userAnswers[currentQuestionIndex] = [index];
            updateStats();
        }

        function toggleMultipleOption(index) {
            const option = document.querySelector(`[data-index="${index}"]`);
            const checkbox = option.querySelector('.option-checkbox');
            
            if (option.classList.contains('selected')) {
                option.classList.remove('selected');
                checkbox.checked = false;
            } else {
                option.classList.add('selected');
                checkbox.checked = true;
            }
            
            // Update answer array
            const selected = [];
            document.querySelectorAll('.option.selected').forEach(opt => {
                selected.push(parseInt(opt.dataset.index));
            });
            
            userAnswers[currentQuestionIndex] = selected.length > 0 ? selected : null;
            updateStats();
        }

        function nextQuestion() {
            if (currentQuestionIndex < examQuestions.length - 1) {
                currentQuestionIndex++;
                loadQuestion();
            }
        }

        function previousQuestion() {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                loadQuestion();
            }
        }

        function goToQuestion(index) {
            currentQuestionIndex = index;
            loadQuestion();
        }

        function flagQuestion() {
            if (flaggedQuestions.has(currentQuestionIndex)) {
                flaggedQuestions.delete(currentQuestionIndex);
                document.getElementById('flagBtn').textContent = '🚩 Flag';
            } else {
                flaggedQuestions.add(currentQuestionIndex);
                document.getElementById('flagBtn').textContent = '🏳️ Unflag';
            }
            updateQuestionNavigation();
            updateStats();
        }

        function updateQuestionNavigation() {
            const navBtns = document.querySelectorAll('.nav-btn');
            navBtns.forEach((btn, index) => {
                btn.className = 'nav-btn';
                
                if (index === currentQuestionIndex) {
                    btn.classList.add('current');
                }
                if (userAnswers[index]) {
                    btn.classList.add('answered');
                }
                if (flaggedQuestions.has(index)) {
                    btn.classList.add('flagged');
                }
            });
        }

        function updateNavigationButtons() {
            document.getElementById('prevBtn').disabled = currentQuestionIndex === 0;
            document.getElementById('nextBtn').disabled = currentQuestionIndex === examQuestions.length - 1;
            
            const flagBtn = document.getElementById('flagBtn');
            flagBtn.textContent = flaggedQuestions.has(currentQuestionIndex) ? '🏳️ Unflag' : '🚩 Flag';
        }

        function updateStats() {
            const answered = userAnswers.filter(a => a !== null).length;
            const progress = (answered / examQuestions.length) * 100;
            
            document.getElementById('currentQ').textContent = currentQuestionIndex + 1;
            document.getElementById('answeredCount').textContent = answered;
            document.getElementById('flaggedCount').textContent = flaggedQuestions.size;
            document.getElementById('progressBar').style.width = progress + '%';
        }

        function startExamTimer() {
            examTimer = setInterval(() => {
                const elapsed = Date.now() - examStartTime;
                const remaining = Math.max(0, examDuration - elapsed);
                
                const minutes = Math.floor(remaining / 60000);
                const seconds = Math.floor((remaining % 60000) / 1000);
                
                const timerElement = document.getElementById('examTimer');
                timerElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
                
                // Warning when < 30 minutes
                if (remaining < 30 * 60 * 1000) {
                    timerElement.classList.add('time-warning');
                }
                
                // Auto-submit when time expires
                if (remaining === 0) {
                    clearInterval(examTimer);
                    alert('⏰ Time expired! Exam will be submitted automatically.');
                    submitExam();
                }
            }, 1000);
        }

        function showSubmitConfirm() {
            const answered = userAnswers.filter(a => a !== null).length;
            const unanswered = examQuestions.length - answered;
            
            document.getElementById('finalAnswered').textContent = answered;
            document.getElementById('finalUnanswered').textContent = unanswered;
            document.getElementById('finalFlagged').textContent = flaggedQuestions.size;
            document.getElementById('finalTime').textContent = document.getElementById('examTimer').textContent;
            
            document.getElementById('examMode').classList.add('hidden');
            document.getElementById('submitConfirm').classList.remove('hidden');
        }

        function hideSubmitConfirm() {
            document.getElementById('examMode').classList.remove('hidden');
            document.getElementById('submitConfirm').classList.add('hidden');
        }

        function submitExam() {
            if (isExamSubmitted) return;
            
            isExamSubmitted = true;
            clearInterval(examTimer);
            
            // Calculate results
            let correctAnswers = 0;
            let partialCredit = 0;
            
            examQuestions.forEach((question, index) => {
                const userAnswer = userAnswers[index];
                if (!userAnswer) return;
                
                const correctAnswer = question.correct.sort();
                const userSorted = userAnswer.sort();
                
                if (question.type === 'single') {
                    if (userSorted.length === 1 && userSorted[0] === correctAnswer[0]) {
                        correctAnswers++;
                    }
                } else {
                    // Multiple choice scoring
                    if (JSON.stringify(userSorted) === JSON.stringify(correctAnswer)) {
                        correctAnswers++;
                    } else {
                        // Partial credit for multiple choice
                        const correctSelected = userAnswer.filter(ans => correctAnswer.includes(ans));
                        const incorrectSelected = userAnswer.filter(ans => !correctAnswer.includes(ans));
                        
                        if (correctSelected.length > 0 && incorrectSelected.length === 0) {
                            partialCredit += 0.5;
                        }
                    }
                }
            });
            
            const totalScore = correctAnswers + partialCredit;
            const percentage = (totalScore / examQuestions.length) * 100;
            const scaledScore = Math.round((totalScore / examQuestions.length) * 1000);
            const passed = scaledScore >= 750;
            
            // Show results
            document.getElementById('submitConfirm').classList.add('hidden');
            document.getElementById('examResults').classList.remove('hidden');
            
            const resultsHTML = `
                <div class="summary-grid">
                    <div class="summary-card">
                        <div class="summary-number" style="color: ${passed ? '#28a745' : '#dc3545'}">${scaledScore}</div>
                        <div>Score (out of 1000)</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-number">${percentage.toFixed(1)}%</div>
                        <div>Percentage</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-number">${correctAnswers}</div>
                        <div>Correct Answers</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-number">${partialCredit.toFixed(1)}</div>
                        <div>Partial Credit</div>
                    </div>
                </div>
                
                <div style="text-align: center; margin: 30px 0; padding: 20px; border-radius: 10px; background: ${passed ? '#d4edda' : '#f8d7da'};">
                    <h2 style="color: ${passed ? '#155724' : '#721c24'};">
                        ${passed ? '🎉 CONGRATULATIONS! YOU PASSED!' : '❌ NOT PASSED - KEEP STUDYING!'}
                    </h2>
                    <p style="margin-top: 10px;">
                        ${passed ? 'You are ready for the real AWS DevOps Professional exam!' : 'Passing score is 750. Review your weak areas and try again.'}
                    </p>
                </div>
            `;
            
            document.getElementById('resultsContent').innerHTML = resultsHTML;
        }

        function restartExam() {
            isExamSubmitted = false;
            examStartTime = Date.now();
            currentQuestionIndex = 0;
            userAnswers = new Array(75).fill(null);
            flaggedQuestions.clear();
            
            document.getElementById('examResults').classList.add('hidden');
            document.getElementById('examMode').classList.remove('hidden');
            
            initializeExam();
        }

        function exportExamResults() {
            const results = {
                examDate: new Date().toISOString(),
                examType: "AWS DevOps Professional Practice Exam",
                totalQuestions: examQuestions.length,
                answeredQuestions: userAnswers.filter(a => a !== null).length,
                correctAnswers: 0, // Calculate this
                score: document.querySelector('#resultsContent .summary-number').textContent,
                timeSpent: document.getElementById('examTimer').textContent,
                flaggedQuestions: Array.from(flaggedQuestions),
                detailedAnswers: examQuestions.map((q, i) => ({
                    questionId: q.id,
                    questionType: q.type,
                    userAnswer: userAnswers[i],
                    correctAnswer: q.correct,
                    flagged: flaggedQuestions.has(i)
                }))
            };

            const blob = new Blob([JSON.stringify(results, null, 2)], {type: 'application/json'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `aws-devops-exam-results-${new Date().toISOString().split('T')[0]}.json`;
            a.click();
        }

        // Initialize exam when page loads
        window.onload = initializeExam;
        
        // Prevent accidental page refresh during exam
        window.addEventListener('beforeunload', function(e) {
            if (!isExamSubmitted) {
                e.preventDefault();
                e.returnValue = 'Are you sure you want to leave? Your exam progress will be lost.';
            }
        });
    </script>
</body>
</html>'''
    
    # Save the exam app
    with open('apps/exam_mode.html', 'w', encoding='utf-8') as f:
        f.write(exam_content)
    
    print(f"✅ Created exam_mode.html")
    print(f"📊 Exam format: 75 questions, 180 minutes")
    print(f"🎯 Passing score: 750/1000 (75%)")
    print(f"📚 Question pool: {len(all_questions)} total questions")

if __name__ == "__main__":
    create_exam_mode()
