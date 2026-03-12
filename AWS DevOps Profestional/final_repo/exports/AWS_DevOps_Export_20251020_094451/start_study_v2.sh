#!/bin/bash

echo "🚀 AWS DevOps Professional Study App v2.0"
echo "=========================================="
echo "✨ NEW: Multiple Choice Support!"

# Check if the v2 app file exists
if [ -f "study_app_day1_v2.html" ]; then
    echo "✅ Found study app v2 with multiple choice support"
    APP_FILE="study_app_day1_v2.html"
elif [ -f "study_app_with_real_questions.html" ]; then
    echo "⚠️  Using study app v1 (single choice only)"
    APP_FILE="study_app_with_real_questions.html"
else
    echo "⚠️  Using study app with sample questions"
    APP_FILE="study_app.html"
fi

# Get the full path
FULL_PATH="$(pwd)/$APP_FILE"

echo "📂 Opening: $APP_FILE"
echo "🎯 Mục tiêu hôm nay: Hoàn thành câu 1-18 (Ngày 1)"
echo ""

# Open in default browser
if command -v open >/dev/null 2>&1; then
    # macOS
    open "$FULL_PATH"
elif command -v xdg-open >/dev/null 2>&1; then
    # Linux
    xdg-open "$FULL_PATH"
elif command -v start >/dev/null 2>&1; then
    # Windows
    start "$FULL_PATH"
else
    echo "❌ Cannot open browser automatically"
    echo "📋 Please open this file manually:"
    echo "   $FULL_PATH"
fi

echo ""
echo "🆕 NEW FEATURES:"
echo "   ✅ Multiple Choice Questions (Choose 2, 3, etc.)"
echo "   ✅ Partial Credit Scoring"
echo "   ✅ Enhanced Question Type Detection"
echo "   ✅ Improved Answer Validation"
echo ""
echo "💡 Tips:"
echo "   - Single Choice: Click to select one answer"
echo "   - Multiple Choice: Click multiple answers (checkboxes)"
echo "   - Read carefully: 'Choose three' means select 3 options"
echo "   - Partial credit given for partially correct answers"
echo ""
echo "⏰ Thời gian mục tiêu: 1.5 giờ (18 câu)"
echo "🎯 Không xem đáp án cho đến khi hoàn thành!"
echo ""
echo "Good luck! 🍀"
