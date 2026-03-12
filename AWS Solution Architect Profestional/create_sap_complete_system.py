#!/usr/bin/env python3
import json
import os
import math
import random
from datetime import datetime, timedelta

def create_exam_mode():
    """Create practice exam with 75 questions, 180 minutes"""
    with open('sap_c02_questions.json', 'r') as f:
        all_questions = json.load(f)
    
    # Select 75 random questions
    exam_questions = random.sample(all_questions, 75)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAP-C02 Practice Exam</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #dc3545, #c82333); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #dc3545, #c82333); color: white; padding: 30px; text-align: center; border-radius: 15px 15px 0 0; }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .timer-section {{ background: #f8f9fa; padding: 20px; text-align: center; border-bottom: 1px solid #dee2e6; }}
        .timer {{ font-size: 2em; font-weight: bold; color: #dc3545; }}
        .question-nav {{ background: #f8f9fa; padding: 15px; display: flex; justify-content: space-between; align-items: center; }}
        .question-container {{ padding: 30px; min-height: 400px; }}
        .question {{ display: none; }}
        .question.active {{ display: block; }}
        .question-header {{ background: #dc3545; color: white; padding: 15px 20px; border-radius: 10px 10px 0 0; font-weight: bold; }}
        .question-content {{ background: #f8f9fa; padding: 25px; border: 1px solid #dee2e6; border-top: none; border-radius: 0 0 10px 10px; }}
        .question-text {{ font-size: 1.1em; line-height: 1.6; margin-bottom: 25px; }}
        .choices {{ list-style: none; }}
        .choice {{ background: white; margin: 10px 0; padding: 15px; border: 2px solid #dee2e6; border-radius: 8px; cursor: pointer; transition: all 0.3s ease; }}
        .choice:hover {{ border-color: #dc3545; }}
        .choice.selected {{ border-color: #dc3545; background: #f8d7da; }}
        .choice-letter {{ display: inline-block; width: 30px; height: 30px; background: #dc3545; color: white; border-radius: 50%; text-align: center; line-height: 30px; margin-right: 15px; font-weight: bold; }}
        .btn {{ padding: 12px 24px; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; transition: all 0.3s ease; }}
        .btn-danger {{ background: linear-gradient(135deg, #dc3545, #c82333); color: white; }}
        .btn-success {{ background: linear-gradient(135deg, #28a745, #1e7e34); color: white; }}
        .btn:hover {{ transform: translateY(-2px); }}
        .question-grid {{ display: grid; grid-template-columns: repeat(15, 1fr); gap: 5px; margin: 20px 0; }}
        .q-num {{ width: 40px; height: 40px; border: 2px solid #dee2e6; border-radius: 5px; display: flex; align-items: center; justify-content: center; cursor: pointer; font-weight: bold; }}
        .q-num.answered {{ background: #28a745; color: white; border-color: #28a745; }}
        .q-num.current {{ background: #dc3545; color: white; border-color: #dc3545; }}
        .results {{ display: none; padding: 30px; text-align: center; }}
        .results.show {{ display: block; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 SAP-C02 Practice Exam</h1>
            <p>75 Questions • 180 Minutes • 750/1000 to Pass</p>
        </div>
        
        <div class="timer-section">
            <div class="timer" id="timer">03:00:00</div>
            <p>Time Remaining</p>
        </div>
        
        <div class="question-nav">
            <div>Question <span id="currentQ">1</span> of 75</div>
            <div class="question-grid" id="questionGrid"></div>
            <button class="btn btn-danger" onclick="submitExam()">Submit Exam</button>
        </div>
        
        <div class="question-container" id="questionContainer"></div>
        
        <div class="question-nav">
            <button class="btn btn-danger" onclick="previousQuestion()" id="prevBtn">Previous</button>
            <button class="btn btn-danger" onclick="nextQuestion()" id="nextBtn">Next</button>
        </div>
        
        <div class="results" id="results">
            <h2>Exam Results</h2>
            <div id="resultContent"></div>
        </div>
    </div>

    <script>
        const questions = {json.dumps(exam_questions, indent=8)};
        let currentQuestionIndex = 0;
        let answers = {{}};
        let timeLeft = 180 * 60; // 180 minutes
        
        function initExam() {{
            createQuestionGrid();
            loadQuestion();
            startTimer();
        }}
        
        function createQuestionGrid() {{
            const grid = document.getElementById('questionGrid');
            for (let i = 1; i <= 75; i++) {{
                const qNum = document.createElement('div');
                qNum.className = 'q-num';
                qNum.textContent = i;
                qNum.onclick = () => goToQuestion(i - 1);
                qNum.id = `q-${{i}}`;
                grid.appendChild(qNum);
            }}
            updateQuestionGrid();
        }}
        
        function updateQuestionGrid() {{
            for (let i = 1; i <= 75; i++) {{
                const qNum = document.getElementById(`q-${{i}}`);
                qNum.className = 'q-num';
                if (i - 1 === currentQuestionIndex) qNum.classList.add('current');
                if (answers[i - 1]) qNum.classList.add('answered');
            }}
        }}
        
        function loadQuestion() {{
            const question = questions[currentQuestionIndex];
            const container = document.getElementById('questionContainer');
            
            let choicesHtml = '';
            question.choices.forEach((choice, index) => {{
                const letter = String.fromCharCode(65 + index);
                const isSelected = answers[currentQuestionIndex] && answers[currentQuestionIndex].includes(letter);
                choicesHtml += `
                    <li class="choice ${{isSelected ? 'selected' : ''}}" onclick="selectChoice('${{letter}}', this)" data-choice="${{letter}}">
                        <span class="choice-letter">${{letter}}</span>
                        ${{choice}}
                    </li>
                `;
            }});
            
            container.innerHTML = `
                <div class="question active">
                    <div class="question-header">
                        Question #${{currentQuestionIndex + 1}} ${{question.is_multiple_choice ? '(Multiple Choice)' : '(Single Choice)'}}
                    </div>
                    <div class="question-content">
                        <div class="question-text">${{question.question_text}}</div>
                        <ul class="choices">
                            ${{choicesHtml}}
                        </ul>
                    </div>
                </div>
            `;
            
            document.getElementById('currentQ').textContent = currentQuestionIndex + 1;
            updateQuestionGrid();
        }}
        
        function selectChoice(letter, element) {{
            const question = questions[currentQuestionIndex];
            
            if (!question.is_multiple_choice) {{
                document.querySelectorAll('.choice').forEach(choice => choice.classList.remove('selected'));
                answers[currentQuestionIndex] = [letter];
            }} else {{
                if (!answers[currentQuestionIndex]) answers[currentQuestionIndex] = [];
                if (element.classList.contains('selected')) {{
                    element.classList.remove('selected');
                    answers[currentQuestionIndex] = answers[currentQuestionIndex].filter(a => a !== letter);
                }} else {{
                    element.classList.add('selected');
                    answers[currentQuestionIndex].push(letter);
                }}
            }}
            
            element.classList.toggle('selected');
            updateQuestionGrid();
        }}
        
        function goToQuestion(index) {{
            currentQuestionIndex = index;
            loadQuestion();
        }}
        
        function nextQuestion() {{
            if (currentQuestionIndex < 74) {{
                currentQuestionIndex++;
                loadQuestion();
            }}
        }}
        
        function previousQuestion() {{
            if (currentQuestionIndex > 0) {{
                currentQuestionIndex--;
                loadQuestion();
            }}
        }}
        
        function startTimer() {{
            const timerInterval = setInterval(() => {{
                const hours = Math.floor(timeLeft / 3600);
                const minutes = Math.floor((timeLeft % 3600) / 60);
                const seconds = timeLeft % 60;
                
                document.getElementById('timer').textContent = 
                    String(hours).padStart(2, '0') + ':' + 
                    String(minutes).padStart(2, '0') + ':' + 
                    String(seconds).padStart(2, '0');
                
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval);
                    submitExam();
                }}
                timeLeft--;
            }}, 1000);
        }}
        
        function submitExam() {{
            let correct = 0;
            let answered = 0;
            
            questions.forEach((question, index) => {{
                if (answers[index]) {{
                    answered++;
                    const userAnswer = answers[index].sort().join('');
                    const correctAnswer = question.correct_answer.split('').sort().join('');
                    if (userAnswer === correctAnswer) correct++;
                }}
            }});
            
            const score = Math.round((correct / 75) * 1000);
            const passed = score >= 750;
            
            document.getElementById('resultContent').innerHTML = `
                <h3 style="color: ${{passed ? '#28a745' : '#dc3545'}}">
                    ${{passed ? '🎉 PASSED!' : '❌ FAILED'}}
                </h3>
                <p><strong>Score:</strong> ${{score}}/1000</p>
                <p><strong>Correct:</strong> ${{correct}}/75 (${{Math.round(correct/75*100)}}%)</p>
                <p><strong>Answered:</strong> ${{answered}}/75</p>
                <p><strong>Passing Score:</strong> 750/1000</p>
                <br>
                <button class="btn btn-danger" onclick="location.reload()">Retake Exam</button>
            `;
            
            document.getElementById('results').classList.add('show');
            document.querySelector('.question-container').style.display = 'none';
            document.querySelectorAll('.question-nav').forEach(nav => nav.style.display = 'none');
        }}
        
        initExam();
    </script>
</body>
</html>"""
    
    with open('sap_exam_mode.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def create_review_modes():
    """Create different review modes"""
    with open('sap_c02_questions.json', 'r') as f:
        all_questions = json.load(f)
    
    # Multiple choice only
    mc_questions = [q for q in all_questions if q.get('is_multiple_choice', False)]
    
    # Hard questions (with voting data showing disagreement)
    hard_questions = []
    for q in all_questions:
        if q.get('voting_data') and len(q['voting_data']) > 1:
            votes = list(q['voting_data'].values())
            if len(votes) > 1 and max(votes) / sum(votes) < 0.7:  # Less than 70% consensus
                hard_questions.append(q)
    
    modes = {
        'sap_review_mixed.html': random.sample(all_questions, min(100, len(all_questions))),
        'sap_review_multiple_choice.html': mc_questions,
        'sap_review_hard.html': hard_questions[:50] if hard_questions else all_questions[:50],
        'sap_review_random.html': random.sample(all_questions, min(150, len(all_questions)))
    }
    
    for filename, questions in modes.items():
        mode_name = filename.replace('sap_review_', '').replace('.html', '').replace('_', ' ').title()
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAP-C02 Review - {mode_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #17a2b8, #138496); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #17a2b8, #138496); color: white; padding: 30px; text-align: center; border-radius: 15px 15px 0 0; }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .progress {{ background: #e9ecef; border-radius: 25px; height: 20px; margin: 20px 30px; }}
        .progress-bar {{ background: linear-gradient(90deg, #17a2b8, #138496); height: 100%; width: 0%; transition: width 0.3s ease; border-radius: 25px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 15px; padding: 20px 30px; }}
        .stat-card {{ background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center; }}
        .stat-number {{ font-size: 1.8em; font-weight: bold; color: #17a2b8; }}
        .question-container {{ padding: 30px; }}
        .question {{ display: none; }}
        .question.active {{ display: block; }}
        .question-header {{ background: #17a2b8; color: white; padding: 15px 20px; border-radius: 10px 10px 0 0; font-weight: bold; }}
        .question-content {{ background: #f8f9fa; padding: 25px; border: 1px solid #dee2e6; border-top: none; border-radius: 0 0 10px 10px; }}
        .question-text {{ font-size: 1.1em; line-height: 1.6; margin-bottom: 25px; }}
        .choices {{ list-style: none; }}
        .choice {{ background: white; margin: 10px 0; padding: 15px; border: 2px solid #dee2e6; border-radius: 8px; cursor: pointer; transition: all 0.3s ease; }}
        .choice:hover {{ border-color: #17a2b8; }}
        .choice.selected {{ border-color: #17a2b8; background: #d1ecf1; }}
        .choice.correct {{ border-color: #28a745; background: #d4edda; }}
        .choice.incorrect {{ border-color: #dc3545; background: #f8d7da; }}
        .choice-letter {{ display: inline-block; width: 30px; height: 30px; background: #17a2b8; color: white; border-radius: 50%; text-align: center; line-height: 30px; margin-right: 15px; font-weight: bold; }}
        .choice.correct .choice-letter {{ background: #28a745; }}
        .choice.incorrect .choice-letter {{ background: #dc3545; }}
        .explanation {{ background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 20px; margin-top: 20px; display: none; }}
        .explanation.show {{ display: block; }}
        .navigation {{ padding: 30px; background: #f8f9fa; display: flex; justify-content: space-between; align-items: center; }}
        .btn {{ padding: 12px 24px; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; transition: all 0.3s ease; }}
        .btn-info {{ background: linear-gradient(135deg, #17a2b8, #138496); color: white; }}
        .btn-success {{ background: linear-gradient(135deg, #28a745, #1e7e34); color: white; }}
        .btn:hover {{ transform: translateY(-2px); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔄 SAP-C02 Review</h1>
            <h2>{mode_name} Mode</h2>
            <p>{len(questions)} questions selected for review</p>
        </div>
        
        <div class="progress">
            <div class="progress-bar" id="progressBar"></div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="currentQuestion">1</div>
                <div>Current</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(questions)}</div>
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
        </div>
        
        <div class="question-container" id="questionContainer"></div>
        
        <div class="navigation">
            <button class="btn btn-info" onclick="previousQuestion()" id="prevBtn">Previous</button>
            <div>
                <button class="btn btn-info" onclick="showAnswer()" id="showAnswerBtn">Show Answer</button>
                <button class="btn btn-success" onclick="nextQuestion()" id="nextBtn" style="display:none;">Next Question</button>
            </div>
            <button class="btn btn-info" onclick="nextQuestion()" id="skipBtn">Skip</button>
        </div>
    </div>

    <script>
        const questions = {json.dumps(questions, indent=8)};
        let currentQuestionIndex = 0;
        let correctAnswers = 0;
        let answeredQuestions = new Set();
        let selectedAnswers = {{}};
        
        function loadQuestion() {{
            const question = questions[currentQuestionIndex];
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
                        <div class="explanation" id="explanation">
                            <strong>Correct Answer:</strong> ${{question.correct_answer}}<br>
                            <strong>Type:</strong> ${{isMultipleChoice ? 'Multiple Choice - Select all that apply' : 'Single Choice - Select one answer'}}
                        </div>
                    </div>
                </div>
            `;
            
            updateProgress();
        }}
        
        function selectChoice(letter, element) {{
            const question = questions[currentQuestionIndex];
            const isMultipleChoice = question.is_multiple_choice;
            
            if (!isMultipleChoice) {{
                document.querySelectorAll('.choice').forEach(choice => choice.classList.remove('selected'));
            }}
            
            element.classList.toggle('selected');
            
            const questionId = question.question_number;
            if (!selectedAnswers[questionId]) selectedAnswers[questionId] = [];
            
            if (element.classList.contains('selected')) {{
                if (!selectedAnswers[questionId].includes(letter)) selectedAnswers[questionId].push(letter);
            }} else {{
                selectedAnswers[questionId] = selectedAnswers[questionId].filter(a => a !== letter);
            }}
            
            if (!isMultipleChoice && selectedAnswers[questionId].length > 0) {{
                selectedAnswers[questionId] = [letter];
            }}
        }}
        
        function showAnswer() {{
            const question = questions[currentQuestionIndex];
            const correctAnswer = question.correct_answer;
            const questionId = question.question_number;
            const userAnswer = selectedAnswers[questionId] || [];
            
            document.querySelectorAll('.choice').forEach(choice => {{
                const choiceLetter = choice.dataset.choice;
                if (correctAnswer.includes(choiceLetter)) {{
                    choice.classList.add('correct');
                }} else if (userAnswer.includes(choiceLetter)) {{
                    choice.classList.add('incorrect');
                }}
            }});
            
            const isCorrect = userAnswer.length > 0 && 
                userAnswer.sort().join('') === correctAnswer.split('').sort().join('');
            
            if (!answeredQuestions.has(questionId)) {{
                answeredQuestions.add(questionId);
                if (isCorrect) correctAnswers++;
            }}
            
            document.getElementById('explanation').classList.add('show');
            document.getElementById('showAnswerBtn').style.display = 'none';
            document.getElementById('nextBtn').style.display = 'inline-block';
            
            updateStats();
        }}
        
        function nextQuestion() {{
            if (currentQuestionIndex < questions.length - 1) {{
                currentQuestionIndex++;
                loadQuestion();
                document.getElementById('showAnswerBtn').style.display = 'inline-block';
                document.getElementById('nextBtn').style.display = 'none';
            }} else {{
                const accuracy = Math.round((correctAnswers / answeredQuestions.size) * 100);
                alert(`Review Complete!\\n\\nCorrect: ${{correctAnswers}}/${{answeredQuestions.size}}\\nAccuracy: ${{accuracy}}%`);
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
            const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
            document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
        }}
        
        function updateStats() {{
            document.getElementById('correctCount').textContent = correctAnswers;
            const accuracy = answeredQuestions.size > 0 ? Math.round((correctAnswers / answeredQuestions.size) * 100) : 0;
            document.getElementById('accuracy').textContent = accuracy + '%';
        }}
        
        loadQuestion();
    </script>
</body>
</html>"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

def create_export_formats():
    """Export questions to different formats"""
    with open('sap_c02_questions.json', 'r') as f:
        questions = json.load(f)
    
    # Markdown export
    md_content = "# AWS SAP-C02 Questions\n\n"
    for i, q in enumerate(questions, 1):
        md_content += f"## Question {i}\n\n"
        md_content += f"{q['question_text']}\n\n"
        for j, choice in enumerate(q['choices']):
            letter = chr(65 + j)
            md_content += f"{letter}. {choice}\n"
        md_content += f"\n**Answer:** {q['correct_answer']}\n"
        md_content += f"**Type:** {'Multiple Choice' if q.get('is_multiple_choice') else 'Single Choice'}\n\n"
        md_content += "---\n\n"
    
    with open('sap_c02_questions.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    # CSV export
    import csv
    with open('sap_c02_questions.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Question Number', 'Question Text', 'Choices', 'Correct Answer', 'Multiple Choice'])
        for q in questions:
            choices_str = ' | '.join([f"{chr(65+i)}. {choice}" for i, choice in enumerate(q['choices'])])
            writer.writerow([
                q['question_number'],
                q['question_text'],
                choices_str,
                q['correct_answer'],
                q.get('is_multiple_choice', False)
            ])

def main():
    print("🚀 Creating SAP-C02 Complete Study System...")
    
    # Create exam mode
    print("📝 Creating practice exam mode...")
    create_exam_mode()
    
    # Create review modes
    print("🔄 Creating review modes...")
    create_review_modes()
    
    # Export to different formats
    print("📤 Exporting to different formats...")
    create_export_formats()
    
    print("✅ SAP-C02 Complete Study System Created!")
    print("\nFiles created:")
    print("- sap_exam_mode.html (Practice Exam)")
    print("- sap_review_mixed.html (Mixed Review)")
    print("- sap_review_multiple_choice.html (MC Only)")
    print("- sap_review_hard.html (Hard Questions)")
    print("- sap_review_random.html (Random Review)")
    print("- sap_c02_questions.md (Markdown)")
    print("- sap_c02_questions.csv (CSV)")

if __name__ == "__main__":
    main()
