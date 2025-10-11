import json

# Constant subjects
SUBJECTS = ("Math", "English", "History", "Geography", "Art", "Hindi", "Computer", "Biology", "Chemistry", "Physics")

# Student database
students = {}

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists.")
        return
    name = input("Enter Name: ")
    marks = {}
    for subject in SUBJECTS:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")

# Search Student
def search_student():
    key = input("Search by Roll Number or Name: ")
    for roll, data in students.items():
        if roll == key or data["name"].lower() == key.lower():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")
            return
    print("Student not found.")

# Update Marks
def update_marks():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        for subject in SUBJECTS:
            students[roll]["marks"][subject] = int(input(f"New marks for {subject}: "))
        print("Marks updated.")
    else:
        print("Student not found.")

# Delete Student
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if students.pop(roll, None):
        print("Student deleted.")
    else:
        print("Student not found.")

# Display All Students
def display_students():
    sort_by = input("Sort by 'name' or 'marks': ").lower()
    if sort_by == "name":
        sorted_data = sorted(students.items(), key=lambda x: x[1]["name"])
    elif sort_by == "marks":
        sorted_data = sorted(students.items(), key=lambda x: sum(x[1]["marks"].values()), reverse=True)
    else:
        print("Invalid sort option.")
        return
    for roll, data in sorted_data:
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

# Remove Duplicates
def remove_duplicates():
    unique_rolls = set()
    duplicates = []
    for roll in list(students.keys()):
        if roll in unique_rolls:
            duplicates.append(roll)
        else:
            unique_rolls.add(roll)
    for dup in duplicates:
        del students[dup]
    print(f"Removed {len(duplicates)} duplicate entries.")

# Save Data
def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved to students.json")

# Load Data
def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
        print("Data loaded from students.json")
    except FileNotFoundError:
        print("No saved data found.")

# Menu
def menu():
    options = {
        "1": add_student,
        "2": search_student,
        "3": update_marks,
        "4": delete_student,
        "5": display_students,
        "6": remove_duplicates,
        "7": save_data,
        "8": load_data,
        "9": exit
    }
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Remove Duplicate Entries")
        print("7. Save Data")
        print("8. Load Data")
        print("9. Exit")
        choice = input("Enter your choice: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")

# Start the program
menu()