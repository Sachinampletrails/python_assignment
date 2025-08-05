# Step 1: Create an empty dictionary to store student names and grades
student_grades = {}

# Step 2: Use a loop to allow the user to perform actions multiple times
while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Step 3: Add new student and grade
    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print("This student already exists. You can update the grade instead.")
        else:
            grade = input("Enter student grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    # Step 4: Update grade for existing student
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print("Student not found. Please add the student first.")

    # Step 5: Print all student grades
    elif choice == '3':
        if student_grades:
            print("\nStudent Grades:")
            for student, grade in student_grades.items():
                print(f"{student}: {grade}")
        else:
            print("No student grades available.")

    # Step 6: Exit the program
    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")
