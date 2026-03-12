#!/usr/bin/env python3
import os
import re
import json
from bs4 import BeautifulSoup

def extract_questions_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    questions = []
    
    # Find all question cards
    question_cards = soup.find_all('div', class_='card exam-question-card')
    
    for card in question_cards:
        try:
            # Extract question number
            header = card.find('div', class_='card-header')
            if not header:
                continue
                
            question_num_text = header.get_text(strip=True)
            question_match = re.search(r'Question #(\d+)', question_num_text)
            if not question_match:
                continue
            
            question_num = int(question_match.group(1))
            
            # Extract question body
            body = card.find('div', class_='card-body')
            if not body:
                continue
            
            # Get question text
            question_text_elem = body.find('p', class_='card-text')
            if not question_text_elem:
                continue
            
            question_text = question_text_elem.get_text(strip=True)
            if not question_text:
                continue
            
            # Extract choices
            choices_container = body.find('div', class_='question-choices-container')
            choices = []
            is_multiple_choice = False
            
            if choices_container:
                choice_items = choices_container.find_all('li', class_='multi-choice-item')
                for item in choice_items:
                    choice_text = item.get_text(strip=True)
                    if choice_text:
                        # Clean up choice text - remove letter prefix and badges
                        choice_text = re.sub(r'^[A-F]\.\s*', '', choice_text)
                        choice_text = re.sub(r'\s*Most Voted\s*$', '', choice_text)
                        if choice_text:
                            choices.append(choice_text)
                
                # Determine if multiple choice based on correct answer format
                answer_elem = body.find('span', class_='correct-answer')
                if answer_elem:
                    answer_text = answer_elem.get_text(strip=True)
                    is_multiple_choice = len(answer_text) > 1 and all(c.isalpha() for c in answer_text)
            
            # Extract correct answer
            answer_elem = body.find('span', class_='correct-answer')
            correct_answer = answer_elem.get_text(strip=True) if answer_elem else ""
            
            # Extract voting data
            voting_data = {}
            script_tag = body.find('script', {'type': 'application/json'})
            if script_tag and script_tag.string:
                try:
                    vote_data = json.loads(script_tag.string)
                    if isinstance(vote_data, list):
                        for vote in vote_data:
                            if 'voted_answers' in vote and 'vote_count' in vote:
                                voting_data[vote['voted_answers']] = vote['vote_count']
                except:
                    pass
            
            question_data = {
                'question_number': question_num,
                'question_text': question_text,
                'choices': choices,
                'correct_answer': correct_answer,
                'is_multiple_choice': is_multiple_choice,
                'voting_data': voting_data
            }
            
            questions.append(question_data)
            
        except Exception as e:
            print(f"Error processing question: {e}")
            continue
    
    return questions

def main():
    # Get all HTML files in the directory
    directory = "/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS Solution Architect Profestional"
    html_files = [f for f in os.listdir(directory) if f.startswith('SAPC02_') and f.endswith('.html')]
    html_files.sort()
    
    all_questions = []
    
    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        print(f"Processing {html_file}...")
        
        questions = extract_questions_from_html(file_path)
        all_questions.extend(questions)
        print(f"Extracted {len(questions)} questions from {html_file}")
    
    # Sort questions by number
    all_questions.sort(key=lambda x: x['question_number'])
    
    # Count multiple choice questions
    mc_count = sum(1 for q in all_questions if q['is_multiple_choice'])
    
    print(f"\nTotal questions extracted: {len(all_questions)}")
    print(f"Multiple choice questions: {mc_count} ({mc_count/len(all_questions)*100:.1f}%)")
    
    # Save to JSON
    output_file = os.path.join(directory, 'sap_c02_questions.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Questions saved to: {output_file}")

if __name__ == "__main__":
    main()
