#!/bin/bash

echo "🌐 AWS Network Specialty Study App"
echo "================================="
echo ""
echo "📋 Exam Info:"
echo "   • AWS Certified Advanced Networking - Specialty"
echo "   • 65 questions, 170 minutes"
echo "   • Passing score: 750/1000"
echo "   • Focus: VPC, Direct Connect, Route 53, CloudFront"
echo ""

if [ -f "network_study_app.html" ]; then
    echo "✅ Found Network Specialty study app"
    APP_FILE="network_study_app.html"
else
    echo "❌ App not found, creating..."
    python3 create_network_app.py
    APP_FILE="network_study_app.html"
fi

echo "🚀 Starting AWS Network Specialty study..."

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
echo "   - Focus on VPC design patterns"
echo "   - Understand Direct Connect vs VPN"
echo "   - Master Route 53 routing policies"
echo "   - Know CloudFront behaviors"
echo ""
echo "🍀 Good luck with your Network Specialty!"
