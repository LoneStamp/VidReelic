import os

memory_file = "memory.txt"


def remember_activity(activity):
   
    with open(memory_file, "a") as file:
        file.write(activity + "\n")
    print(f"Activity '{activity}' has been remembered.")

def recall_activities():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            activities = file.readlines()
            return [activity.strip() for activity in activities]  # Remove newlines
    else:
        return []

def display_activities():
    activities = recall_activities()
    if activities:
        print("Here are the activities I've remembered:")
        for activity in activities:
            print(f"- {activity}")
    else:
        print("I don't remember any activities yet.")


def main():
    while True:
        print("\n1. Remember an activity")
        print("2. Recall and display activities")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            activity = input("What activity do you want me to remember? ")
            remember_activity(activity)
        elif choice == "2":
            display_activities()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
