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

def create_review_app():
    """Create review app with random questions and spaced repetition"""
    
    # Load all questions
    all_questions = load_all_questions()
    
    if not all_questions:
        print("❌ No questions found!")
        return
    
    print(f"📚 Loaded {len(all_questions)} total questions")
    
    # Create review app template
    app_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS DevOps Review App - 5 Ngày Ôn Tập</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        .header { background: #d32f2f; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .review-mode { background: #fff3e0; border: 2px solid #ff9800; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        .progress-bar { background: #ddd; height: 10px; border-radius: 5px; margin: 10px 0; }
        .progress { background: #d32f2f; height: 100%; border-radius: 5px; transition: width 0.3s; }
        .question-card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .question-text { font-size: 18px; line-height: 1.6; margin-bottom: 20px; }
        .question-type { background: #ffebee; color: #c62828; padding: 8px 16px; border-radius: 20px; font-size: 14px; font-weight: bold; margin-bottom: 15px; display: inline-block; }
        .difficulty { background: #e8f5e8; color: #2e7d32; padding: 4px 12px; border-radius: 15px; font-size: 12px; margin-left: 10px; }
        .options { margin: 20px 0; }
        .option { background: #f8f9fa; border: 2px solid #e9ecef; padding: 15px; margin: 10px 0; border-radius: 8px; cursor: pointer; transition: all 0.3s; position: relative; }
        .option:hover { border-color: #d32f2f; }
        .option.selected { border-color: #d32f2f; background: #ffebee; }
        .option.correct { border-color: #28a745; background: #d4edda; }
        .option.incorrect { border-color: #dc3545; background: #f8d7da; }
        .option.partial { border-color: #ffc107; background: #fff3cd; }
        .option-checkbox { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); width: 20px; height: 20px; }
        .controls { display: flex; gap: 15px; justify-content: center; margin-top: 20px; flex-wrap: wrap; }
        .btn { padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; transition: all 0.3s; }
        .btn-primary { background: #d32f2f; color: white; }
        .btn-primary:hover { background: #b71c1c; }
        .btn-secondary { background: #6c757d; color: white; }
        .btn-secondary:hover { background: #545b62; }
        .btn-warning { background: #ff9800; color: white; }
        .btn-warning:hover { background: #f57c00; }
        .btn:disabled { background: #ccc; cursor: not-allowed; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin-bottom: 20px; }
        .stat-card { background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .stat-number { font-size: 20px; font-weight: bold; color: #d32f2f; }
        .review-section { background: white; padding: 20px; border-radius: 10px; margin-top: 20px; }
        .wrong-answer { background: #fff3cd; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #ffc107; }
        .hidden { display: none; }
        .explanation { margin-top: 20px; padding: 15px; border-radius: 8px; }
        .explanation.correct { background: #d4edda; border-left: 4px solid #28a745; }
        .explanation.incorrect { background: #f8d7da; border-left: 4px solid #dc3545; }
        .explanation.partial { background: #fff3cd; border-left: 4px solid #ffc107; }
        .mode-selector { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
        .mode-btn { padding: 10px 20px; border: 2px solid #d32f2f; background: white; color: #d32f2f; border-radius: 6px; cursor: pointer; }
        .mode-btn.active { background: #d32f2f; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 AWS DevOps Review App - 5 Ngày Ôn Tập Cuối</h1>
            <div class="progress-bar">
                <div class="progress" id="progressBar"></div>
            </div>
            <p>Review Mode - Câu <span id="currentQuestion">1</span>/<span id="totalQuestions">50</span></p>
        </div>

        <div class="review-mode">
            <strong>🎯 Chế độ ôn tập:</strong> Random questions từ tất cả 360 câu. 
            Focus vào câu khó và multiple choice để chuẩn bị thi!
        </div>

        <div class="mode-selector">
            <div class="mode-btn active" onclick="setMode('mixed')">🔀 Mixed (50 câu)</div>
            <div class="mode-btn" onclick="setMode('multiple')">📝 Multiple Choice (30 câu)</div>
            <div class="mode-btn" onclick="setMode('hard')">🔥 Câu Khó (25 câu)</div>
            <div class="mode-btn" onclick="setMode('random')">🎲 Random (100 câu)</div>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="correctCount">0</div>
                <div>Đúng</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="wrongCount">0</div>
                <div>Sai</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="accuracy">0%</div>
                <div>Độ chính xác</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="timeSpent">0:00</div>
                <div>Thời gian</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="streak">0</div>
                <div>Streak</div>
            </div>
        </div>

        <div id="studyMode" class="question-card">
            <div class="question-type" id="questionType">Mixed Review</div>
            <div class="question-text" id="questionText">
                Đang tải câu hỏi...
            </div>
            <div class="options" id="optionsContainer">
                <!-- Options will be loaded here -->
            </div>
            <div class="controls">
                <button class="btn btn-secondary" onclick="previousQuestion()">⬅️ Trước</button>
                <button class="btn btn-warning" onclick="skipQuestion()">⏭️ Skip</button>
                <button class="btn btn-primary" onclick="submitAnswer()" id="submitBtn" disabled>Xác nhận</button>
                <button class="btn btn-secondary" onclick="nextQuestion()" id="nextBtn" disabled>Tiếp ➡️</button>
            </div>
        </div>

        <div id="reviewMode" class="review-section hidden">
            <h2>📊 Kết quả ôn tập</h2>
            <div id="reviewStats"></div>
            <div id="wrongAnswers"></div>
            <div class="controls">
                <button class="btn btn-primary" onclick="restartReview()">🔄 Ôn lại</button>
                <button class="btn btn-warning" onclick="reviewWrongOnly()">❌ Chỉ câu sai</button>
                <button class="btn btn-secondary" onclick="exportResults()">💾 Xuất kết quả</button>
            </div>
        </div>
    </div>

    <script>
        // All questions will be inserted here
        const allQuestions = ''' + json.dumps(all_questions, ensure_ascii=False, indent=8) + ''';
        
        let currentMode = 'mixed';
        let questions = [];
        let currentQuestionIndex = 0;
        let userAnswers = [];
        let startTime = Date.now();
        let timer;
        let streak = 0;

        function setMode(mode) {
            currentMode = mode;
            
            // Update UI
            document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Generate questions based on mode
            generateQuestions();
            initializeApp();
        }

        function generateQuestions() {
            const multipleChoiceQuestions = allQuestions.filter(q => q.type === 'multiple');
            const singleChoiceQuestions = allQuestions.filter(q => q.type === 'single');
            
            switch(currentMode) {
                case 'mixed':
                    // 50 câu: 20 multiple + 30 single (random)
                    questions = [
                        ...shuffleArray(multipleChoiceQuestions).slice(0, 20),
                        ...shuffleArray(singleChoiceQuestions).slice(0, 30)
                    ];
                    break;
                case 'multiple':
                    // 30 câu multiple choice
                    questions = shuffleArray(multipleChoiceQuestions).slice(0, 30);
                    break;
                case 'hard':
                    // 25 câu khó (multiple choice + câu có nhiều options)
                    const hardQuestions = allQuestions.filter(q => 
                        q.type === 'multiple' || q.options.length > 4
                    );
                    questions = shuffleArray(hardQuestions).slice(0, 25);
                    break;
                case 'random':
                    // 100 câu random
                    questions = shuffleArray([...allQuestions]).slice(0, 100);
                    break;
            }
            
            questions = shuffleArray(questions);
            document.getElementById('totalQuestions').textContent = questions.length;
        }

        function shuffleArray(array) {
            const shuffled = [...array];
            for (let i = shuffled.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
            }
            return shuffled;
        }

        function initializeApp() {
            currentQuestionIndex = 0;
            userAnswers = [];
            startTime = Date.now();
            streak = 0;
            loadQuestion();
            startTimer();
            updateStats();
        }

        function loadQuestion() {
            if (currentQuestionIndex >= questions.length) {
                showReview();
                return;
            }

            const question = questions[currentQuestionIndex];
            document.getElementById('questionText').innerHTML = `
                <strong>Câu ${currentQuestionIndex + 1} (ID: ${question.id}):</strong><br><br>
                ${question.text}
            `;
            
            // Set question type indicator
            const typeElement = document.getElementById('questionType');
            if (question.type === 'multiple') {
                typeElement.innerHTML = `Multiple Choice (Choose ${question.correct.length}) <span class="difficulty">KHาาÓ</span>`;
            } else {
                typeElement.innerHTML = `Single Choice <span class="difficulty">NORMAL</span>`;
            }
            
            const optionsContainer = document.getElementById('optionsContainer');
            optionsContainer.innerHTML = '';
            
            question.options.forEach((option, index) => {
                const optionDiv = document.createElement('div');
                optionDiv.className = 'option';
                optionDiv.innerHTML = `
                    <strong>${String.fromCharCode(65 + index)}.</strong> ${option}
                    ${question.type === 'multiple' ? '<input type="checkbox" class="option-checkbox">' : ''}
                `;
                
                if (question.type === 'multiple') {
                    optionDiv.onclick = () => toggleMultipleOption(index);
                } else {
                    optionDiv.onclick = () => selectSingleOption(index);
                }
                
                optionDiv.dataset.index = index;
                optionsContainer.appendChild(optionDiv);
            });

            document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
            document.getElementById('submitBtn').disabled = true;
            document.getElementById('nextBtn').disabled = true;
            updateProgressBar();
        }

        function selectSingleOption(index) {
            document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
            document.querySelector(`[data-index="${index}"]`).classList.add('selected');
            document.getElementById('submitBtn').disabled = false;
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
            
            const selectedCount = document.querySelectorAll('.option.selected').length;
            document.getElementById('submitBtn').disabled = selectedCount === 0;
        }

        function getSelectedAnswers() {
            const selected = [];
            document.querySelectorAll('.option.selected').forEach(opt => {
                selected.push(parseInt(opt.dataset.index));
            });
            return selected.sort((a, b) => a - b);
        }

        function submitAnswer() {
            const selectedAnswers = getSelectedAnswers();
            if (selectedAnswers.length === 0) return;

            const question = questions[currentQuestionIndex];
            const correctAnswers = [...question.correct].sort((a, b) => a - b);
            
            let isCorrect = false;
            let isPartial = false;
            
            if (question.type === 'single') {
                isCorrect = selectedAnswers.length === 1 && selectedAnswers[0] === correctAnswers[0];
            } else {
                const selectedSet = new Set(selectedAnswers);
                const correctSet = new Set(correctAnswers);
                
                if (selectedAnswers.length === correctAnswers.length && 
                    selectedAnswers.every(ans => correctSet.has(ans))) {
                    isCorrect = true;
                } else {
                    const correctSelected = selectedAnswers.filter(ans => correctSet.has(ans));
                    const incorrectSelected = selectedAnswers.filter(ans => !correctSet.has(ans));
                    
                    if (correctSelected.length > 0 && incorrectSelected.length === 0) {
                        isPartial = true;
                    }
                }
            }

            // Update streak
            if (isCorrect) {
                streak++;
            } else {
                streak = 0;
            }

            userAnswers[currentQuestionIndex] = {
                questionId: question.id,
                selected: selectedAnswers,
                correct: correctAnswers,
                isCorrect: isCorrect,
                isPartial: isPartial,
                timeSpent: Date.now() - startTime,
                type: question.type
            };

            // Show results
            document.querySelectorAll('.option').forEach((opt, index) => {
                const isSelectedCorrect = correctAnswers.includes(index);
                const isSelectedByUser = selectedAnswers.includes(index);
                
                if (isSelectedCorrect) {
                    opt.classList.add('correct');
                } else if (isSelectedByUser) {
                    opt.classList.add('incorrect');
                }
                
                opt.onclick = null;
            });

            // Show explanation
            const explanationDiv = document.createElement('div');
            let resultClass = 'incorrect';
            let resultText = '❌ Sai rồi!';
            
            if (isCorrect) {
                resultClass = 'correct';
                resultText = '✅ Chính xác!';
            } else if (isPartial) {
                resultClass = 'partial';
                resultText = '⚠️ Đúng một phần!';
            }
            
            explanationDiv.className = `explanation ${resultClass}`;
            explanationDiv.innerHTML = `
                <strong>${resultText} Streak: ${streak}</strong><br>
                <strong>Đáp án đúng:</strong> ${correctAnswers.map(i => String.fromCharCode(65 + i)).join(', ')}<br>
                <strong>Bạn chọn:</strong> ${selectedAnswers.map(i => String.fromCharCode(65 + i)).join(', ')}<br>
                <em>Giải thích:</em> ${question.explanation}
            `;
            document.getElementById('optionsContainer').appendChild(explanationDiv);

            document.getElementById('submitBtn').style.display = 'none';
            document.getElementById('nextBtn').disabled = false;
            updateStats();
        }

        function skipQuestion() {
            userAnswers[currentQuestionIndex] = {
                questionId: questions[currentQuestionIndex].id,
                selected: [],
                correct: questions[currentQuestionIndex].correct,
                isCorrect: false,
                isPartial: false,
                timeSpent: 0,
                type: questions[currentQuestionIndex].type,
                skipped: true
            };
            
            streak = 0;
            nextQuestion();
        }

        function nextQuestion() {
            currentQuestionIndex++;
            loadQuestion();
            document.getElementById('submitBtn').style.display = 'inline-block';
        }

        function previousQuestion() {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                loadQuestion();
                document.getElementById('submitBtn').style.display = 'inline-block';
            }
        }

        function updateStats() {
            const answered = userAnswers.filter(a => a && !a.skipped).length;
            const correct = userAnswers.filter(a => a && a.isCorrect).length;
            const partial = userAnswers.filter(a => a && a.isPartial).length;
            const accuracy = answered > 0 ? Math.round(((correct + partial * 0.5) / answered) * 100) : 0;

            document.getElementById('correctCount').textContent = correct + (partial > 0 ? ` (+${partial})` : '');
            document.getElementById('wrongCount').textContent = answered - correct - partial;
            document.getElementById('accuracy').textContent = accuracy + '%';
            document.getElementById('streak').textContent = streak;
        }

        function updateProgressBar() {
            const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
        }

        function startTimer() {
            timer = setInterval(() => {
                const elapsed = Math.floor((Date.now() - startTime) / 1000);
                const minutes = Math.floor(elapsed / 60);
                const seconds = elapsed % 60;
                document.getElementById('timeSpent').textContent = 
                    `${minutes}:${seconds.toString().padStart(2, '0')}`;
            }, 1000);
        }

        function showReview() {
            clearInterval(timer);
            document.getElementById('studyMode').classList.add('hidden');
            document.getElementById('reviewMode').classList.remove('hidden');

            const correct = userAnswers.filter(a => a.isCorrect).length;
            const partial = userAnswers.filter(a => a.isPartial).length;
            const skipped = userAnswers.filter(a => a.skipped).length;
            const total = userAnswers.length;
            const accuracy = Math.round(((correct + partial * 0.5) / (total - skipped)) * 100);

            document.getElementById('reviewStats').innerHTML = `
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">${correct}/${total}</div>
                        <div>Hoàn toàn đúng</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${partial}</div>
                        <div>Đúng một phần</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${skipped}</div>
                        <div>Bỏ qua</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${accuracy}%</div>
                        <div>Điểm tổng</div>
                    </div>
                </div>
            `;

            const wrongAnswers = userAnswers.filter(a => !a.isCorrect);
            if (wrongAnswers.length > 0) {
                document.getElementById('wrongAnswers').innerHTML = `
                    <h3>🔄 Câu cần ôn lại (${wrongAnswers.length} câu):</h3>
                    ${wrongAnswers.map(a => `
                        <div class="wrong-answer">
                            <strong>Câu ID ${a.questionId} (${a.type === 'multiple' ? 'Multiple' : 'Single'}):</strong><br>
                            ${a.skipped ? 'Đã bỏ qua' : `Bạn chọn: ${a.selected.map(i => String.fromCharCode(65 + i)).join(', ')}`}<br>
                            Đáp án đúng: ${a.correct.map(i => String.fromCharCode(65 + i)).join(', ')}
                            ${a.isPartial ? ' <span style="color: #856404;">(Đúng một phần)</span>' : ''}
                        </div>
                    `).join('')}
                `;
            }
        }

        function restartReview() {
            document.getElementById('studyMode').classList.remove('hidden');
            document.getElementById('reviewMode').classList.add('hidden');
            generateQuestions();
            initializeApp();
        }

        function reviewWrongOnly() {
            const wrongQuestionIds = userAnswers.filter(a => !a.isCorrect).map(a => a.questionId);
            questions = allQuestions.filter(q => wrongQuestionIds.includes(q.id));
            
            if (questions.length === 0) {
                alert('🎉 Không có câu sai để ôn!');
                return;
            }
            
            document.getElementById('studyMode').classList.remove('hidden');
            document.getElementById('reviewMode').classList.add('hidden');
            document.getElementById('totalQuestions').textContent = questions.length;
            initializeApp();
        }

        function exportResults() {
            const results = {
                mode: currentMode,
                date: new Date().toLocaleDateString('vi-VN'),
                questions: questions.length,
                correct: userAnswers.filter(a => a.isCorrect).length,
                partial: userAnswers.filter(a => a.isPartial).length,
                skipped: userAnswers.filter(a => a.skipped).length,
                accuracy: Math.round(((userAnswers.filter(a => a.isCorrect).length + userAnswers.filter(a => a.isPartial).length * 0.5) / userAnswers.filter(a => !a.skipped).length) * 100),
                wrongQuestions: userAnswers.filter(a => !a.isCorrect).map(a => ({
                    id: a.questionId,
                    type: a.type,
                    selected: a.selected,
                    correct: a.correct,
                    skipped: a.skipped || false
                })),
                timeSpent: document.getElementById('timeSpent').textContent
            };

            const blob = new Blob([JSON.stringify(results, null, 2)], {type: 'application/json'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `aws-devops-review-${currentMode}-${new Date().toISOString().split('T')[0]}.json`;
            a.click();
        }

        // Initialize app when page loads
        window.onload = () => {
            generateQuestions();
            initializeApp();
        };
    </script>
</body>
</html>'''
    
    # Save the review app
    with open('apps/review_app.html', 'w', encoding='utf-8') as f:
        f.write(app_content)
    
    print(f"✅ Created review_app.html with {len(all_questions)} questions")
    print(f"📊 Question breakdown:")
    print(f"   - Single Choice: {len([q for q in all_questions if q['type'] == 'single'])}")
    print(f"   - Multiple Choice: {len([q for q in all_questions if q['type'] == 'multiple'])}")

if __name__ == "__main__":
    create_review_app()
