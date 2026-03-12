import json

with open('questions_converted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Đảo ngược thứ tự và cập nhật id
for i, item in enumerate(reversed(data)):
    item['id'] = i + 1

with open('questions_converted.json', 'w', encoding='utf-8') as f:
    json.dump(list(reversed(data)), f, indent=2, ensure_ascii=False)

print(f"Đã đảo ngược thứ tự {len(data)} câu hỏi!")
