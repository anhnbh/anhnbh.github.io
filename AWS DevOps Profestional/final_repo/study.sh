#!/bin/bash

# Quick launcher for specific day
DAY=${1:-1}

echo "🚀 Quick Study Launcher"
echo "======================"

if [[ $DAY -lt 1 || $DAY -gt 20 ]]; then
    echo "❌ Invalid day: $DAY"
    echo ""
    echo "💡 Usage: ./study.sh [day]"
    echo "   Examples:"
    echo "   ./study.sh     # Day 1"
    echo "   ./study.sh 5   # Day 5"
    echo "   ./study.sh 20  # Day 20"
    echo ""
    echo "📅 Available days: 1-20"
    exit 1
fi

echo "📅 Starting Day $DAY..."
cd apps && ./start_study_v2.sh $DAY
