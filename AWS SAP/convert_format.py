import json

# Đọc file gốc
with open('questions.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Chuyển đổi format
converted_data = []
for item in original_data:
    # Xử lý correct_answer
    correct_answer = item["correct_answer"].strip()
    
    # Xác định type và correct array
    if item["is_multiple_choice"]:
        # Multiple choice: correct_answer có thể là "ADF", "BCE", etc.
        correct_indices = [ord(char) - ord('A') for char in correct_answer]
        question_type = "multiple"
    else:
        # Single choice: correct_answer là "A", "B", "C", "D"
        correct_indices = [ord(correct_answer[0]) - ord('A')]
        question_type = "single"
    
    converted_item = {
        "id": item["question_number"],
        "text": item["question_text"],
        "options": item["choices"],
        "correct": correct_indices,
        "type": question_type,
        "explanation": "Đáp án được chọn nhiều nhất trong cộng đồng. Xem thêm giải thích trong file gốc."
    }
    converted_data.append(converted_item)

# Ghi file mới
with open('questions_converted.json', 'w', encoding='utf-8') as f:
    json.dump(converted_data, f, indent=2, ensure_ascii=False)

print(f"Đã chuyển đổi {len(converted_data)} câu hỏi thành công!")
print(f"Trong đó có {sum(1 for item in converted_data if item['type'] == 'single')} câu single choice")
print(f"và {sum(1 for item in converted_data if item['type'] == 'multiple')} câu multiple choice")
