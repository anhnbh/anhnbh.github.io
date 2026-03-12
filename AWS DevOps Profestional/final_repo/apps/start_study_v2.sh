#!/bin/bash

echo "🚀 AWS DevOps Professional Study App v2.0"
echo "=========================================="
echo "✨ NEW: Multiple Choice Support!"

# Get day from parameter or default to 1
DAY=${1:-1}

# Validate day range
if [[ $DAY -lt 1 || $DAY -gt 20 ]]; then
    echo "❌ Invalid day: $DAY (must be 1-20)"
    echo ""
    echo "💡 Usage: ./start_study_v2.sh [day]"
    echo "   Examples:"
    echo "   ./start_study_v2.sh     # Day 1 (default)"
    echo "   ./start_study_v2.sh 5   # Day 5"
    echo "   ./start_study_v2.sh 15  # Day 15"
    exit 1
fi

# Check if the app file exists
APP_FILE="study_app_day${DAY}_v2.html"
if [ -f "$APP_FILE" ]; then
    echo "✅ Found study app for Day $DAY"
else
    echo "❌ App file not found: $APP_FILE"
    echo ""
    echo "💡 Available days:"
    ls study_app_day*_v2.html 2>/dev/null | sed 's/study_app_day\([0-9]*\)_v2.html/   Day \1/' | sort -V
    exit 1
fi

# Get the full path
FULL_PATH="$(pwd)/$APP_FILE"

# Get question range for this day
case $DAY in
    1) RANGE="1-18 (18 câu)" ;;
    2) RANGE="19-36 (18 câu)" ;;
    3) RANGE="37-54 (18 câu)" ;;
    4) RANGE="55-72 (18 câu)" ;;
    5) RANGE="73-90 (18 câu)" ;;
    6) RANGE="91-108 (18 câu)" ;;
    7) RANGE="109-126 (18 câu)" ;;
    8) RANGE="127-144 (18 câu)" ;;
    9) RANGE="145-162 (18 câu)" ;;
    10) RANGE="163-180 (18 câu)" ;;
    11) RANGE="181-198 (18 câu)" ;;
    12) RANGE="199-216 (18 câu)" ;;
    13) RANGE="217-234 (18 câu)" ;;
    14) RANGE="235-252 (18 câu)" ;;
    15) RANGE="253-268 (16 câu)" ;;
    16) RANGE="269-284 (16 câu)" ;;
    17) RANGE="285-300 (16 câu)" ;;
    18) RANGE="301-316 (16 câu)" ;;
    19) RANGE="317-332 (16 câu)" ;;
    20) RANGE="333-363 (31 câu)" ;;
esac

echo "📂 Opening: $APP_FILE"
echo "🎯 Mục tiêu Day $DAY: Hoàn thành câu $RANGE"
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
echo "⏰ Thời gian mục tiêu: 1.5 giờ"
echo "🎯 Không xem đáp án cho đến khi hoàn thành!"
echo ""
echo "Good luck! 🍀"
