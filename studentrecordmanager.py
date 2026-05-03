# Student Record Manager

students = []


# Display menu
def displayMenu():
    print("\n----- Student Record Manager -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Show Statistics")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")


# Add student
def addStudent():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    while True:
        marks = float(input("Enter Marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks. Enter between 0 and 100.")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


# Display all students
def displayStudents():
    if len(students) == 0:
        print("No records found.")
        return

    print("\nStudent Records:")
    print("-" * 50)

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Marks: {student['marks']}")
        print("-" * 50)


# Search student
def searchStudent():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found.")


# Calculate statistics
def calculateStatistics():
    if len(students) == 0:
        print("No records available.")
        return

    marks_list = []

    for student in students:
        marks_list.append(student["marks"])

    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)

    print("\nStatistics")
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Average Marks:", round(average, 2))


# Save to file
def saveToFile():
    file = open("students.txt", "w")

    for student in students:
        line = f"{student['id']},{student['name']},{student['age']},{student['marks']}\n"
        file.write(line)

    file.close()

    print("Records saved successfully.")


# Load from file
def loadFromFile():
    global students

    try:
        file = open("students.txt", "r")

        students = []

        for line in file:
            data = line.strip().split(",")

            student = {
                "id": data[0],
                "name": data[1],
                "age": int(data[2]),
                "marks": float(data[3])
            }

            students.append(student)

        file.close()

        print("Records loaded successfully.")

    except FileNotFoundError:
        print("File not found.")


# Main program
while True:
    displayMenu()

    choice = input("Enter your choice: ")

    if choice == "1":
        addStudent()

    elif choice == "2":
        displayStudents()

    elif choice == "3":
        searchStudent()

    elif choice == "4":
        calculateStatistics()

    elif choice == "5":
        saveToFile()

    elif choice == "6":
        loadFromFile()

    elif choice == "7":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")