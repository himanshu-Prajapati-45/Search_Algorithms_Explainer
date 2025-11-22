#-------------------------------------------------
# Search Algorithms Explainer - Python (CLI) 
#-------------------------------------------------

# Features for now:
# - Load questions from JSON
# - Show keys menu
# - Choose Q1/Q2
# - Show selected list
# - Show algorithm menu (1/2/3/b/exit) → (functions added later)
#-------------------------------------------------

import json
import os



def load_questions(filename):           #Load questions from a JSON file and return as a dictionary.
    
    
    if not os.path.exists(filename):       #checking the file exist or not
        print(f"Warning: {filename} not found.")
        return {}
    
    try:                #try to open the file and load JSON data
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception:
        print(f"Error: Unable to read '{filename}'.")
        return {}
    
    if not isinstance(data, dict):       #Check if the loaded JSON is in dictionary format
        print("Error: JSON must contain key-value pair.")
        return {}

    return data         #Return the load question






def show_main_q_menu(keys):           
    """Display the main menu where user chooses a question key from JSON."""
    
    # Header
    print("\n--------------------------------------")
    print(" Choose question key from JSON (e.g. Q1)")
    print("--------------------------------------")

    # If keys exist, display them nicely
    if len(keys) > 0:
        print("Available keys:")

        count = 0        # Count how many keys printed in a single line
        line = ""        # Temporary line to store grouped keys

        i = 0
        while i < len(keys):
            line += keys[i] + "  "    # Add key to the line
            count += 1

            # After 10 keys, print the line and reset
            if count == 10:
                print(line)
                line = ""
                count = 0

            i += 1

        # Print leftover keys if any
        if line != "":
            print(line)

    else:
        print("No keys loaded from JSON.")   # If JSON is empty

    # Footer instructions
    print("--------------------------------------")
    print("You may type: Q1  OR  manual  OR  numbers directly (e.g. 1 2 3 4)")
    print("Type 'exit' to quit.")
    print("--------------------------------------")



def print_list_plain(arr):
    """Print the list in a simple, single-line format."""
    
    print("List contents:")
    output = ""
    i = 0
    while i < len(arr):
        output += str(arr[i]) + " "     # Convert each number to string and add to output
        i += 1
    print(output.strip())               # Remove trailing space and print



def show_algo_menu():
    """Display the algorithm selection menu."""
    
    print("\n--------------------------------------")
    print(" Choose algorithm:")
    print(" 1 - Linear Search")                     # Option 1
    print(" 2 - Binary Search (on sorted list)")    # Option 2
    print(" 3 - Compare Linear vs Binary")          # Option 3
    print(" b - Back to choose Q-key")              # Back option
    print(" exit - Quit program")                   # Exit program
    print("--------------------------------------")



# -------------------------
# MAIN PROGRAM FLOW
# -------------------------
def main():
    """Main menu loop for choosing question keys and algorithms."""
    
    # Load all questions from JSON file
    questions = load_questions("questions.json")
    keys = list(questions.keys())   # Extract keys like ["Q1", "Q2", ...]

    # If no questions found, stop program
    if not questions:
        print("No questions loaded. Exiting...")
        return

    # Outer loop → choose Q1, Q2, manual, exit, etc.
    while True:
        show_main_q_menu(keys)                     # Show question key menu
        raw_choice = input("Which question (Q1) or command: ").strip()

        if raw_choice == "":
            continue                               # Ignore empty input
        
        low = raw_choice.lower()

        # Exit command
        if low in ("exit", "quit"):
            print("Goodbye!")
            break

        # ---------- Handle Q1, Q2, Q3... ----------
        if raw_choice in questions:
            
            arr = questions[raw_choice]            # Extract the corresponding list

            print(f"\nLoaded list for {raw_choice}:")
            print_list_plain(arr)                  # Print list nicely
            print("--------------------------------------")

            # -------- ALGORITHM CHOICE MENU --------
            while True:
                show_algo_menu()
                algo = input("Enter choice (1/2/3/b/exit): ").strip().lower()

                if algo == "b":
                    break                          # Go back to choose Q1/Q2 menu

                elif algo == "exit":
                    print("Goodbye!")
                    return                         # Exit completely

                elif algo in ("1", "2", "3"):
                    # Search algorithms will be added later
                    print("\n[INFO] Search algorithms will be added in next step...")
                    input("Press Enter to go back...")
                
                else:
                    print("Invalid choice. Enter 1,2,3,b or exit.")
        
        else:
            print("\n❌ Invalid key:", raw_choice)  # Wrong Q-key entered



# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    main()      
