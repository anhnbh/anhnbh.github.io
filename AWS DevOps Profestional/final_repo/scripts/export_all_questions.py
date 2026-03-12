#!/usr/bin/env python3
import json
import os
from datetime import datetime

def load_all_questions():
    """Load all questions from day files"""
    all_questions = []
    
    for day in range(1, 21):
        json_file = f'day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                all_questions.extend(questions)
                print(f"✅ Loaded {len(questions)} questions from Day {day}")
        else:
            print(f"❌ Missing: {json_file}")
    
    return all_questions

def export_to_markdown(questions):
    """Export all questions to markdown format"""
    
    content = f"""# AWS DevOps Professional (DOP-C02) - Tất Cả Câu Hỏi

**Tổng số câu**: {len(questions)}  
**Ngày xuất**: {datetime.now().strftime('%d/%m/%Y %H:%M')}  
**Single Choice**: {len([q for q in questions if q['type'] == 'single'])}  
**Multiple Choice**: {len([q for q in questions if q['type'] == 'multiple'])}

---

"""
    
    for i, q in enumerate(questions, 1):
        content += f"## Câu {q['id']}\n\n"
        
        # Question type
        if q['type'] == 'multiple':
            correct_count = len(q['correct'])
            content += f"**Loại**: Multiple Choice (Chọn {correct_count} đáp án)\n\n"
        else:
            content += f"**Loại**: Single Choice\n\n"
        
        # Question text
        content += f"**Câu hỏi**: {q['text']}\n\n"
        
        # Options
        content += "**Các lựa chọn**:\n\n"
        for j, option in enumerate(q['options']):
            letter = chr(65 + j)
            is_correct = j in q['correct']
            marker = "✅" if is_correct else "❌"
            content += f"{letter}. {option} {marker}\n\n"
        
        # Correct answer
        correct_letters = [chr(65 + i) for i in q['correct']]
        content += f"**Đáp án đúng**: {', '.join(correct_letters)}\n\n"
        content += f"**Giải thích**: {q['explanation']}\n\n"
        content += "---\n\n"
    
    with open('AWS_DevOps_All_Questions.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Exported to AWS_DevOps_All_Questions.md")

def export_to_json(questions):
    """Export all questions to comprehensive JSON"""
    
    export_data = {
        "metadata": {
            "exam": "AWS Certified DevOps Engineer Professional (DOP-C02)",
            "total_questions": len(questions),
            "single_choice": len([q for q in questions if q['type'] == 'single']),
            "multiple_choice": len([q for q in questions if q['type'] == 'multiple']),
            "export_date": datetime.now().isoformat(),
            "version": "2.0"
        },
        "questions": questions
    }
    
    with open('AWS_DevOps_All_Questions.json', 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Exported to AWS_DevOps_All_Questions.json")

def export_to_csv(questions):
    """Export all questions to CSV format"""
    
    import csv
    
    with open('AWS_DevOps_All_Questions.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Question_ID', 'Type', 'Question_Text', 'Option_A', 'Option_B', 
            'Option_C', 'Option_D', 'Option_E', 'Option_F', 'Correct_Answers', 
            'Correct_Letters', 'Explanation'
        ])
        
        # Data
        for q in questions:
            options = q['options'] + [''] * (6 - len(q['options']))  # Pad to 6 options
            correct_letters = [chr(65 + i) for i in q['correct']]
            
            writer.writerow([
                q['id'],
                q['type'],
                q['text'],
                options[0], options[1], options[2], options[3], options[4], options[5],
                ','.join(map(str, q['correct'])),
                ','.join(correct_letters),
                q['explanation']
            ])
    
    print(f"✅ Exported to AWS_DevOps_All_Questions.csv")

def export_study_guide(questions):
    """Export study guide with answers separated"""
    
    # Questions only
    questions_content = f"""# AWS DevOps Professional - Câu Hỏi (Không Đáp Án)

**Tổng số câu**: {len(questions)}  
**Ngày xuất**: {datetime.now().strftime('%d/%m/%Y %H:%M')}

**Hướng dẫn**: In file này để làm bài, sau đó đối chiếu với file đáp án.

---

"""
    
    # Answers only
    answers_content = f"""# AWS DevOps Professional - Đáp Án

**Tổng số câu**: {len(questions)}  
**Ngày xuất**: {datetime.now().strftime('%d/%m/%Y %H:%M')}

---

"""
    
    for q in questions:
        # Questions file
        questions_content += f"## Câu {q['id']}\n\n"
        if q['type'] == 'multiple':
            correct_count = len(q['correct'])
            questions_content += f"**Loại**: Multiple Choice (Chọn {correct_count} đáp án)\n\n"
        else:
            questions_content += f"**Loại**: Single Choice\n\n"
        
        questions_content += f"{q['text']}\n\n"
        
        for j, option in enumerate(q['options']):
            letter = chr(65 + j)
            questions_content += f"{letter}. {option}\n\n"
        
        questions_content += f"**Đáp án của bạn**: ___________\n\n"
        questions_content += "---\n\n"
        
        # Answers file
        correct_letters = [chr(65 + i) for i in q['correct']]
        answers_content += f"**Câu {q['id']}**: {', '.join(correct_letters)}\n\n"
    
    # Save files
    with open('AWS_DevOps_Questions_Only.md', 'w', encoding='utf-8') as f:
        f.write(questions_content)
    
    with open('AWS_DevOps_Answers_Only.md', 'w', encoding='utf-8') as f:
        f.write(answers_content)
    
    print(f"✅ Exported to AWS_DevOps_Questions_Only.md")
    print(f"✅ Exported to AWS_DevOps_Answers_Only.md")

def export_by_day_summary():
    """Export summary by day"""
    
    summary_content = f"""# AWS DevOps Professional - Tóm Tắt Theo Ngày

**Ngày xuất**: {datetime.now().strftime('%d/%m/%Y %H:%M')}

---

"""
    
    total_questions = 0
    total_single = 0
    total_multiple = 0
    
    for day in range(1, 21):
        json_file = f'day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                
            single_count = len([q for q in questions if q['type'] == 'single'])
            multiple_count = len([q for q in questions if q['type'] == 'multiple'])
            
            total_questions += len(questions)
            total_single += single_count
            total_multiple += multiple_count
            
            # Get question range
            if questions:
                start_q = min(q['id'] for q in questions)
                end_q = max(q['id'] for q in questions)
                
                summary_content += f"## Ngày {day}\n\n"
                summary_content += f"- **Câu hỏi**: {start_q}-{end_q} ({len(questions)} câu)\n"
                summary_content += f"- **Single Choice**: {single_count}\n"
                summary_content += f"- **Multiple Choice**: {multiple_count}\n"
                summary_content += f"- **File**: `study_app_day{day}_v2.html`\n\n"
    
    summary_content += f"""
---

## Tổng Kết

- **Tổng câu hỏi**: {total_questions}
- **Single Choice**: {total_single}
- **Multiple Choice**: {total_multiple}
- **Tỷ lệ Multiple Choice**: {round(total_multiple/total_questions*100, 1)}%

"""
    
    with open('AWS_DevOps_Day_Summary.md', 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print(f"✅ Exported to AWS_DevOps_Day_Summary.md")

def main():
    print("🚀 Exporting all AWS DevOps questions...")
    print("=" * 50)
    
    # Load all questions
    questions = load_all_questions()
    
    if not questions:
        print("❌ No questions found!")
        return
    
    print(f"\n📊 Total loaded: {len(questions)} questions")
    print(f"   - Single Choice: {len([q for q in questions if q['type'] == 'single'])}")
    print(f"   - Multiple Choice: {len([q for q in questions if q['type'] == 'multiple'])}")
    
    print(f"\n📁 Exporting to multiple formats...")
    
    # Export to different formats
    export_to_markdown(questions)
    export_to_json(questions)
    export_to_csv(questions)
    export_study_guide(questions)
    export_by_day_summary()
    
    print(f"\n🎉 Export completed! Files created:")
    print(f"   📄 AWS_DevOps_All_Questions.md - Tất cả câu hỏi với đáp án")
    print(f"   📄 AWS_DevOps_Questions_Only.md - Chỉ câu hỏi (để làm bài)")
    print(f"   📄 AWS_DevOps_Answers_Only.md - Chỉ đáp án (để chấm)")
    print(f"   📄 AWS_DevOps_Day_Summary.md - Tóm tắt theo ngày")
    print(f"   📊 AWS_DevOps_All_Questions.json - Dữ liệu JSON")
    print(f"   📊 AWS_DevOps_All_Questions.csv - Dữ liệu CSV")

if __name__ == "__main__":
    main()
