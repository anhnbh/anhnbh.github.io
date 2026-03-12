#!/bin/bash

# Smart Study App Launcher với random questions

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SMART_APP="$SCRIPT_DIR/apps/smart_study_app.html"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}🚀 AWS DevOps Smart Study App${NC}"
echo "=================================="
echo -e "${YELLOW}✨ Tính năng mới:${NC}"
echo "• Random câu hỏi tự động mỗi lần học"
echo "• Chọn ngày học từ 1-20"
echo "• Có thể random lại bất cứ lúc nào"
echo "• Chỉ cần 1 app duy nhất"
echo ""

if [ ! -f "$SMART_APP" ]; then
    echo -e "${RED}❌ Không tìm thấy smart study app!${NC}"
    exit 1
fi

# Check if specific day is requested
if [ $# -eq 1 ]; then
    DAY=$1
    if [[ $DAY =~ ^[1-9]$|^1[0-9]$|^20$ ]]; then
        echo -e "${GREEN}📚 Mở study app cho ngày $DAY...${NC}"
        echo "🎲 Câu hỏi sẽ được random tự động!"
    else
        echo -e "${RED}❌ Ngày không hợp lệ. Vui lòng chọn từ 1-20.${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}📚 Mở smart study app...${NC}"
    echo "🎯 Bạn có thể chọn bất kỳ ngày nào từ 1-20"
fi

echo ""
echo -e "${YELLOW}🌐 Đang mở trong trình duyệt...${NC}"

# Open in browser
if command -v open &> /dev/null; then
    # macOS
    open "$SMART_APP"
elif command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open "$SMART_APP"
elif command -v start &> /dev/null; then
    # Windows
    start "$SMART_APP"
else
    echo "Vui lòng mở file sau trong trình duyệt:"
    echo "$SMART_APP"
fi

echo ""
echo -e "${GREEN}✅ Hoàn thành! Smart study app đã được mở.${NC}"
echo ""
echo "💡 Hướng dẫn sử dụng:"
echo "• Chọn ngày học từ 1-20"
echo "• Câu hỏi sẽ tự động random"
echo "• Nhấn 'Random lại câu hỏi' để xáo trộn lại"
echo "• Có thể chuyển đổi giữa các ngày bất cứ lúc nào"
