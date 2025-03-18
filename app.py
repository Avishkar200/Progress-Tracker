from datetime import datetime

def save_progress(tasks, progress):
    """Save tasks and progress to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("progress.txt", "a") as file:
        file.write(f"\n\nEntry on {timestamp}:\n")
        file.write("Your Tasks For Today:\n")
        for task in tasks:
            file.write(f"- {task}\n")
        file.write(f"\nYour today's progress is {progress}%")
    print("\nYour tasks and progress have been saved to 'progress.txt'.")

def view_progress():
    """View all previous progress entries from the file."""
    try:
        with open("progress.txt", "r") as file:
            print("\nPrevious Progress Entries:")
            print(file.read())
    except FileNotFoundError:
        print("\nNo progress entries found. Start your journey!")

def main():
    print("Start Your Journey Of Improvement!!!")
    while True:
        print("\nMenu:")
        print("1. Enter Today's Tasks")
        print("2. View Previous Progress")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            print("\nEnter your tasks for today")
            tasks = []
            for i in range(5):
                task = input(f"Task {i + 1}: ")  # Prompt the user for each task
                tasks.append(task)  # Add the task to the list

            print("\nYour Tasks For Today!!!")
            for task in tasks:
                print(task)

            print("\nBest of luck to you!!!")

            # Ask the user if they completed each task
            count = 0  # Initialize the count of completed tasks
            for i in range(5):
                while True:  # Keep asking until a valid input is provided
                    choice = input(f"Have you completed '{tasks[i]}'? (Y/N): ").strip().upper()
                    if choice == "Y" or choice == "N":
                        break
                    else:
                        print("Invalid input! Please enter 'Y' or 'N'.")
                if choice == "Y":
                    count += 1  # Increment the count if the task is completed

            # Calculate progress
            progress = count * 20  # Each task contributes 20% to the progress
            print(f"\nYour today's progress is {progress}%")

            # Save tasks and progress to a file
            save_progress(tasks, progress)

        elif choice == "2":
            # View previous progress entries
            view_progress()

        elif choice == "3":
            print("\nThank you for using the Improvement Tracker. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()