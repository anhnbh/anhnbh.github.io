#!/usr/bin/env python3
import json
import os
import random
from datetime import datetime, timedelta

def create_study_app(questions, output_file, title, exam_info):
    """Create a comprehensive study app HTML file"""
    
    # Shuffle questions for variety
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .exam-info {{
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }}
        
        .controls {{
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 1px solid #dee2e6;
        }}
        
        .progress-container {{
            background: #e9ecef;
            border-radius: 25px;
            height: 20px;
            margin-bottom: 20px;
            overflow: hidden;
        }}
        
        .progress-bar {{
            background: linear-gradient(90deg, #28a745, #20c997);
            height: 100%;
            width: 0%;
            transition: width 0.3s ease;
            border-radius: 25px;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        
        .stat-card {{
            background: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #007bff;
        }}
        
        .question-container {{
            padding: 30px;
            min-height: 400px;
        }}
        
        .question {{
            display: none;
            animation: fadeIn 0.5s ease-in;
        }}
        
        .question.active {{
            display: block;
        }}
        
        .question-header {{
            background: #007bff;
            color: white;
            padding: 15px 20px;
            border-radius: 10px 10px 0 0;
            font-weight: bold;
            font-size: 1.1em;
        }}
        
        .question-content {{
            background: #f8f9fa;
            padding: 25px;
            border: 1px solid #dee2e6;
            border-top: none;
            border-radius: 0 0 10px 10px;
        }}
        
        .question-text {{
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 25px;
            color: #333;
        }}
        
        .choices {{
            list-style: none;
        }}
        
        .choice {{
            background: white;
            margin: 10px 0;
            padding: 15px;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }}
        
        .choice:hover {{
            border-color: #007bff;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,123,255,0.15);
        }}
        
        .choice.selected {{
            border-color: #007bff;
            background: #e3f2fd;
        }}
        
        .choice.correct {{
            border-color: #28a745;
            background: #d4edda;
        }}
        
        .choice.incorrect {{
            border-color: #dc3545;
            background: #f8d7da;
        }}
        
        .choice-letter {{
            display: inline-block;
            width: 30px;
            height: 30px;
            background: #007bff;
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 30px;
            margin-right: 15px;
            font-weight: bold;
        }}
        
        .choice.correct .choice-letter {{
            background: #28a745;
        }}
        
        .choice.incorrect .choice-letter {{
            background: #dc3545;
        }}
        
        .explanation {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
            display: none;
        }}
        
        .explanation.show {{
            display: block;
            animation: slideDown 0.3s ease;
        }}
        
        .voting-info {{
            background: #e9ecef;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-size: 0.9em;
        }}
        
        .navigation {{
            padding: 30px;
            background: #f8f9fa;
            border-top: 1px solid #dee2e6;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            font-weight: bold;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, #007bff, #0056b3);
            color: white;
        }}
        
        .btn-success {{
            background: linear-gradient(135deg, #28a745, #1e7e34);
            color: white;
        }}
        
        .btn-secondary {{
            background: linear-gradient(135deg, #6c757d, #545b62);
            color: white;
        }}
        
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        
        .btn:disabled {{
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }}
        
        .timer {{
            font-size: 1.2em;
            font-weight: bold;
            color: #007bff;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes slideDown {{
            from {{ opacity: 0; transform: translateY(-10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .mode-selector {{
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        
        .mode-btn {{
            padding: 10px 20px;
            border: 2px solid #007bff;
            background: white;
            color: #007bff;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .mode-btn.active {{
            background: #007bff;
            color: white;
        }}
        
        .results-summary {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        @media (max-width: 768px) {{
            .container {{
                margin: 10px;
                border-radius: 10px;
            }}
            
            .header {{
                padding: 20px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .stats {{
                grid-template-columns: repeat(2, 1fr);
            }}
            
            .navigation {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <div class="exam-info">
                <div><strong>Total Questions:</strong> {len(questions)}</div>
                <div><strong>Multiple Choice:</strong> {sum(1 for q in questions if q.get('is_multiple_choice', False))} questions</div>
                <div><strong>Exam Format:</strong> {exam_info}</div>
            </div>
        </div>
        
        <div class="controls">
            <div class="mode-selector">
                <button class="mode-btn active" onclick="setMode('study')">Study Mode</button>
                <button class="mode-btn" onclick="setMode('practice')">Practice Test</button>
                <button class="mode-btn" onclick="setMode('review')">Review Wrong</button>
            </div>
            
            <div class="progress-container">
                <div class="progress-bar" id="progressBar"></div>
            </div>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number" id="currentQuestion">1</div>
                    <div>Current</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalQuestions">{len(questions)}</div>
                    <div>Total</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="correctCount">0</div>
                    <div>Correct</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="accuracy">0%</div>
                    <div>Accuracy</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number timer" id="timer">00:00</div>
                    <div>Time</div>
                </div>
            </div>
        </div>
        
        <div class="question-container" id="questionContainer">
            <!-- Questions will be loaded here -->
        </div>
        
        <div class="navigation">
            <button class="btn btn-secondary" onclick="previousQuestion()" id="prevBtn">Previous</button>
            <div>
                <button class="btn btn-primary" onclick="showAnswer()" id="showAnswerBtn">Show Answer</button>
                <button class="btn btn-success" onclick="nextQuestion()" id="nextBtn" style="display:none;">Next Question</button>
            </div>
            <button class="btn btn-primary" onclick="nextQuestion()" id="skipBtn">Skip</button>
        </div>
    </div>

    <script>
        const questions = {json.dumps(shuffled_questions, indent=8)};
        
        let currentQuestionIndex = 0;
        let correctAnswers = 0;
        let answeredQuestions = new Set();
        let wrongAnswers = [];
        let startTime = new Date();
        let currentMode = 'study';
        let selectedAnswers = {{}};
        
        function setMode(mode) {{
            currentMode = mode;
            document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            if (mode === 'practice') {{
                // Practice test mode - 75 questions, 180 minutes
                const practiceQuestions = questions.slice(0, 75);
                loadQuestions(practiceQuestions);
                startTimer(180 * 60); // 180 minutes
            }} else if (mode === 'review') {{
                if (wrongAnswers.length === 0) {{
                    alert('No wrong answers to review yet. Answer some questions first!');
                    return;
                }}
                loadQuestions(wrongAnswers);
            }} else {{
                loadQuestions(questions);
            }}
            
            resetStats();
            loadQuestion();
        }}
        
        function loadQuestions(questionSet) {{
            // Update the questions array for current mode
            window.currentQuestions = questionSet;
            currentQuestionIndex = 0;
            document.getElementById('totalQuestions').textContent = questionSet.length;
        }}
        
        function loadQuestion() {{
            const question = (window.currentQuestions || questions)[currentQuestionIndex];
            if (!question) return;
            
            const container = document.getElementById('questionContainer');
            const isMultipleChoice = question.is_multiple_choice;
            
            let choicesHtml = '';
            question.choices.forEach((choice, index) => {{
                const letter = String.fromCharCode(65 + index);
                choicesHtml += `
                    <li class="choice" onclick="selectChoice('${{letter}}', this)" data-choice="${{letter}}">
                        <span class="choice-letter">${{letter}}</span>
                        ${{choice}}
                    </li>
                `;
            }});
            
            let votingHtml = '';
            if (question.voting_data && Object.keys(question.voting_data).length > 0) {{
                const sortedVotes = Object.entries(question.voting_data)
                    .sort(([,a], [,b]) => b - a)
                    .slice(0, 3);
                votingHtml = `
                    <div class="voting-info">
                        <strong>Community Votes:</strong> 
                        ${{sortedVotes.map(([answer, votes]) => `${{answer}}: ${{votes}} votes`).join(', ')}}
                    </div>
                `;
            }}
            
            container.innerHTML = `
                <div class="question active">
                    <div class="question-header">
                        Question #${{question.question_number}} ${{isMultipleChoice ? '(Multiple Choice)' : '(Single Choice)'}}
                    </div>
                    <div class="question-content">
                        <div class="question-text">${{question.question_text}}</div>
                        <ul class="choices">
                            ${{choicesHtml}}
                        </ul>
                        ${{votingHtml}}
                        <div class="explanation" id="explanation">
                            <strong>Correct Answer:</strong> ${{question.correct_answer}}<br>
                            <strong>Type:</strong> ${{isMultipleChoice ? 'Multiple Choice - Select all that apply' : 'Single Choice - Select one answer'}}
                        </div>
                    </div>
                </div>
            `;
            
            updateProgress();
            updateNavigation();
        }}
        
        function selectChoice(letter, element) {{
            const question = (window.currentQuestions || questions)[currentQuestionIndex];
            const isMultipleChoice = question.is_multiple_choice;
            
            if (!isMultipleChoice) {{
                // Single choice - clear other selections
                document.querySelectorAll('.choice').forEach(choice => {{
                    choice.classList.remove('selected');
                }});
            }}
            
            element.classList.toggle('selected');
            
            // Store selected answer
            const questionId = question.question_number;
            if (!selectedAnswers[questionId]) {{
                selectedAnswers[questionId] = [];
            }}
            
            if (element.classList.contains('selected')) {{
                if (!selectedAnswers[questionId].includes(letter)) {{
                    selectedAnswers[questionId].push(letter);
                }}
            }} else {{
                selectedAnswers[questionId] = selectedAnswers[questionId].filter(a => a !== letter);
            }}
            
            if (!isMultipleChoice && selectedAnswers[questionId].length > 0) {{
                selectedAnswers[questionId] = [letter];
            }}
        }}
        
        function showAnswer() {{
            const question = (window.currentQuestions || questions)[currentQuestionIndex];
            const correctAnswer = question.correct_answer;
            const questionId = question.question_number;
            const userAnswer = selectedAnswers[questionId] || [];
            
            // Show correct/incorrect styling
            document.querySelectorAll('.choice').forEach(choice => {{
                const choiceLetter = choice.dataset.choice;
                if (correctAnswer.includes(choiceLetter)) {{
                    choice.classList.add('correct');
                }} else if (userAnswer.includes(choiceLetter)) {{
                    choice.classList.add('incorrect');
                }}
            }});
            
            // Check if answer is correct
            const isCorrect = userAnswer.length > 0 && 
                userAnswer.sort().join('') === correctAnswer.split('').sort().join('');
            
            if (!answeredQuestions.has(questionId)) {{
                answeredQuestions.add(questionId);
                if (isCorrect) {{
                    correctAnswers++;
                }} else {{
                    wrongAnswers.push(question);
                }}
            }}
            
            document.getElementById('explanation').classList.add('show');
            document.getElementById('showAnswerBtn').style.display = 'none';
            document.getElementById('nextBtn').style.display = 'inline-block';
            
            updateStats();
        }}
        
        function nextQuestion() {{
            if (currentQuestionIndex < (window.currentQuestions || questions).length - 1) {{
                currentQuestionIndex++;
                loadQuestion();
                document.getElementById('showAnswerBtn').style.display = 'inline-block';
                document.getElementById('nextBtn').style.display = 'none';
            }} else {{
                showResults();
            }}
        }}
        
        function previousQuestion() {{
            if (currentQuestionIndex > 0) {{
                currentQuestionIndex--;
                loadQuestion();
                document.getElementById('showAnswerBtn').style.display = 'inline-block';
                document.getElementById('nextBtn').style.display = 'none';
            }}
        }}
        
        function updateProgress() {{
            const progress = ((currentQuestionIndex + 1) / (window.currentQuestions || questions).length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
            document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
        }}
        
        function updateNavigation() {{
            document.getElementById('prevBtn').disabled = currentQuestionIndex === 0;
        }}
        
        function updateStats() {{
            document.getElementById('correctCount').textContent = correctAnswers;
            const accuracy = answeredQuestions.size > 0 ? Math.round((correctAnswers / answeredQuestions.size) * 100) : 0;
            document.getElementById('accuracy').textContent = accuracy + '%';
        }}
        
        function updateTimer() {{
            const now = new Date();
            const elapsed = Math.floor((now - startTime) / 1000);
            const minutes = Math.floor(elapsed / 60);
            const seconds = elapsed % 60;
            document.getElementById('timer').textContent = 
                String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
        }}
        
        function startTimer(duration) {{
            if (duration) {{
                // Countdown timer for practice mode
                let timeLeft = duration;
                const timerInterval = setInterval(() => {{
                    const minutes = Math.floor(timeLeft / 60);
                    const seconds = timeLeft % 60;
                    document.getElementById('timer').textContent = 
                        String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
                    
                    if (timeLeft <= 0) {{
                        clearInterval(timerInterval);
                        alert('Time is up!');
                        showResults();
                    }}
                    timeLeft--;
                }}, 1000);
            }}
        }}
        
        function resetStats() {{
            correctAnswers = 0;
            answeredQuestions.clear();
            selectedAnswers = {{}};
            startTime = new Date();
            updateStats();
        }}
        
        function showResults() {{
            const totalAnswered = answeredQuestions.size;
            const accuracy = totalAnswered > 0 ? Math.round((correctAnswers / totalAnswered) * 100) : 0;
            const timeElapsed = Math.floor((new Date() - startTime) / 1000 / 60);
            
            alert(`Results Summary:
            
Questions Answered: ${{totalAnswered}}
Correct Answers: ${{correctAnswers}}
Accuracy: ${{accuracy}}%
Time Taken: ${{timeElapsed}} minutes
Wrong Answers: ${{wrongAnswers.length}}

${{accuracy >= 75 ? 'Congratulations! You passed!' : 'Keep studying and try again!'}}`);
        }}
        
        // Initialize
        setInterval(updateTimer, 1000);
        loadQuestion();
    </script>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    # Load questions
    questions_file = "/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/sap_c02_questions.json"
    
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    # Create study app
    output_file = "/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/sap_c02_study_app.html"
    
    exam_info = "75 questions, 180 minutes, 750/1000 passing score"
    
    create_study_app(
        questions=questions,
        output_file=output_file,
        title="AWS Solutions Architect Professional (SAP-C02) Study App",
        exam_info=exam_info
    )
    
    print(f"Study app created: {output_file}")
    print(f"Total questions: {len(questions)}")
    print(f"Multiple choice: {sum(1 for q in questions if q.get('is_multiple_choice', False))}")

if __name__ == "__main__":
    main()
