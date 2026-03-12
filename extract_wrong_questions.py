import json

# Đọc file kết quả
with open('/Users/hungtn/Desktop/aws-certificates/AWS Dump/aws-devops-results-2025-11-16.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# Đọc file đề bài
with open('/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS DevOps Profestional/final_repo/apps/data.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Lấy danh sách ID câu hỏi làm sai
wrong_ids = {wrong['id'] for wrong in results['wrongQuestions']}

# Lọc câu hỏi làm sai
wrong_questions = [q for q in questions if q['id'] in wrong_ids]

# Lưu file
with open('/Users/hungtn/Desktop/aws-certificates/AWS Dump/wrong-questions-2025-11-16.json', 'w', encoding='utf-8') as f:
    json.dump(wrong_questions, f, indent=4, ensure_ascii=False)

print(f"Đã tạo file wrong-questions-2025-11-16.json với {len(wrong_questions)} câu hỏi làm sai")
