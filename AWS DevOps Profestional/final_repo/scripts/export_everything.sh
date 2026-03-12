#!/bin/bash

echo "🚀 AWS DevOps Professional - Export Everything"
echo "=============================================="

# Create export directory
EXPORT_DIR="AWS_DevOps_Export_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$EXPORT_DIR"

echo "📁 Created export directory: $EXPORT_DIR"

# Run export scripts
echo ""
echo "📊 Exporting all questions..."
python3 export_all_questions.py

echo ""
echo "🃏 Creating flashcards and practice tests..."
python3 create_flashcards.py

# Move all exported files to export directory
echo ""
echo "📦 Moving files to export directory..."

# Main exports
mv AWS_DevOps_All_Questions.* "$EXPORT_DIR/" 2>/dev/null
mv AWS_DevOps_Questions_Only.md "$EXPORT_DIR/" 2>/dev/null
mv AWS_DevOps_Answers_Only.md "$EXPORT_DIR/" 2>/dev/null
mv AWS_DevOps_Day_Summary.md "$EXPORT_DIR/" 2>/dev/null

# Flashcards and practice tests
mv AWS_DevOps_Anki_Flashcards.txt "$EXPORT_DIR/" 2>/dev/null
mv AWS_DevOps_Quizlet.txt "$EXPORT_DIR/" 2>/dev/null
mv AWS_DevOps_Practice_*.md "$EXPORT_DIR/" 2>/dev/null

# Copy study apps
echo "📱 Copying study apps..."
cp study_app_day*_v2.html "$EXPORT_DIR/" 2>/dev/null
cp start_study_v2.sh "$EXPORT_DIR/" 2>/dev/null

# Copy question data
echo "💾 Copying question data..."
mkdir -p "$EXPORT_DIR/data"
cp day*_questions_v2.json "$EXPORT_DIR/data/" 2>/dev/null

# Create README for export
cat > "$EXPORT_DIR/README.md" << 'EOF'
# AWS DevOps Professional (DOP-C02) - Complete Export

## 📊 Nội Dung

### 📄 Tài Liệu Học Tập
- `AWS_DevOps_All_Questions.md` - Tất cả câu hỏi với đáp án
- `AWS_DevOps_Questions_Only.md` - Chỉ câu hỏi (để làm bài)
- `AWS_DevOps_Answers_Only.md` - Chỉ đáp án (để chấm)
- `AWS_DevOps_Day_Summary.md` - Tóm tắt theo ngày

### 📊 Dữ Liệu
- `AWS_DevOps_All_Questions.json` - Dữ liệu JSON đầy đủ
- `AWS_DevOps_All_Questions.csv` - Dữ liệu CSV (Excel)

### 🃏 Flashcards
- `AWS_DevOps_Anki_Flashcards.txt` - Import vào Anki
- `AWS_DevOps_Quizlet.txt` - Import vào Quizlet

### 📝 Practice Tests
- `AWS_DevOps_Practice_Week1.md` - Test tuần 1 (126 câu)
- `AWS_DevOps_Practice_Week2.md` - Test tuần 2 (126 câu)
- `AWS_DevOps_Practice_Week3.md` - Test tuần 3 (108 câu)
- `AWS_DevOps_Practice_MultipleChoice.md` - Chỉ multiple choice (103 câu)
- `AWS_DevOps_Practice_SingleChoice.md` - Chỉ single choice (257 câu)

### 📱 Study Apps
- `study_app_day1_v2.html` đến `study_app_day20_v2.html` - Apps học tập
- `start_study_v2.sh` - Script khởi động

### 💾 Raw Data
- `data/` - Thư mục chứa JSON files cho từng ngày

## 🚀 Cách Sử Dụng

### Học Online
```bash
# Mở app học tập
open study_app_day1_v2.html
```

### Học Offline
1. In file `AWS_DevOps_Questions_Only.md`
2. Làm bài trên giấy
3. Đối chiếu với `AWS_DevOps_Answers_Only.md`

### Flashcards
1. Import `AWS_DevOps_Anki_Flashcards.txt` vào Anki
2. Hoặc import `AWS_DevOps_Quizlet.txt` vào Quizlet

### Practice Tests
1. Mở file practice test tương ứng
2. Làm bài theo thời gian
3. Kiểm tra đáp án ở cuối file

## 📊 Thống Kê
- **Tổng câu hỏi**: 360
- **Single Choice**: 257 câu
- **Multiple Choice**: 103 câu
- **Tỷ lệ Multiple Choice**: 28.6%

Good luck with your AWS DevOps Professional exam! 🍀
EOF

# Create file list
echo ""
echo "📋 Creating file list..."
ls -la "$EXPORT_DIR" > "$EXPORT_DIR/file_list.txt"

# Show summary
echo ""
echo "🎉 Export completed!"
echo "📁 All files exported to: $EXPORT_DIR"
echo ""
echo "📊 Summary:"
echo "   📄 $(ls "$EXPORT_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ') Markdown files"
echo "   📊 $(ls "$EXPORT_DIR"/*.json "$EXPORT_DIR"/*.csv 2>/dev/null | wc -l | tr -d ' ') Data files"
echo "   🃏 $(ls "$EXPORT_DIR"/*.txt 2>/dev/null | wc -l | tr -d ' ') Flashcard files"
echo "   📱 $(ls "$EXPORT_DIR"/*.html 2>/dev/null | wc -l | tr -d ' ') Study apps"
echo "   💾 $(ls "$EXPORT_DIR"/data/*.json 2>/dev/null | wc -l | tr -d ' ') Raw data files"
echo ""
echo "🎯 Ready to study anywhere, anytime!"

# Open export directory
if command -v open >/dev/null 2>&1; then
    open "$EXPORT_DIR"
fi
