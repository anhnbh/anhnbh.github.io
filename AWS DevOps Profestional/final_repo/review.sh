#!/bin/bash

echo "🔥 AWS DevOps Review Mode - 5 Ngày Ôn Tập Cuối"
echo "============================================="

# Get review day from parameter or show menu
REVIEW_DAY=${1}

if [ -z "$REVIEW_DAY" ]; then
    echo ""
    echo "📅 Chọn ngày ôn tập (hoặc chế độ):"
    echo "   1) Ngày 1: Mixed Review (50 câu hỗn hợp)"
    echo "   2) Ngày 2: Multiple Choice Focus (30 câu khó)"
    echo "   3) Ngày 3: Hard Questions (25 câu siêu khó)"
    echo "   4) Ngày 4: Random Marathon (100 câu)"
    echo "   5) Ngày 5: Final Sprint (Custom)"
    echo ""
    echo "   m) Mixed Mode"
    echo "   h) Hard Mode"
    echo "   r) Random Mode"
    echo ""
    read -p "Chọn (1-5, m, h, r): " choice
    
    case $choice in
        1|m) MODE="mixed" ;;
        2) MODE="multiple" ;;
        3|h) MODE="hard" ;;
        4|r) MODE="random" ;;
        5) MODE="mixed" ;;
        *) echo "❌ Invalid choice"; exit 1 ;;
    esac
else
    case $REVIEW_DAY in
        1) MODE="mixed" ;;
        2) MODE="multiple" ;;
        3) MODE="hard" ;;
        4) MODE="random" ;;
        5) MODE="mixed" ;;
        *) echo "❌ Invalid day: $REVIEW_DAY (1-5)"; exit 1 ;;
    esac
fi

# Check if review app exists
if [ ! -f "apps/review_app.html" ]; then
    echo "❌ Review app not found!"
    echo "💡 Creating review app..."
    python3 create_review_app.py
fi

echo ""
echo "🔥 Starting Review Mode: $MODE"
echo "📱 Opening review app..."

# Get the full path
FULL_PATH="$(pwd)/apps/review_app.html"

# Open in default browser
if command -v open >/dev/null 2>&1; then
    open "$FULL_PATH"
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$FULL_PATH"
elif command -v start >/dev/null 2>&1; then
    start "$FULL_PATH"
else
    echo "❌ Cannot open browser automatically"
    echo "📋 Please open: $FULL_PATH"
fi

echo ""
echo "🎯 Kế hoạch 5 ngày ôn tập:"
echo "   Ngày 1: Mixed (50 câu) - Làm quen lại"
echo "   Ngày 2: Multiple Choice (30 câu) - Focus câu khó"
echo "   Ngày 3: Hard Mode (25 câu) - Thử thách bản thân"
echo "   Ngày 4: Random (100 câu) - Marathon"
echo "   Ngày 5: Custom - Ôn câu sai + Final prep"
echo ""
echo "💡 Tips ôn tập:"
echo "   - Focus vào câu multiple choice (28% đề thi)"
echo "   - Ôn lại câu sai nhiều lần"
echo "   - Tập tốc độ: 1.5 phút/câu"
echo "   - Đọc kỹ keywords: MOST, LEAST, cost-effective"
echo ""
echo "🔥 Good luck with your final review!"
