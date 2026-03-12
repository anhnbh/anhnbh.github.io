#!/bin/bash
echo "🚀 AWS DevOps Professional Study Kit"
echo "===================================="
echo ""
echo "📱 Study Apps:"
echo "   cd apps && ./start_study_v2.sh"
echo ""
echo "📊 Export Materials:"
echo "   cd scripts && ./export_everything.sh"
echo ""
echo "📄 Documentation:"
echo "   open docs/README.md"
echo ""
echo "🎯 Choose your action:"
echo "1) Start studying (choose day 1-20)"
echo "2) Review mode (5 ngày ôn tập cuối)"
echo "3) Practice exam (75 câu, 180 phút)"
echo "4) Export all materials"
echo "5) View documentation"
echo ""
read -p "Enter choice (1-5): " choice

case $choice in
    1) 
        echo ""
        echo "📅 Which day do you want to study? (1-20)"
        echo "   Week 1: Days 1-7   (Questions 1-126)"
        echo "   Week 2: Days 8-14  (Questions 127-252)"
        echo "   Week 3: Days 15-20 (Questions 253-363)"
        echo ""
        read -p "Enter day (1-20) or press Enter for Day 1: " day
        day=${day:-1}
        cd apps && ./start_study_v2.sh $day
        ;;
    2)
        echo ""
        echo "🔥 Review Mode - 5 Ngày Ôn Tập Cuối"
        echo "   1) Ngày 1: Mixed (50 câu)"
        echo "   2) Ngày 2: Multiple Choice (30 câu)"  
        echo "   3) Ngày 3: Hard Mode (25 câu)"
        echo "   4) Ngày 4: Random Marathon (100 câu)"
        echo "   5) Ngày 5: Final Sprint"
        echo ""
        read -p "Choose review day (1-5) or press Enter for Day 1: " review_day
        review_day=${review_day:-1}
        ./review.sh $review_day
        ;;
    3)
        ./exam.sh
        ;;
    4) cd scripts && ./export_everything.sh ;;
    5) open docs/ ;;
    *) echo "Invalid choice" ;;
esac
