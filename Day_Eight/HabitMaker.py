import json
from datetime import date

# List to store habits
habits = []

# Menu Function
def menu():
    print("\nHello, Welcome to Habit Tracker!")
    print("1. Add a Habit")
    print("2. Mark Habit as Completed")
    print("3. View Progress")
    print("4. Save and Exit")

# Add a Habit
def add_habit():
    habit_name = input("Enter the name of the habit: ")
    habit = {"name": habit_name, "completed_dates": []}
    habits.append(habit)
    print(f"Habit '{habit_name}' added successfully!")

# Mark Habit as Completed
def mark_habit():
    if not habits:
        print("No habits to mark. Please add a habit first.")
        return
    print("\nYour Habits:")
    for idx, habit in enumerate(habits, start=1):
        print(f"{idx}. {habit['name']}")

    try:
        choice = int(input("Select a habit to mark as completed: ")) - 1
        if 0 <= choice < len(habits):
            today = date.today().isoformat()
            if today not in habits[choice]["completed_dates"]:
                habits[choice]["completed_dates"].append(today)
                print(f"Habit '{habits[choice]['name']}' marked as completed for today!")
            else:
                print("You already marked this habit as completed for today.")
        else:
            print("Invalid choice! Please select a valid habit.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# View Progress
def view_progress():
    if not habits:
        print("No habits to show. Please add a habit first.")
        return
    print("\n--- Habit Progress ---")
    for habit in habits:
        print(f"\nHabit: {habit['name']}")
        print("Completed on:", ", ".join(habit['completed_dates']) if habit['completed_dates'] else "No progress yet.")
    print("\n-----------------------")

# Save Habits to File
def save_habits(filename="habits.json"):
    with open(filename, "w") as file:
        json.dump(habits, file)
    print(f"Habits saved successfully to {filename}!")

# Load Habits from File
def load_habits(filename="habits.json"):
    global habits
    try:
        with open(filename, "r") as file:
            habits = json.load(file)
            if not isinstance(habits, list):  # Validate the data
                print("Invalid data in file. Starting fresh.")
                habits = []
        print(f"Habits loaded successfully from {filename}!")
    except FileNotFoundError:
        print("No saved habits found. Starting fresh.")

# Main Program
if __name__ == "__main__":
    load_habits()

    while True:
        menu()
        menu_choice = input("\nSelect an option (1/2/3/4): ")

        if menu_choice == "1":
            add_habit()
        elif menu_choice == "2":
            mark_habit()
        elif menu_choice == "3":
            view_progress()
        elif menu_choice == "4":
            save_habits()
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid choice! Please try again.")
