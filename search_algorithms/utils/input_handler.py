"""
Input handling utilities for user interactions.
"""


def take_list_input():
    """
    Take list input from user when user types 'manual'.
    
    Returns:
        list: List of integers entered by the user.
    """
    while True:
        raw = input("\nEnter list of numbers (comma or space separated): ")
        parts = raw.replace(",", " ").split()
        numbers = []
        for part in parts:
            try:
                numbers.append(int(part))
            except Exception:
                print("Please enter only integers. Try again.")
                numbers = []
                break
        if len(numbers) == 0:
            print("List cannot be empty.")
            continue
        return numbers
