#!/usr/bin/env python3
import json
import os
import math
from datetime import datetime, timedelta

def create_daily_study_app(questions, day, output_file):
    """Create daily study app with specific questions"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAP-C02 Day {day} Study</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #6f42c1, #5a32a3); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); overflow: hidden; }}
        .header {{ background: linear-gradient(135deg, #6f42c1, #5a32a3); color: white; padding: 30px; text-align: center; }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .progress {{ background: #e9ecef; border-radius: 25px; height: 20px; margin: 20px 30px; }}
        .progress-bar {{ background: linear-gradient(90deg, #28a745, #20c997); height: 100%; width: 0%; transition: width 0.3s ease; border-radius: 25px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 15px; padding: 20px 30px; }}
        .stat-card {{ background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center; }}
        .stat-number {{ font-size: 1.8em; font-weight: bold; color: #6f42c1; }}
        .question-container {{ padding: 30px; }}
        .question {{ display: none; }}
        .question.active {{ display: block; }}
        .question-header {{ background: #6f42c1; color: white; padding: 15px 20px; border-radius: 10px 10px 0 0; font-weight: bold; }}
        .question-content {{ background: #f8f9fa; padding: 25px; border: 1px solid #dee2e6; border-top: none; border-radius: 0 0 10px 10px; }}
        .question-text {{ font-size: 1.1em; line-height: 1.6; margin-bottom: 25px; }}
        .choices {{ list-style: none; }}
        .choice {{ background: white; margin: 10px 0; padding: 15px; border: 2px solid #dee2e6; border-radius: 8px; cursor: pointer; transition: all 0.3s ease; }}
        .choice:hover {{ border-color: #6f42c1; transform: translateY(-2px); }}
        .choice.selected {{ border-color: #6f42c1; background: #f3e5f5; }}
        .choice.correct {{ border-color: #28a745; background: #d4edda; }}
        .choice.incorrect {{ border-color: #dc3545; background: #f8d7da; }}
        .choice-letter {{ display: inline-block; width: 30px; height: 30px; background: #6f42c1; color: white; border-radius: 50%; text-align: center; line-height: 30px; margin-right: 15px; font-weight: bold; }}
        .choice.correct .choice-letter {{ background: #28a745; }}
        .choice.incorrect .choice-letter {{ background: #dc3545; }}
        .explanation {{ background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px; padding: 20px; margin-top: 20px; display: none; }}
        .explanation.show {{ display: block; }}
        .navigation {{ padding: 30px; background: #f8f9fa; display: flex; justify-content: space-between; align-items: center; }}
        .btn {{ padding: 12px 24px; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; transition: all 0.3s ease; }}
        .btn-primary {{ background: linear-gradient(135deg, #6f42c1, #5a32a3); color: white; }}
        .btn-success {{ background: linear-gradient(135deg, #28a745, #1e7e34); color: white; }}
        .btn:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
        .btn:disabled {{ opacity: 0.6; cursor: not-allowed; transform: none; }}
        @media (max-width: 768px) {{ .navigation {{ flex-direction: column; gap: 15px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 SAP-C02 Day {day}</h1>
            <p>{len(questions)} questions for today's study session</p>
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
            <button class="btn btn-primary" onclick="previousQuestion()" id="prevBtn">Previous</button>
            <div>
                <button class="btn btn-primary" onclick="showAnswer()" id="showAnswerBtn">Show Answer</button>
                <button class="btn btn-success" onclick="nextQuestion()" id="nextBtn" style="display:none;">Next Question</button>
            </div>
            <button class="btn btn-primary" onclick="nextQuestion()" id="skipBtn">Skip</button>
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
            updateNavigation();
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
                alert(`Day {day} Complete!\\n\\nCorrect: ${{correctAnswers}}/${{answeredQuestions.size}}\\nAccuracy: ${{accuracy}}%\\n\\nGreat job! See you tomorrow!`);
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
        
        function updateNavigation() {{
            document.getElementById('prevBtn').disabled = currentQuestionIndex === 0;
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
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    # Load questions
    with open('/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/sap_c02_questions.json', 'r') as f:
        all_questions = json.load(f)
    
    # Create 30-day study plan (17-18 questions per day)
    questions_per_day = math.ceil(len(all_questions) / 30)
    
    for day in range(1, 31):
        start_idx = (day - 1) * questions_per_day
        end_idx = min(start_idx + questions_per_day, len(all_questions))
        daily_questions = all_questions[start_idx:end_idx]
        
        if daily_questions:
            output_file = f'/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/day_{day:02d}_study.html'
            create_daily_study_app(daily_questions, day, output_file)
    
    # Create 7-day review plan (mixed questions)
    import random
    review_questions = all_questions.copy()
    random.shuffle(review_questions)
    
    review_per_day = math.ceil(len(review_questions) / 7)
    
    for day in range(1, 8):
        start_idx = (day - 1) * review_per_day
        end_idx = min(start_idx + review_per_day, len(review_questions))
        daily_questions = review_questions[start_idx:end_idx]
        
        if daily_questions:
            output_file = f'/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/review_day_{day}_study.html'
            create_daily_study_app(daily_questions, f"Review {day}", output_file)
    
    print(f"✅ Created 30-day study plan ({questions_per_day} questions/day)")
    print(f"✅ Created 7-day review plan ({review_per_day} questions/day)")
    print(f"📚 Total: {len(all_questions)} questions")

if __name__ == "__main__":
    main()
