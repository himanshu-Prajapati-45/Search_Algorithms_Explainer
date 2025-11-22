#-------------------------------------------------
# Search Algorithms Explainer - Python (CLI) 
#-------------------------------------------------

# Features for now:
# - Load questions from JSON
# - Show keys menu
# - Choose Q1/Q2 or manual or inline numbers
# - Show selected list
# - Show algorithm menu (1/2/3/b/exit)
# - Linear Search (option 1) with step-by-step output
#-------------------------------------------------

import json
import os


def load_questions(filename):
    """Load questions from a JSON file and return as a dictionary."""

    if not os.path.exists(filename):        # Check if file exists
        print(f"Warning: {filename} not found.")
        return {}
    
    try:                                    # Try to open and load JSON
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception:
        print(f"Error: Unable to read '{filename}'.")
        return {}
    
    if not isinstance(data, dict):          # JSON must be a dictionary
        print("Error: JSON must contain key-value pair.")
        return {}

    return data



def show_main_q_menu(keys):
    """Display the main menu where user chooses a question key from JSON."""

    print("\n--------------------------------------")
    print(" Choose question key from JSON (e.g. Q1)")
    print("--------------------------------------")

    # Print all keys nicely
    if len(keys) > 0:
        print("Available keys:")

        count = 0
        line = ""

        i = 0
        while i < len(keys):
            line += keys[i] + "  "
            count += 1
            if count == 10:                # Print 10 keys per line
                print(line)
                line = ""
                count = 0
            i += 1

        if line != "":
            print(line)

    else:
        print("No keys loaded from JSON.")

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
        output += str(arr[i]) + " "
        i += 1
    print(output.strip())



# ---------------------------
#   EXTRA FUNCTIONS ADDED
# ---------------------------

def take_list_input():
    """Take list input from user when user types 'manual'."""
    while True:
        raw = input("\nEnter list of numbers (comma or space separated): ")
        parts = raw.replace(",", " ").split()
        numbers = []
        for part in parts:
            try:
                numbers.append(int(part))      # Convert to int
            except Exception:
                print("Please enter only integers. Try again.")
                numbers = []
                break
        if len(numbers) == 0:
            print("List cannot be empty.")
            continue
        return numbers


def convert_num(s):
    """Try to convert inline input like '1 2 3' or '4,5,6' into list of integers."""
    if s.strip() == "":
        return None

    parts = s.replace(",", " ").split()
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except Exception:
            return None       # If any value fails → not a number input

    return nums if len(nums) > 0 else None


def take_target_input():
    """Ask the user to enter the target number and validate it."""
    while True:
        raw = input("Enter target number to search: ").strip()
        try:
            return int(raw)
        except Exception:
            print("Please enter a valid integer.")


def linear_search(arr, target):
    """Perform linear search with step-by-step explanation."""
    print("\n--------- LINEAR SEARCH ---------")
    steps = 0

    for i in range(len(arr)):
        value = arr[i]
        steps += 1
        # Same style as you showed: spaces around = and commas
        print(f"Step {steps} : index = {i} , element = {value} , target = {target}")

        if value == target:
            print("=> Match found")
            print(f"=> Element {target} found at index {i}")
            print("Total steps taken (Linear Search):", steps)
            return
        else:
            print("=> Not equal, moving next\n")

    # If not found
    print("=> Element not found")
    print("Total steps taken (Linear Search):", steps)



def show_algo_menu():
    """Display the algorithm selection menu."""
    
    print("\n--------------------------------------")
    print(" Choose algorithm:")
    print(" 1 - Linear Search")
    print(" 2 - Binary Search (on sorted list)")
    print(" 3 - Compare Linear vs Binary")
    print(" b - Back to choose Q-key")
    print(" exit - Quit program")
    print("--------------------------------------")



# -------------------------
# MAIN PROGRAM FLOW
# -------------------------
def main():
    """Main menu loop for choosing question keys and algorithms."""

    questions = load_questions("questions.json")      # Load JSON
    keys = list(questions.keys())                     # All Q keys

    if not questions:
        print("No questions loaded. Exiting...")
        return

    while True:
        show_main_q_menu(keys)
        raw_choice = input("Which question (Q1) or command: ").strip()

        if raw_choice == "":
            continue

        low = raw_choice.lower()

        # Exit program
        if low in ("exit", "quit"):
            print("Goodbye!")
            break

        # -----------------------------------
        # Handle manual / inline / Q1, Q2 etc
        # -----------------------------------
        
        if low == "manual":                            # User types "manual"
            arr = take_list_input()                    # Ask for list manually

        else:
            parsed = convert_num(raw_choice)           # Try inline numbers

            if parsed is not None:                     # Inline numbers detected
                arr = parsed

            elif raw_choice in questions:              # Q1, Q2, ...
                arr = questions[raw_choice]

            else:                                      # Neither Q1 nor numbers
                print("\n❌ Invalid key or input:", raw_choice)
                continue

        # Print loaded list
        print(f"\nLoaded list for {raw_choice}:")
        print_list_plain(arr)
        print("--------------------------------------")

        # -------------------------
        # Algorithm Selection Menu
        # -------------------------
        while True:
            show_algo_menu()
            algo = input("Enter choice (1/2/3/b/exit): ").strip().lower()

            if algo == "b":
                break

            elif algo == "exit":
                print("Goodbye!")
                return

            elif algo == "1":
                # Linear search: ask for target, then run search
                target = take_target_input()
                linear_search(arr, target)
                input("Press Enter to continue...")

            elif algo in ("2", "3"):
                # Placeholders for now
                print("\n[INFO] Search algorithms will be added in next step...")
                input("Press Enter to go back...")

            else:
                print("Invalid choice. Enter 1,2,3,b or exit.")



if __name__ == "__main__":
    main()
