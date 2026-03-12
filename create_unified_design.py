#!/usr/bin/env python3

def create_unified_master_launchers():
    """Create unified design for all master launchers"""
    
    # Base template with unified design
    base_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, {gradient}); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 20px; box-shadow: 0 25px 50px rgba(0,0,0,0.15); overflow: hidden; }}
        .header {{ background: linear-gradient(135deg, {gradient}); color: white; padding: 40px; text-align: center; }}
        .header h1 {{ font-size: 3em; margin-bottom: 15px; }}
        .section {{ padding: 30px; }}
        .section h2 {{ font-size: 2em; margin-bottom: 20px; color: #333; text-align: center; }}
        .apps-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .app-card {{ background: #f8f9fa; border: 2px solid #dee2e6; border-radius: 15px; padding: 25px; text-align: center; transition: all 0.3s ease; }}
        .app-card:hover {{ border-color: {primary_color}; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .app-title {{ font-size: 1.5em; font-weight: bold; color: {primary_color}; margin-bottom: 15px; }}
        .app-desc {{ color: #6c757d; margin-bottom: 20px; line-height: 1.5; }}
        .btn {{ display: inline-block; padding: 12px 25px; background: linear-gradient(135deg, {gradient}); color: white; text-decoration: none; border-radius: 25px; font-weight: bold; transition: all 0.3s ease; margin: 5px; }}
        .btn:hover {{ transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}
        .btn-secondary {{ background: linear-gradient(135deg, #6c757d, #5a6268); }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }}
        .stat-card {{ background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
        .stat-number {{ font-size: 2.5em; font-weight: bold; color: {primary_color}; }}
        .stat-label {{ color: #6c757d; margin-top: 5px; }}
        .back-buttons {{ text-align: center; padding: 30px; background: #f8f9fa; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{icon} {cert_name}</h1>
            <p>{description}</p>
        </div>
        
        <div class="section">
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{questions}</div>
                    <div class="stat-label">Questions</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{days}</div>
                    <div class="stat-label">Study Days</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{duration}</div>
                    <div class="stat-label">Exam Duration</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{level}</div>
                    <div class="stat-label">Level</div>
                </div>
            </div>
            
            <div class="apps-grid">
                {content}
            </div>
            
            <div class="back-buttons">
                <a href="../master_study_launcher.html" class="btn btn-secondary">🏠 Master Hub</a>
                <a href="../index.html" class="btn btn-secondary">🏡 Home Page</a>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    # DevOps Pro content
    devops_content = '''
                <div class="app-card">
                    <div class="app-title">📚 Daily Study</div>
                    <div class="app-desc">Study 18 questions per day over 20 days</div>
                    <a href="apps/study_app_day1_v2.html" class="btn">Day 1</a>
                    <a href="apps/study_app_day2_v2.html" class="btn">Day 2</a>
                    <a href="apps/study_app_day3_v2.html" class="btn">Day 3</a>
                    <br><button onclick="showAllDays('devops')" class="btn btn-secondary">Show All 20 Days</button>
                </div>
                
                <div class="app-card">
                    <div class="app-title">🎯 Practice Modes</div>
                    <div class="app-desc">Test your knowledge with different modes</div>
                    <a href="apps/exam_mode.html" class="btn">Practice Exam</a>
                    <a href="apps/review_app.html" class="btn">Review Mode</a>
                </div>'''
    
    # SAP-C02 content  
    sap_content = '''
                <div class="app-card">
                    <div class="app-title">📚 Daily Study</div>
                    <div class="app-desc">Study 18 questions per day over 30 days</div>
                    <a href="apps/study_app_day1_v2.html" class="btn">Day 1</a>
                    <a href="apps/study_app_day2_v2.html" class="btn">Day 2</a>
                    <a href="apps/study_app_day3_v2.html" class="btn">Day 3</a>
                    <br><button onclick="showAllDays('sap')" class="btn btn-secondary">Show All 30 Days</button>
                </div>
                
                <div class="app-card">
                    <div class="app-title">🎯 Practice Modes</div>
                    <div class="app-desc">Test your knowledge with different modes</div>
                    <a href="apps/exam_mode.html" class="btn">Practice Exam</a>
                    <a href="apps/review_app.html" class="btn">Review Mode</a>
                </div>'''
    
    # Network content
    network_content = '''
                <div class="app-card">
                    <div class="app-title">🌐 Network Study</div>
                    <div class="app-desc">Advanced networking concepts and scenarios</div>
                    <a href="apps/study_app_network_v2.html" class="btn">Start Studying</a>
                </div>'''
    
    # JavaScript for showing all days
    js_script = '''
    <script>
        function showAllDays(cert) {
            const maxDays = cert === 'sap' ? 30 : 20;
            let html = '<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 15px;">';
            for(let i = 1; i <= maxDays; i++) {
                html += `<a href="apps/study_app_day${i}_v2.html" class="btn">Day ${i}</a>`;
            }
            html += '</div>';
            event.target.parentElement.innerHTML = html;
        }
    </script>'''
    
    # Create DevOps launcher
    devops_html = base_template.format(
        title="DOP-C02 Study Hub",
        gradient="#28a745, #20c997",
        primary_color="#28a745",
        icon="⚙️",
        cert_name="AWS DevOps Professional",
        description="CI/CD, Infrastructure as Code, Monitoring & Automation",
        questions="360+",
        days="20",
        duration="180 min",
        level="Professional",
        content=devops_content
    ) + js_script
    
    # Create SAP launcher
    sap_html = base_template.format(
        title="SAP-C02 Study Hub", 
        gradient="#4caf50, #45a049",
        primary_color="#4caf50",
        icon="🏗️",
        cert_name="Solutions Architect Professional",
        description="Advanced AWS Architecture Design & Implementation",
        questions="529",
        days="30", 
        duration="180 min",
        level="Professional",
        content=sap_content
    ) + js_script
    
    # Create Network launcher
    network_html = base_template.format(
        title="Network Specialty Study Hub",
        gradient="#2196f3, #1976d2", 
        primary_color="#2196f3",
        icon="🌐",
        cert_name="AWS Network Specialty",
        description="Advanced Networking, VPC, Direct Connect & Security",
        questions="25",
        days="Flexible",
        duration="170 min", 
        level="Specialty",
        content=network_content
    )
    
    # Save files
    paths = [
        ("/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS DevOps Profestional/final_repo/master_launcher.html", devops_html),
        ("/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/final_repo/master_launcher.html", sap_html),
        ("/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Network Specity/final_repo/master_launcher.html", network_html)
    ]
    
    for path, content in paths:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print("✅ Created unified design for all 3 master launchers")

if __name__ == "__main__":
    create_unified_master_launchers()
