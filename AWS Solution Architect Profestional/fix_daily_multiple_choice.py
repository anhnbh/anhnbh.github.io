#!/usr/bin/env python3
import os
import re

def fix_multiple_choice_in_file(file_path):
    """Fix multiple choice selection in daily study files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix selectChoice function
    old_function = r'''function selectChoice\(letter, element\) \{[^}]+\}'''
    
    new_function = '''function selectChoice(letter, element) {
            const question = questions[currentQuestionIndex];
            const isMultipleChoice = question.is_multiple_choice;
            const questionId = question.question_number;
            
            if (!selectedAnswers[questionId]) {
                selectedAnswers[questionId] = [];
            }
            
            if (!isMultipleChoice) {
                // Single choice - clear other selections
                document.querySelectorAll('.choice').forEach(choice => {
                    choice.classList.remove('selected');
                });
                selectedAnswers[questionId] = [letter];
                element.classList.add('selected');
            } else {
                // Multiple choice - toggle selection
                element.classList.toggle('selected');
                
                if (element.classList.contains('selected')) {
                    if (!selectedAnswers[questionId].includes(letter)) {
                        selectedAnswers[questionId].push(letter);
                    }
                } else {
                    selectedAnswers[questionId] = selectedAnswers[questionId].filter(a => a !== letter);
                }
            }
        }'''
    
    content = re.sub(old_function, new_function, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Fix daily study files
    daily_dir = "/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/final_repo/daily_study"
    for i in range(1, 31):
        file_path = os.path.join(daily_dir, f"day_{i:02d}.html")
        if os.path.exists(file_path):
            fix_multiple_choice_in_file(file_path)
    
    # Fix review day files
    review_dir = "/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional/final_repo/review_days"
    for i in range(1, 8):
        file_path = os.path.join(review_dir, f"review_day_{i}.html")
        if os.path.exists(file_path):
            fix_multiple_choice_in_file(file_path)
    
    print("✅ Fixed multiple choice support in all daily/review files")

if __name__ == "__main__":
    main()
