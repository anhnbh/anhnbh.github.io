#!/bin/bash

echo "🏗️ AWS Solutions Architect Professional Study App"
echo "==============================================="
echo ""
echo "📋 Exam Info:"
echo "   • AWS Certified Solutions Architect - Professional"
echo "   • 75 questions, 180 minutes"
echo "   • Passing score: 750/1000"
echo "   • Focus: Complex architectures, migrations, cost optimization"
echo ""

if [ -f "sap_study_app.html" ]; then
    echo "✅ Found SAP-C02 study app"
    APP_FILE="sap_study_app.html"
else
    echo "❌ App not found, creating..."
    python3 create_sap_app.py
    APP_FILE="sap_study_app.html"
fi

echo "🚀 Starting AWS Solutions Architect Professional study..."

# Get the full path
FULL_PATH="$(pwd)/$APP_FILE"

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
echo "💡 Study Tips:"
echo "   - Think enterprise-scale solutions"
echo "   - Focus on cost optimization strategies"
echo "   - Master hybrid architectures"
echo "   - Understand migration patterns"
echo "   - Know disaster recovery strategies"
echo ""
echo "🍀 Good luck with your SAP-C02!"
