#--------------------------------------------------------------------
# Search Algorithms Explainer - Python (CLI) 
#---------------------------------------------------------------------

# Features:
# - Load questions from JSON
# - Show keys menu
# - Choose Q1/Q2 or manual or inline numbers
# - Show selected list
# - Show algorithm menu (1/2/3/b/exit)
# - Linear Search (option 1) with step-by-step output
# - Binary Search (option 2) with step-by-step output (on sorted list)
# - Compare Linear vs Binary (option 3)
# - Log results to results.json (question, method, time/space complexity, steps, found/not found)
#----------------------------------------------------------------------

import json
import os
import argparse 
import sys

# Result file name for logging
RESULTS_FILE = "results.json"


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
#   RESULT LOGGING
# ---------------------------

def save_result(question, method, steps, time_complexity, space_complexity, found):
    """
    Save one result entry into results.json as a list of records.
    Each record contains:
    - question
    - method
    - time_complexity
    - space_complexity
    - steps
    - found (Found / Not Found)
    """
    entry = {
        "question": question,                 # e.g. "Q1", "manual", "inline: 1 2 3"
        "method": method,                     # "Linear Search" / "Binary Search"
        "time_complexity": time_complexity,   # e.g. "O(n)"
        "space_complexity": space_complexity, # e.g. "O(1)"
        "steps": steps,
        "found": "Found" if found else "Not Found"
    }

    # Load existing data (if any)
    data = []
    if os.path.exists(RESULTS_FILE):
        try:
            with open(RESULTS_FILE, "r", encoding="utf-8") as f:
                old = json.load(f)
                if isinstance(old, list):
                    data = old
        except Exception:
            # If file corrupt or not a list, start fresh
            data = []

    data.append(entry)

    # Save back to file
    try:
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception:
        print("Warning: Could not write to results.json")


#----------------------------
#   CLI COMMAND FUNCTION
#----------------------------

def show_history():
    """Display the history of all searches from results.json"""
    
    print("\n" + "="*60)
    print(" SEARCH HISTORY")
    print("="*60)
    
    if not os.path.exists(RESULTS_FILE):
        print("No history found. The results file doesn't exist yet.")
        print("="*60)
        return
    
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            if not isinstance(data, list) or len(data) == 0:
                print("No search results found in history.")
                print("="*60)
                return
            
            for idx, entry in enumerate(data, 1):
                print(f"\n[{idx}] Question: {entry.get('question', 'N/A')}")
                print(f"    Method: {entry.get('method', 'N/A')}")
                print(f"    Result: {entry.get('found', 'N/A')}")
                print(f"    Steps: {entry.get('steps', 'N/A')}")
                print(f"    Time Complexity: {entry.get('time_complexity', 'N/A')}")
                print(f"    Space Complexity: {entry.get('space_complexity', 'N/A')}")
            
            print("\n" + "="*60)
            print(f"Total entries: {len(data)}")
            print("="*60)
            
    except Exception as e:
        print(f"Error reading history: {e}")
        print("="*60)


def clear_last_result():
    """Remove the last entry from results.json"""
    
    if not os.path.exists(RESULTS_FILE):
        print("\n❌ No results file found. Nothing to clear.")
        return
    
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            if not isinstance(data, list) or len(data) == 0:
                print("\n❌ No results found in history. Nothing to clear.")
                return
            
            # Get the last entry before removing
            last_entry = data[-1]
            
            # Remove the last entry
            data = data[:-1]
            
            # Save back
            with open(RESULTS_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            
            print("\n✓ Last result cleared successfully!")
            print(f"  Removed: Question '{last_entry.get('question', 'N/A')}' - Method '{last_entry.get('method', 'N/A')}'")
            print(f"  Remaining entries: {len(data)}")
            
    except Exception as e:
        print(f"\n❌ Error clearing last result: {e}")

# ---------------------------
#   EXTRA FUNCTIONS
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
    """Perform linear search with step-by-step explanation.
       Returns: (index_found_or_-1, steps_taken)
    """
    print("\n--------- LINEAR SEARCH ---------")
    steps = 0

    for i in range(len(arr)):
        value = arr[i]
        steps += 1
        print(f"Step {steps} : index = {i} , element = {value} , target = {target}")

        if value == target:
            print("=> Match found")
            print(f"=> Element {target} found at index {i}")
            print("Total steps taken (Linear Search):", steps)
            return i, steps
        else:
            print("=> Not equal, moving next\n")

    print("=> Element not found")
    print("Total steps taken (Linear Search):", steps)
    return -1, steps



def binary_search(arr, target):
    """Perform binary search with step-by-step explanation on a sorted copy.
       Returns: (index_found_or_-1_in_sorted_array, steps_taken)
    """
    print("\n--------- BINARY SEARCH ---------")
    if len(arr) == 0:
        print("List is empty. Nothing to search.")
        return -1, 0

    # Binary search requires a sorted list → use a sorted copy
    sorted_arr = sorted(arr)
    print("Note: Binary Search works on a sorted list.")
    print("Sorted list used:")
    print_list_plain(sorted_arr)

    low, high = 0, len(sorted_arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        value = sorted_arr[mid]

        print(
            f"Step {steps} : low = {low} , high = {high} , mid = {mid} , "
            f"element = {value} , target = {target}"
        )

        if value == target:
            print("=> Match found")
            print(f"=> Element {target} found at index {mid} (in sorted list)")
            print("Total steps taken (Binary Search):", steps)
            return mid, steps
        elif value < target:
            print("=> element < target , searching RIGHT half (low = mid + 1)\n")
            low = mid + 1
        else:
            print("=> element > target , searching LEFT half (high = mid - 1)\n")
            high = mid - 1

    print("=> Element not found")
    print("Total steps taken (Binary Search):", steps)
    return -1, steps



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
            question_label = "manual"

        else:
            parsed = convert_num(raw_choice)           # Try inline numbers

            if parsed is not None:                     # Inline numbers detected
                arr = parsed
                question_label = "inline: " + raw_choice

            elif raw_choice in questions:              # Q1, Q2, ...
                arr = questions[raw_choice]
                question_label = raw_choice

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
                index, steps = linear_search(arr, target)
                found = index != -1

                # Log result for Linear Search
                save_result(
                    question=question_label,
                    method="Linear Search",
                    time_complexity="O(n)",
                    space_complexity="O(1)",
                    steps=steps,
                    found=found
                )

                input("Press Enter to continue...")

            elif algo == "2":
                # Binary search: ask for target, then run search
                target = take_target_input()
                index, steps = binary_search(arr, target)
                found = index != -1

                # Log result for Binary Search
                save_result(
                    question=question_label,
                    method="Binary Search",
                    time_complexity="O(log n)",
                    space_complexity="O(1)",
                    steps=steps,
                    found=found
                )

                input("Press Enter to continue...")

            elif algo == "3":
                # Compare Linear vs Binary
                target = take_target_input()
                print("\n===== Comparing Linear Search vs Binary Search =====")
                print("Same list and same target will be used for both.\n")

                print("[1] Running Linear Search...\n")
                index_lin, steps_lin = linear_search(arr, target)
                found_lin = index_lin != -1

                # Log Linear Search (Compare Mode)
                save_result(
                    question=question_label,
                    method="Linear Search (Compare Mode)",
                    time_complexity="O(n)",
                    space_complexity="O(1)",
                    steps=steps_lin,
                    found=found_lin
                )

                print("\n[2] Running Binary Search...\n")
                index_bin, steps_bin = binary_search(arr, target)
                found_bin = index_bin != -1

                # Log Binary Search (Compare Mode)
                save_result(
                    question=question_label,
                    method="Binary Search (Compare Mode)",
                    time_complexity="O(log n)",
                    space_complexity="O(1)",
                    steps=steps_bin,
                    found=found_bin
                )

                print("\n----------- SUMMARY -----------")
                # Found / not found comparison
                if found_lin:
                    print(f"Linear Search  : Found (index {index_lin} in original list)")
                else:
                    print("Linear Search  : Not found")

                if found_bin:
                    print(f"Binary Search  : Found (index {index_bin} in sorted list)")
                else:
                    print("Binary Search  : Not found")

                print("\nSteps taken:")
                print(f"  Linear Search  -> {steps_lin} steps")
                print(f"  Binary Search  -> {steps_bin} steps")

                print("\nTime Complexity:")
                print("  Linear Search  -> O(n)")
                print("  Binary Search  -> O(log n)  (requires sorted list)")
                print("-------------------------------")
                input("Press Enter to go back...")

            else:
                print("Invalid choice. Enter 1,2,3,b or exit.")



if __name__ == "__main__":
    main()
