#!/bin/bash

echo "🚀 Setting up SAP-C02 Complete Study System..."
echo "================================================"

# Extract questions if not already done
if [ ! -f "sap_c02_questions.json" ]; then
    echo "📚 Extracting questions from HTML files..."
    python3 extract_sap_questions.py
else
    echo "✅ Questions already extracted"
fi

# Create daily study plan
echo "📅 Creating 30-day study plan + 7-day review..."
python3 create_sap_daily_plan.py

# Create complete system (exam mode, review modes, exports)
echo "🎯 Creating exam mode and review modes..."
python3 create_sap_complete_system.py

# Create main study app if not exists
if [ ! -f "sap_c02_study_app.html" ]; then
    echo "📱 Creating main study app..."
    python3 create_sap_study_app.py
fi

echo ""
echo "✅ SAP-C02 Study System Setup Complete!"
echo "========================================"
echo ""
echo "📂 Files created:"
echo "   📚 Main Apps:"
echo "   - sap_master_launcher.html (Start here!)"
echo "   - sap_c02_study_app.html (Complete study app)"
echo "   - sap_exam_mode.html (Practice exam: 75Q, 180min)"
echo ""
echo "   📅 Daily Study (30 days):"
echo "   - day_01_study.html → day_30_study.html"
echo ""
echo "   🔄 Review (7 days):"
echo "   - review_day_1_study.html → review_day_7_study.html"
echo ""
echo "   📝 Review Modes:"
echo "   - sap_review_mixed.html (Mixed questions)"
echo "   - sap_review_multiple_choice.html (MC only)"
echo "   - sap_review_hard.html (Difficult questions)"
echo "   - sap_review_random.html (Random selection)"
echo ""
echo "   📤 Export Formats:"
echo "   - sap_c02_questions.json (JSON data)"
echo "   - sap_c02_questions.md (Markdown)"
echo "   - sap_c02_questions.csv (CSV)"
echo ""
echo "🎯 Quick Start:"
echo "   1. Open: sap_master_launcher.html"
echo "   2. Choose your study mode"
echo "   3. Start learning!"
echo ""
echo "📊 Study Plan:"
echo "   • Days 1-30: Learn 18 questions/day"
echo "   • Days 31-37: Review 76 questions/day"
echo "   • Practice Exam: 75Q in 180min"
echo "   • Pass Score: 750/1000"
echo ""
echo "🎉 Happy studying! Good luck with SAP-C02!"
