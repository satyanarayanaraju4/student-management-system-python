import json
import os

FILENAME = 'students.json'

def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)

def add_student():
    data = load_data()
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    student = {"roll": roll, "name": name, "marks": marks}
    data.append(student)
    save_data(data)
    print("Student added successfully.\n")

def display_all():
    data = load_data()
    if not data:
        print("No student records found.\n")
        return
    print("\n--- All Students ---")
    for s in data:
        print(f"Roll No: {s['roll']}\nName: {s['name']}\nMarks: {s['marks']}\n------------------")

def search_student():
    data = load_data()
    roll = input("Enter Roll No to search: ")
    for s in data:
        if s['roll'] == roll:
            print(f"Found!\nName: {s['name']}\nMarks: {s['marks']}\n")
            return
    print("Student not found.\n")

def update_student():
    data = load_data()
    roll = input("Enter Roll No to update: ")
    for s in data:
        if s['roll'] == roll:
            s['name'] = input("Enter new name: ")
            s['marks'] = float(input("Enter new marks: "))
            save_data(data)
            print("Record updated successfully.\n")
            return
    print("Student not found.\n")

def delete_student():
    data = load_data()
    roll = input("Enter Roll No to delete: ")
    new_data = [s for s in data if s['roll'] != roll]
    if len(new_data) == len(data):
        print("Student not found.\n")
    else:
        save_data(new_data)
        print("Record deleted successfully.\n")

def menu():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. Display All")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    menu()
