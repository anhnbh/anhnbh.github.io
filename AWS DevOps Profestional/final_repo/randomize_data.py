#!/usr/bin/env python3
import json
import random

def randomize_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Randomize question order
    random.shuffle(data)
    
    # Reassign sequential IDs
    for i, question in enumerate(data, 1):
        question['id'] = i
    
    # Randomize answer options and update correct indices
    for question in data:
        if 'options' in question and 'correct' in question:
            options = question['options']
            correct_indices = question['correct']
            
            # Filter out invalid indices
            valid_correct = [idx for idx in correct_indices if 0 <= idx < len(options)]
            if len(valid_correct) != len(correct_indices):
                print(f"Warning: Question {question['id']} had invalid indices, fixed")
                question['correct'] = valid_correct
            
            # Create mapping of old index to new index
            indices = list(range(len(options)))
            random.shuffle(indices)
            
            # Reorder options
            new_options = [options[i] for i in indices]
            
            # Update correct indices
            new_correct = []
            for old_idx in valid_correct:
                new_idx = indices.index(old_idx)
                new_correct.append(new_idx)
            
            question['options'] = new_options
            question['correct'] = sorted(new_correct)
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Randomized {len(data)} questions and their answers")

if __name__ == "__main__":
    randomize_data("/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS DevOps Profestional/final_repo/apps/data.json")
