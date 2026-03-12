#!/bin/bash

echo "🎓 AWS DevOps Professional - Practice Exam"
echo "=========================================="

# Check if exam app exists
if [ ! -f "apps/exam_mode.html" ]; then
    echo "❌ Exam app not found!"
    echo "💡 Creating exam mode..."
    python3 create_exam_mode.py
fi

echo ""
echo "📋 EXAM INSTRUCTIONS:"
echo "   • 75 questions (random from 360 question pool)"
echo "   • 180 minutes (3 hours) time limit"
echo "   • Passing score: 750/1000 points (75%)"
echo "   • Mix of single and multiple response questions"
echo "   • You can flag questions for review"
echo "   • Exam auto-submits when time expires"
echo ""

read -p "⚠️  Ready to start your practice exam? (y/N): " confirm

if [[ $confirm =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Starting AWS DevOps Professional Practice Exam..."
    echo "📱 Opening exam interface..."
    echo ""
    echo "💡 EXAM TIPS:"
    echo "   - Read each question carefully (1.5-2 min per question)"
    echo "   - For multiple response: select ALL correct answers"
    echo "   - Use flag feature for questions you want to review"
    echo "   - Manage your time: 180 minutes for 75 questions"
    echo "   - Don't refresh the page - progress will be lost!"
    echo ""
    echo "🍀 Good luck! You've got this!"
    
    # Get the full path
    FULL_PATH="$(pwd)/apps/exam_mode.html"
    
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
    
else
    echo "📚 No problem! Come back when you're ready."
    echo ""
    echo "💡 Preparation tips:"
    echo "   - Review your weak areas first"
    echo "   - Practice with review mode: ./review.sh"
    echo "   - Study the 5-day review plan: docs/5_day_review_plan.md"
    echo "   - Get a good night's sleep before the exam"
fi
