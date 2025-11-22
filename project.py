#-------------------------------------------------
# Search Algorithms Explainer - Python (CLI) 
#-------------------------------------------------

# Features ----->

# - Linear Search 
# - Binary Search
# - Comparing
# - History
#- Argparse CLI Commands

#-------------------------------------------------

import json
import os

def load_questions(filename):     
    
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found.")
        return {}
    
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data = json.load(file)
    
    except Exception:
        print(f"Error: Unable to read'{filename}'.")    
        return {}
    
    if not isinstance(data,dict):
        print("Error: JSON must contain key-value pair.")
        return {}

    return data

if __name__ == "__main__":
    questions = load_questions("questions.json")
    print("KEYS:",list(questions.keys()))