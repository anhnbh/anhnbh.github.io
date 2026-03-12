#!/usr/bin/env python3
import json
import sys
import re
from extract_questions_v4 import get_questions_for_range

# Mapping of days to question ranges
DAILY_SCHEDULE = {
    # Tuần 1 (126 câu)
    1: (1, 18),     # 18 câu
    2: (19, 36),    # 18 câu
    3: (37, 54),    # 18 câu
    4: (55, 72),    # 18 câu
    5: (73, 90),    # 18 câu
    6: (91, 108),   # 18 câu
    7: (109, 126),  # 18 câu
    
    # Tuần 2 (126 câu)
    8: (127, 144),  # 18 câu
    9: (145, 162),  # 18 câu
    10: (163, 180), # 18 câu
    11: (181, 198), # 18 câu
    12: (199, 216), # 18 câu
    13: (217, 234), # 18 câu
    14: (235, 252), # 18 câu
    
    # Tuần 3 (111 câu)
    15: (253, 268), # 16 câu
    16: (269, 284), # 16 câu
    17: (285, 300), # 16 câu
    18: (301, 316), # 16 câu
    19: (317, 332), # 16 câu
    20: (333, 363), # 31 câu (hoàn thành 363 câu)
}

def generate_app_for_day(day):
    """Generate study app for specific day with multiple choice support"""
    
    if day not in DAILY_SCHEDULE:
        print(f"❌ Day {day} not configured")
        return False
    
    start_q, end_q = DAILY_SCHEDULE[day]
    
    print(f"📅 Generating app for Day {day}")
    print(f"🎯 Questions: {start_q}-{end_q} ({end_q - start_q + 1} questions)")
    
    # Extract questions using the new method with multiple choice support
    questions = get_questions_for_range(start_q, end_q)
    
    if not questions:
        print("❌ No questions extracted")
        return False
    
    # Count question types
    single_count = len([q for q in questions if q['type'] == 'single'])
    multiple_count = len([q for q in questions if q['type'] == 'multiple'])
    
    print(f"📊 Question types: {single_count} single choice, {multiple_count} multiple choice")
    
    # Read the updated app template
    with open('study_app_v2.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace day number and question count
    content = content.replace('id="currentDay">1', f'id="currentDay">{day}')
    content = content.replace('Ngày <span id="currentDay">1</span>', f'Ngày <span id="currentDay">{day}</span>')
    content = content.replace('Câu <span id="currentQuestion">1</span>/18', f'Câu <span id="currentQuestion">1</span>/{len(questions)}')
    
    # Replace questions
    js_questions = json.dumps(questions, ensure_ascii=False, indent=12)
    pattern = r'const questions = \[.*?\];'
    replacement = f'const questions = {js_questions};'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Save day-specific app
    output_file = f'study_app_day{day}_v2.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Save questions backup
    with open(f'day{day}_questions_v2.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generated {output_file} with {len(questions)} questions")
    return True

def generate_all_days():
    """Generate apps for all 20 days with multiple choice support"""
    
    print("🚀 Generating study apps for all 20 days (with multiple choice support)...")
    print("=" * 60)
    
    success_count = 0
    failed_days = []
    total_single = 0
    total_multiple = 0
    
    for day in range(1, 21):
        print(f"\n📅 Day {day}:")
        try:
            if generate_app_for_day(day):
                success_count += 1
                
                # Count questions for this day
                start_q, end_q = DAILY_SCHEDULE[day]
                questions = get_questions_for_range(start_q, end_q)
                single_count = len([q for q in questions if q['type'] == 'single'])
                multiple_count = len([q for q in questions if q['type'] == 'multiple'])
                total_single += single_count
                total_multiple += multiple_count
                
            else:
                failed_days.append(day)
        except Exception as e:
            failed_days.append(day)
            print(f"❌ Day {day} error: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Summary:")
    print(f"✅ Successfully generated: {success_count}/20 days")
    print(f"📝 Total questions: {total_single + total_multiple}")
    print(f"   - Single choice: {total_single}")
    print(f"   - Multiple choice: {total_multiple}")
    
    if failed_days:
        print(f"❌ Failed days: {failed_days}")
    else:
        print("🎉 All 20 days generated successfully!")
    
    print(f"\n🎯 Ready to study! Use:")
    print(f"   open study_app_day1_v2.html          # Day 1 (with multiple choice support)")
    print(f"   open study_app_day2_v2.html          # Day 2")
    print(f"   ... and so on")
    
    return success_count == 20

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            day = int(sys.argv[1])
            if day == 0:
                # Generate all days
                generate_all_days()
            else:
                success = generate_app_for_day(day)
                if success:
                    print(f"🎯 Ready for Day {day}! Open 'study_app_day{day}_v2.html' in your browser")
        except ValueError:
            print("❌ Please provide a valid day number")
    else:
        print("Usage:")
        print("  python3 generate_daily_app_v3.py <day>     # Generate specific day")
        print("  python3 generate_daily_app_v3.py 0         # Generate all 20 days")
        print("Examples:")
        print("  python3 generate_daily_app_v3.py 1         # Generate day 1")
        print("  python3 generate_daily_app_v3.py 0         # Generate all days")
