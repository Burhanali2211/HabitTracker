# **Habit Tracker**

A **Habit Tracker** application built in Python that helps you develop and track your habits. You can add habits, mark them as completed, view your progress, and save your data for future use. Your habits and progress are stored in a JSON file to ensure your data persists even after exiting the program.

---

## **Features**
- Add a new habit.
- Mark habits as completed for the current day.
- View your habit progress (including completion dates).
- Save habits and progress to a file (`habits.json`).
- Load previously saved habits when the program starts.

---

## **How It Works**
1. When you run the program, it checks for a `habits.json` file to load previously saved habits.
2. The main menu provides the following options:
   - **1. Add a Habit**: Add a new habit to the list.
   - **2. Mark Habit as Completed**: Select a habit and mark it as completed for today.
   - **3. View Progress**: View all habits with their completion dates.
   - **4. Save and Exit**: Save your data to the `habits.json` file and exit the program.
3. Your progress is automatically saved when you exit the program.

---

## **Requirements**
- Python 3.6 or higher
- No additional libraries are required; this program uses built-in Python modules like `json` and `datetime`.

---

## **How to Run the Program**
1. Clone this repository or download the script to your local machine.
   ```bash
   git clone https://github.com/your-username/HabitTracker.git
   cd habit-tracker
