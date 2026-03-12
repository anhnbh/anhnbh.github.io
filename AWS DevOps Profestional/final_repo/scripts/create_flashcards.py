#!/usr/bin/env python3
import json
import os
from datetime import datetime

def create_anki_flashcards():
    """Create Anki-compatible flashcards"""
    
    # Load all questions
    all_questions = []
    for day in range(1, 21):
        json_file = f'day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                all_questions.extend(questions)
    
    # Create Anki CSV format
    anki_content = ""
    
    for q in all_questions:
        # Front of card (question)
        front = f"<b>Câu {q['id']} ({q['type'].title()} Choice)</b><br><br>"
        front += q['text'].replace('\n', '<br>')
        front += "<br><br>"
        
        for j, option in enumerate(q['options']):
            letter = chr(65 + j)
            front += f"{letter}. {option}<br>"
        
        # Back of card (answer + explanation)
        correct_letters = [chr(65 + i) for i in q['correct']]
        back = f"<b>Đáp án: {', '.join(correct_letters)}</b><br><br>"
        back += f"<i>{q['explanation']}</i>"
        
        # Add to Anki format (tab-separated)
        anki_content += f'"{front}"\t"{back}"\n'
    
    with open('AWS_DevOps_Anki_Flashcards.txt', 'w', encoding='utf-8') as f:
        f.write(anki_content)
    
    print(f"✅ Created AWS_DevOps_Anki_Flashcards.txt ({len(all_questions)} cards)")

def create_quizlet_format():
    """Create Quizlet-compatible format"""
    
    # Load all questions
    all_questions = []
    for day in range(1, 21):
        json_file = f'day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                all_questions.extend(questions)
    
    quizlet_content = ""
    
    for q in all_questions:
        # Term (question)
        term = f"Q{q['id']}: {q['text'][:100]}..."
        
        # Definition (answer)
        correct_letters = [chr(65 + i) for i in q['correct']]
        definition = f"Answer: {', '.join(correct_letters)}"
        
        quizlet_content += f"{term}\t{definition}\n"
    
    with open('AWS_DevOps_Quizlet.txt', 'w', encoding='utf-8') as f:
        f.write(quizlet_content)
    
    print(f"✅ Created AWS_DevOps_Quizlet.txt ({len(all_questions)} terms)")

def create_practice_tests():
    """Create practice test files by topic"""
    
    # Load all questions
    all_questions = []
    for day in range(1, 21):
        json_file = f'day{day}_questions_v2.json'
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                all_questions.extend(questions)
    
    # Create practice tests
    tests = {
        "Week1": all_questions[:126],
        "Week2": all_questions[126:252],
        "Week3": all_questions[252:],
        "MultipleChoice": [q for q in all_questions if q['type'] == 'multiple'],
        "SingleChoice": [q for q in all_questions if q['type'] == 'single']
    }
    
    for test_name, questions in tests.items():
        content = f"""# AWS DevOps Practice Test - {test_name}

**Số câu**: {len(questions)}  
**Ngày tạo**: {datetime.now().strftime('%d/%m/%Y %H:%M')}

---

"""
        
        for i, q in enumerate(questions, 1):
            content += f"## Câu {i}\n\n"
            content += f"**ID**: {q['id']} | **Loại**: {q['type'].title()} Choice\n\n"
            content += f"{q['text']}\n\n"
            
            for j, option in enumerate(q['options']):
                letter = chr(65 + j)
                content += f"{letter}. {option}\n\n"
            
            content += "**Đáp án**: ___________\n\n"
            content += "---\n\n"
        
        # Answer key
        content += "\n# Đáp Án\n\n"
        for i, q in enumerate(questions, 1):
            correct_letters = [chr(65 + j) for j in q['correct']]
            content += f"**Câu {i}** (ID {q['id']}): {', '.join(correct_letters)}\n\n"
        
        with open(f'AWS_DevOps_Practice_{test_name}.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Created AWS_DevOps_Practice_{test_name}.md ({len(questions)} questions)")

if __name__ == "__main__":
    print("🃏 Creating flashcards and practice tests...")
    print("=" * 50)
    
    create_anki_flashcards()
    create_quizlet_format()
    create_practice_tests()
    
    print(f"\n🎉 Flashcards and practice tests created!")
    print(f"   🃏 AWS_DevOps_Anki_Flashcards.txt - Import vào Anki")
    print(f"   🃏 AWS_DevOps_Quizlet.txt - Import vào Quizlet")
    print(f"   📝 AWS_DevOps_Practice_Week1.md - Test tuần 1")
    print(f"   📝 AWS_DevOps_Practice_Week2.md - Test tuần 2")
    print(f"   📝 AWS_DevOps_Practice_Week3.md - Test tuần 3")
    print(f"   📝 AWS_DevOps_Practice_MultipleChoice.md - Chỉ multiple choice")
    print(f"   📝 AWS_DevOps_Practice_SingleChoice.md - Chỉ single choice")
