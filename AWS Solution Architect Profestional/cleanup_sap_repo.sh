#!/bin/bash

echo "🧹 Cleaning up SAP-C02 repository..."
echo "=================================="

# Remove scattered files (keep only final_repo)
echo "📁 Removing scattered files..."

# Remove old daily study files
rm -f day_*.html
rm -f review_day_*.html

# Remove old review files
rm -f sap_review_*.html

# Remove old main apps
rm -f sap_c02_study_app.html
rm -f sap_exam_mode.html
rm -f sap_master_launcher.html

# Remove old exports
rm -f sap_c02_questions.md
rm -f sap_c02_questions.csv

# Keep only essential files
echo "✅ Keeping essential files:"
echo "   - final_repo/ (complete organized system)"
echo "   - sap_c02_questions.json (source data)"
echo "   - *.py (scripts)"
echo "   - *.sh (setup scripts)"
echo "   - SAPC02_*.html (original HTML files)"

echo ""
echo "🎯 Clean repository structure:"
echo "   📁 final_repo/"
echo "   ├── master_launcher.html (START HERE)"
echo "   ├── main_study_app.html"
echo "   ├── exam_mode.html"
echo "   ├── review_*.html"
echo "   ├── questions.json"
echo "   ├── daily_study/"
echo "   │   └── day_01.html → day_30.html"
echo "   ├── review_days/"
echo "   │   └── review_day_1.html → review_day_7.html"
echo "   └── exports/"
echo "       ├── questions.md"
echo "       └── questions.csv"
echo ""
echo "✅ Repository cleanup complete!"
echo "🚀 Open: final_repo/master_launcher.html"
