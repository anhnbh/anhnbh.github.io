#!/usr/bin/env python3
import os
import shutil
import json

def organize_repo():
    """Organize SAP-C02 repo like DevOps Pro final_repo structure"""
    
    # Create final_repo structure
    final_repo = "final_repo"
    if os.path.exists(final_repo):
        shutil.rmtree(final_repo)
    
    os.makedirs(final_repo)
    os.makedirs(f"{final_repo}/daily_study")
    os.makedirs(f"{final_repo}/review_days")
    os.makedirs(f"{final_repo}/exports")
    
    # Move files to organized structure
    files_to_move = {
        # Main apps
        "sap_c02_study_app.html": f"{final_repo}/main_study_app.html",
        "sap_exam_mode.html": f"{final_repo}/exam_mode.html",
        
        # Review modes
        "sap_review_mixed.html": f"{final_repo}/review_mixed.html",
        "sap_review_multiple_choice.html": f"{final_repo}/review_multiple_choice.html", 
        "sap_review_hard.html": f"{final_repo}/review_hard.html",
        "sap_review_random.html": f"{final_repo}/review_random.html",
        
        # Data
        "sap_c02_questions.json": f"{final_repo}/questions.json",
        
        # Exports
        "sap_c02_questions.md": f"{final_repo}/exports/questions.md",
        "sap_c02_questions.csv": f"{final_repo}/exports/questions.csv",
    }
    
    # Move daily study files
    for i in range(1, 31):
        src = f"day_{i:02d}_study.html"
        if os.path.exists(src):
            shutil.move(src, f"{final_repo}/daily_study/day_{i:02d}.html")
    
    # Move review day files
    for i in range(1, 8):
        src = f"review_day_{i}_study.html"
        if os.path.exists(src):
            shutil.move(src, f"{final_repo}/review_days/review_day_{i}.html")
    
    # Move other files
    for src, dst in files_to_move.items():
        if os.path.exists(src):
            shutil.move(src, dst)
    
    # Create master launcher
    create_master_launcher()
    
    print("✅ Repository organized successfully!")
    print(f"📁 Structure created in: {final_repo}/")

def create_master_launcher():
    """Create master launcher with correct paths"""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAP-C02 Study Hub</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #6f42c1, #5a32a3); min-height: 100vh; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; background: white; border-radius: 20px; box-shadow: 0 25px 50px rgba(0,0,0,0.15); overflow: hidden; }
        .header { background: linear-gradient(135deg, #6f42c1, #5a32a3); color: white; padding: 40px; text-align: center; }
        .header h1 { font-size: 3em; margin-bottom: 15px; }
        .section { padding: 30px; }
        .section h2 { font-size: 2em; margin-bottom: 20px; color: #333; text-align: center; }
        .apps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .app-card { background: #f8f9fa; border: 2px solid #dee2e6; border-radius: 15px; padding: 25px; text-align: center; transition: all 0.3s ease; }
        .app-card:hover { border-color: #6f42c1; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .app-title { font-size: 1.5em; font-weight: bold; color: #6f42c1; margin-bottom: 15px; }
        .app-desc { color: #6c757d; margin-bottom: 20px; line-height: 1.5; }
        .btn { display: inline-block; padding: 12px 25px; background: linear-gradient(135deg, #6f42c1, #5a32a3); color: white; text-decoration: none; border-radius: 25px; font-weight: bold; transition: all 0.3s ease; margin: 5px; }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .btn-danger { background: linear-gradient(135deg, #dc3545, #c82333); }
        .btn-info { background: linear-gradient(135deg, #17a2b8, #138496); }
        .btn-success { background: linear-gradient(135deg, #28a745, #1e7e34); }
        .days-section { background: #f8f9fa; }
        .days-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; }
        .day-card { background: white; border: 2px solid #dee2e6; border-radius: 10px; padding: 15px; text-align: center; transition: all 0.3s ease; }
        .day-card:hover { border-color: #6f42c1; transform: translateY(-3px); }
        .day-title { font-weight: bold; color: #6f42c1; margin-bottom: 8px; }
        .day-info { font-size: 0.9em; color: #6c757d; margin-bottom: 10px; }
        .day-btn { padding: 8px 15px; font-size: 0.9em; }
        .review-card { background: linear-gradient(135deg, #28a745, #20c997); color: white; border-color: #28a745; }
        .review-card .day-title { color: white; }
        .review-card .day-info { color: rgba(255,255,255,0.9); }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
        .stat-card { background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        .stat-number { font-size: 2.5em; font-weight: bold; color: #6f42c1; }
        .stat-label { color: #6c757d; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 SAP-C02 Study Hub</h1>
            <p>AWS Solutions Architect Professional - Complete Study System</p>
        </div>
        
        <div class="section">
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">529</div>
                    <div class="stat-label">Total Questions</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">108</div>
                    <div class="stat-label">Multiple Choice</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">37</div>
                    <div class="stat-label">Study Days</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">750</div>
                    <div class="stat-label">Pass Score</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>📚 Main Study Apps</h2>
            <div class="apps-grid">
                <div class="app-card">
                    <div class="app-title">🎯 Complete Study App</div>
                    <div class="app-desc">All 529 questions with multiple study modes, progress tracking, and practice tests</div>
                    <a href="main_study_app.html" class="btn">Start Studying</a>
                </div>
                
                <div class="app-card">
                    <div class="app-title">📝 Practice Exam</div>
                    <div class="app-desc">Realistic exam simulation: 75 questions, 180 minutes, AWS exam format</div>
                    <a href="exam_mode.html" class="btn btn-danger">Take Practice Exam</a>
                </div>
                
                <div class="app-card">
                    <div class="app-title">🔄 Review Modes</div>
                    <div class="app-desc">Targeted review sessions for different question types and difficulty levels</div>
                    <a href="review_mixed.html" class="btn btn-info">Mixed Review</a>
                    <a href="review_multiple_choice.html" class="btn btn-info">MC Only</a>
                    <a href="review_hard.html" class="btn btn-info">Hard Questions</a>
                </div>
            </div>
        </div>
        
        <div class="section days-section">
            <h2>📅 30-Day Study Plan</h2>
            <p style="text-align: center; margin-bottom: 20px; color: #6c757d;">18 questions per day • Build knowledge foundation</p>
            <div class="days-grid">"""

    # Add daily study days
    for i in range(1, 31):
        html_content += f"""
                <div class="day-card">
                    <div class="day-title">Day {i}</div>
                    <div class="day-info">18 Questions</div>
                    <a href="daily_study/day_{i:02d}.html" class="btn day-btn">Study</a>
                </div>"""

    html_content += """
            </div>
        </div>
        
        <div class="section">
            <h2>🔄 7-Day Review Plan</h2>
            <p style="text-align: center; margin-bottom: 20px; color: #6c757d;">76 questions per day • Intensive final review</p>
            <div class="days-grid">"""

    # Add review days
    for i in range(1, 8):
        html_content += f"""
                <div class="day-card review-card">
                    <div class="day-title">Review {i}</div>
                    <div class="day-info">76 Questions</div>
                    <a href="review_days/review_day_{i}.html" class="btn day-btn">Review</a>
                </div>"""

    html_content += """
            </div>
        </div>
        
        <div class="section" style="background: #f8f9fa; text-align: center;">
            <h2>📊 Study Strategy</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">
                <div style="background: white; padding: 20px; border-radius: 10px;">
                    <h3>📚 Phase 1: Learning</h3>
                    <p>Days 1-30: Study 18 questions daily<br>Build comprehensive knowledge base</p>
                </div>
                <div style="background: white; padding: 20px; border-radius: 10px;">
                    <h3>🔄 Phase 2: Review</h3>
                    <p>Days 31-37: Review 76 questions daily<br>Reinforce and solidify learning</p>
                </div>
                <div style="background: white; padding: 20px; border-radius: 10px;">
                    <h3>🎯 Exam Day</h3>
                    <p>75 questions in 180 minutes<br>Score 750/1000 to pass</p>
                </div>
            </div>
            
            <div style="margin-top: 30px;">
                <h3>📤 Export Options</h3>
                <a href="exports/questions.md" class="btn btn-info">Markdown</a>
                <a href="exports/questions.csv" class="btn btn-info">CSV</a>
                <a href="questions.json" class="btn btn-info">JSON</a>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    with open("final_repo/master_launcher.html", 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    organize_repo()
