#given list of roll numbers: [101,105,102,101,108,105,110]. print all unique roll numbers in the list
roll_no=[101,105,102,101,108,105,110]
print(list(set(roll_no)))

#given empployee records in the form of the list of tuples where each tuple contains: (employee id, employee name, employee salary) 

# Given employee records in the form of a list of tuples: (Employee ID, Employee Name, Salary)
employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

# Ask user to enter Employee ID and convert it to an integer
search_id = int(input("Enter Employee ID to search: "))

# Flag to track if the employee is found
found = False

# Search through the records
for emp in employees:
    if emp[0] == search_id:
        print(f"Employee Found!\nID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
        found = True
        break

if not found:
    print("Employee ID not found in the records.")

