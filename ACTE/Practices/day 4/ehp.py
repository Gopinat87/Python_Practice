def add_student():
    with open("students.txt", "a") as f:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")
        f.write(f"{name},{roll},{marks}\n")
    print("Student record added successfully.")

def view_students():
    try:
        with open("students.txt", "r") as f:
            print("\n--- Student Records ---")
            for line in f:
                name, roll, marks = line.strip().split(",")
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    except FileNotFoundError:
        print("No student records found!")

# Menu
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
    