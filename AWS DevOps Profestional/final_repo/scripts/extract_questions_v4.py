#!/usr/bin/env python3
import re
import json
from bs4 import BeautifulSoup

def extract_questions_from_html_by_position(html_file, start_pos=1, end_pos=18):
    """Extract questions by position in the HTML file with multiple choice support"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    questions = []
    
    # Find all question cards
    question_cards = soup.find_all('div', class_='card exam-question-card')
    
    print(f"📄 Found {len(question_cards)} questions in {html_file}")
    
    # Extract questions by position
    for pos in range(start_pos - 1, min(end_pos, len(question_cards))):
        card = question_cards[pos]
        
        try:
            # Extract question text
            question_body = card.find('div', class_='card-body')
            question_text_elem = question_body.find('p', class_='card-text')
            
            if not question_text_elem:
                continue
                
            question_text = question_text_elem.get_text(strip=True)
            # Clean up the text
            question_text = re.sub(r'\s+', ' ', question_text)
            
            # Detect question type
            is_multiple_choice = False
            required_choices = 1
            
            # Check for multiple choice indicators
            multiple_patterns = [
                r'\(Choose\s+(\w+)\.?\)',  # (Choose three.) or (Choose three)
                r'Choose\s+(\w+)\.?',      # Choose three. or Choose three
                r'Select\s+(\w+)\.?'       # Select three. or Select three
            ]
            
            for pattern in multiple_patterns:
                match = re.search(pattern, question_text, re.IGNORECASE)
                if match:
                    choice_word = match.group(1).lower()
                    
                    # Convert word to number
                    word_to_num = {
                        'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6
                    }
                    
                    if choice_word in word_to_num:
                        is_multiple_choice = True
                        required_choices = word_to_num[choice_word]
                        break
                    elif choice_word.isdigit():
                        is_multiple_choice = True
                        required_choices = int(choice_word)
                        break
            
            # Extract options
            options = []
            choice_items = card.find_all('li', class_='multi-choice-item')
            
            for choice in choice_items:
                choice_text = choice.get_text(strip=True)
                # Remove the letter prefix (A. B. C. D.)
                choice_text = re.sub(r'^[A-F]\.\s*', '', choice_text)
                # Remove badges like "Most Voted"
                choice_text = re.sub(r'Most Voted.*$', '', choice_text).strip()
                if choice_text:
                    options.append(choice_text)
            
            # Find correct answer(s)
            correct_answers = []
            
            # Try to get voting data for most popular answer
            script_elem = card.find('script', {'id': True})
            if script_elem:
                try:
                    vote_data = json.loads(script_elem.get_text())
                    most_voted = max(vote_data, key=lambda x: x['vote_count'])
                    voted_answer = most_voted['voted_answers']
                    
                    if is_multiple_choice and len(voted_answer) > 1:
                        # Multiple choice - parse each letter
                        for letter in voted_answer:
                            if letter in 'ABCDEF':
                                correct_answers.append(ord(letter) - ord('A'))
                    else:
                        # Single choice
                        if voted_answer in 'ABCDEF':
                            correct_answers = [ord(voted_answer) - ord('A')]
                            
                except Exception as e:
                    print(f"Error parsing vote data: {e}")
            
            # Fallback: look for correct-choice class
            if not correct_answers:
                correct_choice = card.find('li', class_='correct-choice')
                if correct_choice:
                    letter_elem = correct_choice.find('span', class_='multi-choice-letter')
                    if letter_elem:
                        letter = letter_elem.get_text(strip=True).replace('.', '')
                        if letter in 'ABCDEF':
                            correct_answers = [ord(letter) - ord('A')]
            
            # Default to A if no answer found
            if not correct_answers:
                correct_answers = [0]
            
            if len(options) >= 2:  # At least 2 options
                questions.append({
                    'id': start_pos + pos,  # Sequential ID
                    'text': question_text,
                    'options': options[:6],  # Max 6 options (A-F)
                    'correct': correct_answers,
                    'type': 'multiple' if is_multiple_choice else 'single',
                    'explanation': f'Đáp án được chọn nhiều nhất trong cộng đồng. Xem thêm giải thích trong file gốc.'
                })
                
        except Exception as e:
            print(f"Error processing question at position {pos + 1}: {e}")
            continue
    
    return questions

# Page mapping - how many questions each page has
PAGE_INFO = {
    1: 50,  # Page 1 has 50 questions
    2: 50,  # Page 2 has 50 questions  
    3: 50,  # Page 3 has 50 questions
    4: 50,  # Page 4 has 50 questions
    5: 50,  # Page 5 has 50 questions
    6: 50,  # Page 6 has 50 questions
    7: 50,  # Page 7 has 50 questions
    8: 13,  # Page 8 has 13 questions (total = 363)
}

def get_questions_for_range(start_q, end_q):
    """Get questions for a specific range across multiple pages"""
    
    questions = []
    current_q = 1
    
    for page in range(1, 9):  # Pages 1-8
        page_size = PAGE_INFO[page]
        page_start = current_q
        page_end = current_q + page_size - 1
        
        # Check if this page contains questions we need
        if start_q <= page_end and end_q >= page_start:
            # Calculate which questions to extract from this page
            extract_start = max(1, start_q - page_start + 1)
            extract_end = min(page_size, end_q - page_start + 1)
            
            html_file = f"AWS Certified DevOps Engineer - Professional DOP-C02 Exam - Free Exam Q&As, Page {page} _ ExamTopics.html"
            
            try:
                page_questions = extract_questions_from_html_by_position(html_file, extract_start, extract_end)
                
                # Adjust question IDs to match global numbering
                for q in page_questions:
                    q['id'] = page_start + (q['id'] - extract_start)
                
                questions.extend(page_questions)
                
                # Count question types
                single_count = len([q for q in page_questions if q['type'] == 'single'])
                multiple_count = len([q for q in page_questions if q['type'] == 'multiple'])
                
                print(f"✅ Extracted {len(page_questions)} questions from Page {page} ({single_count} single, {multiple_count} multiple)")
                
            except FileNotFoundError:
                print(f"❌ Page {page} file not found: {html_file}")
            except Exception as e:
                print(f"❌ Error extracting from Page {page}: {e}")
        
        current_q = page_end + 1
        
        if current_q > end_q:
            break
    
    return questions

if __name__ == "__main__":
    # Test with Day 1 (questions 1-18) to check multiple choice detection
    questions = get_questions_for_range(1, 18)
    print(f"📚 Total extracted: {len(questions)} questions")
    
    if questions:
        print(f"\n🔍 Question types breakdown:")
        single_count = len([q for q in questions if q['type'] == 'single'])
        multiple_count = len([q for q in questions if q['type'] == 'multiple'])
        print(f"   Single choice: {single_count}")
        print(f"   Multiple choice: {multiple_count}")
        
        # Show multiple choice questions
        for q in questions:
            if q['type'] == 'multiple':
                correct_letters = [chr(65 + i) for i in q['correct']]
                print(f"\n📝 Q{q['id']} (Multiple): {correct_letters}")
                print(f"   Text: {q['text'][:100]}...")
