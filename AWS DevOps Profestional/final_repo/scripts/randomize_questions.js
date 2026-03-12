#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Fisher-Yates shuffle algorithm
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

function randomizeQuestionsInFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Extract questions array using regex
        const questionsMatch = content.match(/const questions = (\[[\s\S]*?\]);/);
        if (!questionsMatch) {
            console.log(`❌ Không tìm thấy questions array trong ${path.basename(filePath)}`);
            return false;
        }
        
        // Parse questions array
        const questionsStr = questionsMatch[1];
        const questions = eval(questionsStr);
        
        // Shuffle questions
        const shuffledQuestions = shuffleArray(questions);
        
        // Convert back to string with proper formatting
        const newQuestionsStr = JSON.stringify(shuffledQuestions, null, 12)
            .replace(/"/g, '"')
            .replace(/'/g, "'");
        
        // Replace in content
        const newContent = content.replace(
            /const questions = \[[\s\S]*?\];/,
            `const questions = ${newQuestionsStr};`
        );
        
        // Write back to file
        fs.writeFileSync(filePath, newContent, 'utf8');
        console.log(`✅ Đã random ${questions.length} câu hỏi trong ${path.basename(filePath)}`);
        return true;
        
    } catch (error) {
        console.error(`❌ Lỗi khi xử lý ${path.basename(filePath)}:`, error.message);
        return false;
    }
}

// Main function
function main() {
    const appsDir = path.join(__dirname, '..', 'apps');
    
    if (process.argv.length > 2) {
        // Random specific file
        const fileName = process.argv[2];
        const filePath = path.join(appsDir, fileName);
        
        if (!fs.existsSync(filePath)) {
            console.error(`❌ File không tồn tại: ${fileName}`);
            process.exit(1);
        }
        
        randomizeQuestionsInFile(filePath);
    } else {
        // Random all study app files
        const files = fs.readdirSync(appsDir)
            .filter(file => file.startsWith('study_app_day') && file.endsWith('.html'));
        
        console.log(`🎲 Bắt đầu random câu hỏi cho ${files.length} files...`);
        
        let successCount = 0;
        files.forEach(file => {
            const filePath = path.join(appsDir, file);
            if (randomizeQuestionsInFile(filePath)) {
                successCount++;
            }
        });
        
        console.log(`\n🎉 Hoàn thành! Đã random ${successCount}/${files.length} files thành công.`);
    }
}

if (require.main === module) {
    main();
}
