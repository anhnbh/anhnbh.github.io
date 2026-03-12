#!/bin/bash

echo "🚀 AWS Certifications Study Hub"
echo "==============================="
echo ""
echo "📚 Available Certifications:"
echo ""
echo "1) 🔧 DevOps Engineer Professional (DOP-C02)"
echo "   └─ 360 questions, complete study system"
echo ""
echo "2) 🌐 Advanced Networking Specialty (ANS-C01)"
echo "   └─ Network-focused questions and scenarios"
echo ""
echo "3) 🏗️ Solutions Architect Professional (SAP-C02)"
echo "   └─ Complex architecture and design patterns"
echo ""
echo "4) 📊 View all certifications"
echo ""

read -p "Choose certification (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🔧 Starting DevOps Professional study..."
        cd "AWS DevOps Profestional/final_repo" && ./start_here.sh
        ;;
    2)
        echo ""
        echo "🌐 Starting Network Specialty study..."
        cd "AWS Network Specity" && ./start_network.sh
        ;;
    3)
        echo ""
        echo "🏗️ Starting Solutions Architect Professional study..."
        cd "AWS Solution Architect Profestional" && ./start_sap.sh
        ;;
    4)
        echo ""
        echo "📊 AWS Certifications Overview:"
        echo ""
        echo "🔧 DevOps Professional (DOP-C02):"
        echo "   • 75 questions, 180 minutes"
        echo "   • Focus: CI/CD, automation, monitoring"
        echo "   • Status: ✅ Complete study system (360 questions)"
        echo ""
        echo "🌐 Network Specialty (ANS-C01):"
        echo "   • 65 questions, 170 minutes" 
        echo "   • Focus: VPC, Direct Connect, Route 53"
        echo "   • Status: 📝 Basic app (sample questions)"
        echo ""
        echo "🏗️ Solutions Architect Professional (SAP-C02):"
        echo "   • 75 questions, 180 minutes"
        echo "   • Focus: Complex architectures, migrations"
        echo "   • Status: 📝 Basic app (sample questions)"
        echo ""
        ;;
    *)
        echo "❌ Invalid choice"
        ;;
esac
