#!/usr/bin/env python3
import json

def create_sap_app():
    """Create AWS Solutions Architect Professional study app"""
    
    # Sample questions for SAP-C02 (you'll need to extract real ones from HTML files)
    sample_questions = [
        {
            "id": 1,
            "text": "A company needs to migrate a large-scale application to AWS with minimal downtime. The application uses a relational database and requires high availability across multiple regions. What is the MOST cost-effective solution?",
            "options": [
                "Use AWS Database Migration Service with Multi-AZ RDS deployment",
                "Implement Aurora Global Database with read replicas",
                "Set up RDS with cross-region automated backups",
                "Use DynamoDB Global Tables with DMS for migration"
            ],
            "correct": [1],
            "type": "single",
            "explanation": "Aurora Global Database provides the best combination of high availability, cross-region replication, and cost-effectiveness for large-scale applications."
        },
        {
            "id": 2,
            "text": "An enterprise needs to implement a hybrid cloud architecture with the following requirements: secure connectivity, bandwidth predictability, and compliance with data residency laws. Which combination of services should be used? (Choose three)",
            "options": [
                "AWS Direct Connect",
                "AWS VPN",
                "AWS Storage Gateway",
                "AWS Outposts",
                "AWS Local Zones",
                "AWS Wavelength"
            ],
            "correct": [0, 2, 3],
            "type": "multiple",
            "explanation": "Direct Connect provides secure, predictable connectivity; Storage Gateway enables hybrid storage; Outposts helps with data residency compliance."
        }
    ]
    
    app_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS Solutions Architect Professional Study App</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; padding: 25px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.1); }}
        .cert-badge {{ background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 25px; font-size: 14px; margin-bottom: 15px; display: inline-block; backdrop-filter: blur(10px); }}
        .progress-bar {{ background: rgba(255,255,255,0.3); height: 12px; border-radius: 6px; margin: 15px 0; }}
        .progress {{ background: linear-gradient(90deg, #00d2ff, #3a7bd5); height: 100%; border-radius: 6px; transition: width 0.3s; }}
        .question-card {{ background: white; padding: 35px; border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); margin-bottom: 20px; border-left: 6px solid #ff6b6b; }}
        .question-text {{ font-size: 18px; line-height: 1.7; margin-bottom: 25px; color: #2c3e50; }}
        .question-type {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 10px 20px; border-radius: 25px; font-size: 14px; font-weight: bold; margin-bottom: 20px; display: inline-block; }}
        .difficulty {{ background: #e74c3c; color: white; padding: 6px 15px; border-radius: 20px; font-size: 12px; margin-left: 15px; }}
        .options {{ margin: 25px 0; }}
        .option {{ background: #f8f9fa; border: 3px solid #e9ecef; padding: 18px; margin: 12px 0; border-radius: 12px; cursor: pointer; transition: all 0.3s; position: relative; }}
        .option:hover {{ border-color: #ff6b6b; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
        .option.selected {{ border-color: #ff6b6b; background: linear-gradient(135deg, #fff5f5, #ffe8e8); }}
        .option.correct {{ border-color: #27ae60; background: linear-gradient(135deg, #d5f4e6, #a8e6cf); }}
        .option.incorrect {{ border-color: #e74c3c; background: linear-gradient(135deg, #ffeaea, #ffcccb); }}
        .option-checkbox {{ position: absolute; right: 18px; top: 50%; transform: translateY(-50%); width: 22px; height: 22px; }}
        .controls {{ display: flex; gap: 15px; justify-content: center; margin-top: 30px; }}
        .btn {{ padding: 14px 28px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: 600; transition: all 0.3s; }}
        .btn-primary {{ background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 5px 15px rgba(255,107,107,0.4); }}
        .btn-secondary {{ background: linear-gradient(135deg, #74b9ff, #0984e3); color: white; }}
        .btn:disabled {{ background: #bdc3c7; cursor: not-allowed; transform: none; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 25px; }}
        .stat-card {{ background: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.1); }}
        .stat-number {{ font-size: 28px; font-weight: bold; background: linear-gradient(135deg, #ff6b6b, #ee5a24); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .explanation {{ margin-top: 25px; padding: 20px; border-radius: 12px; }}
        .explanation.correct {{ background: linear-gradient(135deg, #d5f4e6, #a8e6cf); border-left: 5px solid #27ae60; }}
        .explanation.incorrect {{ background: linear-gradient(135deg, #ffeaea, #ffcccb); border-left: 5px solid #e74c3c; }}
        .hidden {{ display: none; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="cert-badge">🏗️ AWS Certified Solutions Architect - Professional</div>
            <h1>SAP-C02 Study App</h1>
            <div class="progress-bar">
                <div class="progress" id="progressBar"></div>
            </div>
            <p>Câu <span id="currentQuestion">1</span>/<span id="totalQuestions">2</span></p>
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" id="correctCount">0</div>
                <div>Câu đúng</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="wrongCount">0</div>
                <div>Câu sai</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="accuracy">0%</div>
                <div>Độ chính xác</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="timeSpent">0:00</div>
                <div>Thời gian</div>
            </div>
        </div>

        <div id="studyMode" class="question-card">
            <div class="question-type" id="questionType">Single Choice <span class="difficulty">PROFESSIONAL</span></div>
            <div class="question-text" id="questionText">
                Đang tải câu hỏi...
            </div>
            <div class="options" id="optionsContainer">
                <!-- Options will be loaded here -->
            </div>
            <div class="controls">
                <button class="btn btn-secondary" onclick="previousQuestion()">⬅️ Câu trước</button>
                <button class="btn btn-primary" onclick="submitAnswer()" id="submitBtn" disabled>Xác nhận</button>
                <button class="btn btn-secondary" onclick="nextQuestion()" id="nextBtn" disabled>Câu tiếp ➡️</button>
            </div>
        </div>
    </div>

    <script>
        const questions = {json.dumps(sample_questions, ensure_ascii=False, indent=8)};
        
        let currentQuestionIndex = 0;
        let userAnswers = [];
        let startTime = Date.now();
        let timer;

        function initializeApp() {{
            document.getElementById('totalQuestions').textContent = questions.length;
            loadQuestion();
            startTimer();
            updateStats();
        }}

        function loadQuestion() {{
            const question = questions[currentQuestionIndex];
            document.getElementById('questionText').innerHTML = `
                <strong>Câu ${{question.id}}:</strong><br><br>
                ${{question.text}}
            `;
            
            const typeElement = document.getElementById('questionType');
            if (question.type === 'multiple') {{
                typeElement.innerHTML = `Multiple Choice (Choose ${{question.correct.length}}) <span class="difficulty">PROFESSIONAL</span>`;
            }} else {{
                typeElement.innerHTML = `Single Choice <span class="difficulty">PROFESSIONAL</span>`;
            }}
            
            const optionsContainer = document.getElementById('optionsContainer');
            optionsContainer.innerHTML = '';
            
            question.options.forEach((option, index) => {{
                const optionDiv = document.createElement('div');
                optionDiv.className = 'option';
                optionDiv.innerHTML = `
                    <strong>${{String.fromCharCode(65 + index)}}.</strong> ${{option}}
                    ${{question.type === 'multiple' ? '<input type="checkbox" class="option-checkbox">' : ''}}
                `;
                
                if (question.type === 'multiple') {{
                    optionDiv.onclick = () => toggleMultipleOption(index);
                }} else {{
                    optionDiv.onclick = () => selectSingleOption(index);
                }}
                
                optionDiv.dataset.index = index;
                optionsContainer.appendChild(optionDiv);
            }});

            document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
            document.getElementById('submitBtn').disabled = true;
            document.getElementById('nextBtn').disabled = true;
            updateProgressBar();
        }}

        function selectSingleOption(index) {{
            document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
            document.querySelector(`[data-index="${{index}}"]`).classList.add('selected');
            document.getElementById('submitBtn').disabled = false;
        }}

        function toggleMultipleOption(index) {{
            const option = document.querySelector(`[data-index="${{index}}"]`);
            const checkbox = option.querySelector('.option-checkbox');
            
            if (option.classList.contains('selected')) {{
                option.classList.remove('selected');
                checkbox.checked = false;
            }} else {{
                option.classList.add('selected');
                checkbox.checked = true;
            }}
            
            const selectedCount = document.querySelectorAll('.option.selected').length;
            document.getElementById('submitBtn').disabled = selectedCount === 0;
        }}

        function getSelectedAnswers() {{
            const selected = [];
            document.querySelectorAll('.option.selected').forEach(opt => {{
                selected.push(parseInt(opt.dataset.index));
            }});
            return selected.sort((a, b) => a - b);
        }}

        function submitAnswer() {{
            const selectedAnswers = getSelectedAnswers();
            if (selectedAnswers.length === 0) return;

            const question = questions[currentQuestionIndex];
            const correctAnswers = [...question.correct].sort((a, b) => a - b);
            
            let isCorrect = false;
            
            if (question.type === 'single') {{
                isCorrect = selectedAnswers.length === 1 && selectedAnswers[0] === correctAnswers[0];
            }} else {{
                isCorrect = selectedAnswers.length === correctAnswers.length && 
                    selectedAnswers.every(ans => correctAnswers.includes(ans));
            }}

            userAnswers[currentQuestionIndex] = {{
                questionId: question.id,
                selected: selectedAnswers,
                correct: correctAnswers,
                isCorrect: isCorrect,
                type: question.type
            }};

            // Show results
            document.querySelectorAll('.option').forEach((opt, index) => {{
                const isSelectedCorrect = correctAnswers.includes(index);
                const isSelectedByUser = selectedAnswers.includes(index);
                
                if (isSelectedCorrect) {{
                    opt.classList.add('correct');
                }} else if (isSelectedByUser) {{
                    opt.classList.add('incorrect');
                }}
                
                opt.onclick = null;
            }});

            // Show explanation
            const explanationDiv = document.createElement('div');
            const resultClass = isCorrect ? 'correct' : 'incorrect';
            const resultText = isCorrect ? '✅ Chính xác!' : '❌ Sai rồi!';
            
            explanationDiv.className = `explanation ${{resultClass}}`;
            explanationDiv.innerHTML = `
                <strong>${{resultText}}</strong><br>
                <strong>Đáp án đúng:</strong> ${{correctAnswers.map(i => String.fromCharCode(65 + i)).join(', ')}}<br>
                <em>Giải thích:</em> ${{question.explanation}}
            `;
            document.getElementById('optionsContainer').appendChild(explanationDiv);

            document.getElementById('submitBtn').style.display = 'none';
            document.getElementById('nextBtn').disabled = false;
            updateStats();
        }}

        function nextQuestion() {{
            if (currentQuestionIndex < questions.length - 1) {{
                currentQuestionIndex++;
                loadQuestion();
                document.getElementById('submitBtn').style.display = 'inline-block';
            }} else {{
                showResults();
            }}
        }}

        function previousQuestion() {{
            if (currentQuestionIndex > 0) {{
                currentQuestionIndex--;
                loadQuestion();
                document.getElementById('submitBtn').style.display = 'inline-block';
            }}
        }}

        function updateStats() {{
            const answered = userAnswers.filter(a => a).length;
            const correct = userAnswers.filter(a => a && a.isCorrect).length;
            const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;

            document.getElementById('correctCount').textContent = correct;
            document.getElementById('wrongCount').textContent = answered - correct;
            document.getElementById('accuracy').textContent = accuracy + '%';
        }}

        function updateProgressBar() {{
            const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
        }}

        function startTimer() {{
            timer = setInterval(() => {{
                const elapsed = Math.floor((Date.now() - startTime) / 1000);
                const minutes = Math.floor(elapsed / 60);
                const seconds = elapsed % 60;
                document.getElementById('timeSpent').textContent = 
                    `${{minutes}}:${{seconds.toString().padStart(2, '0')}}`;
            }}, 1000);
        }}

        function showResults() {{
            const correct = userAnswers.filter(a => a.isCorrect).length;
            const total = userAnswers.length;
            const accuracy = Math.round((correct / total) * 100);
            
            alert(`🎉 Hoàn thành!\\n\\nKết quả: ${{correct}}/${{total}} (${{accuracy}}%)\\n\\nAWS Solutions Architect Professional - Keep studying!`);
        }}

        window.onload = initializeApp;
    </script>
</body>
</html>'''
    
    with open('sap_study_app.html', 'w', encoding='utf-8') as f:
        f.write(app_content)
    
    print("✅ Created AWS Solutions Architect Professional study app")

if __name__ == "__main__":
    create_sap_app()
