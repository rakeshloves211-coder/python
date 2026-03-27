#MiniProject1
employees = []
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    employee = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    
    employees.append(employee)
    print(" Employee added successfully!")
def update_employee():
    name = input("Enter the name of the employee to update: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            emp["age"] = int(input("Enter new age: "))
            emp["role"] = input("Enter new role: ")
            emp["salary"] = float(input("Enter new salary: "))
            print(" Employee details updated!")
            return
    print(" Employee not found!")

def delete_employee():
    name = input("Enter the name of the employee to delete: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            employees.remove(emp)
            print(" Employee deleted!")
            return
    print(" Employee not found!")

def display_employees():
    if not employees:
        print("No employees found.")
        return
    
    print("\n===== Employee List =====")
    print(f"{'Name':<15}{'Age':<5}{'Role':<15}{'Salary':<10}")
    print("-" * 45)
    for emp in employees:
        print(f"{emp['name']:<15}{emp['age']:<5}{emp['role']:<15}{emp['salary']:<10}")
    print("-" * 45)

while True:
    print("\n===== Employee Management Menu =====")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Display All Employees")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        print(" Exiting Employee Management System")
        break
    else:
        print(" Invalid choice, try again!")

#MiniProject2
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
def report_card():
    student = {}
    
    student['name'] = input("Enter student name: ")
    student['marks'] = {}
    
    subjects = ["Math", "Science", "English"]
    
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        student['marks'][subject] = mark
    
    total = sum(student['marks'].values())
    average = total / len(subjects)
    grade = calculate_grade(average)
    
    print("\n===== Report Card =====")
    print(f"Student Name: {student['name']}")
    print("-" * 30)
    print(f"{'Subject':<10}{'Marks':>10}")
    for subject, mark in student['marks'].items():
        print(f"{subject:<10}{mark:>10}")
    print("-" * 30)
    print(f"{'Total':<10}{total:>10}")
    print(f"{'Average':<10}{average:>10.2f}")
    print(f"{'Grade':<10}{grade:>10}")
    print("-" * 30)
report_card()

#MiniProject3
cart = []
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    cart.append(product)
    print(" Product added to cart!")

def remove_product():
    name = input("Enter product name to remove: ")
    
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(" Product removed!")
            return
    
    print(" Product not found")


def display_cart():
    if not cart:
        print("🛒 Cart is empty")
        return
    
    print(" Your Cart:")
    print("-" * 40)
    print(f"{'Name':<10}{'Price':<10}{'Qty':<5}{'Total':<10}")
    print("-" * 40)
    
    for item in cart:
        total = item["price"] * item["quantity"]
        print(f"{item['name']:<10}{item['price']:<10}{item['quantity']:<5}{total:<10}")
    
    print("-" * 40)


def total_bill():
    total = sum(item["price"] * item["quantity"] for item in cart)
    print(f" Total Bill: ₹{total}")

while True:
    print("\n===== Shopping Cart Menu =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Total Bill")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        total_bill()
    elif choice == "5":
        print(" Exiting cart system")
        break
    else:
        print(" Invalid choice")


#MiniProject4
users = {
    "admin": "1234",
    "ravi": "pass123",
    "sita": "welcome"
}
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users:
        if users[username] == password:
            print(" Login Successful!")
        else:
            print(" Incorrect Password")
    else:
        print(" Username not found")
print("===== Login System =====")
login()
#MiniProject5

visitors = set()

# Take number of entries
n = int(input("Enter number of visitors: "))

# Input visitor names
for i in range(n):
    name = input(f"Enter visitor {i+1} name: ")
    visitors.add(name)   # Set automatically ignores duplicates

# Display results
print("Unique Visitors:")
for visitor in visitors:
    print(visitor)

print("Total Unique Visitors:", len(visitors))

# 6.String Formatter Tool
# Concepts: String Formatting
# 👉 Build a formatting utility.
# Requirements:
# Input name and product
# Display formatted sentence
# Show padded output (left, right, center)?
 
# Taking input
name = input("Enter your name: ")
product = input("Enter a product: ")
sentence = f"Hello {name}, thank you for purchasing {product}!"
print("Formatted Sentence:")
print(sentence)
width = 50
 
print("Padded Output:")
print("Left Align :")
print(sentence.ljust(width, '-'))#here l for left
print("Right Align :")
print(sentence.rjust(width, '-'))# here r for right
print("Center Align :")
print(sentence.center(width, '-'))# here centre
 
# 7. Bank Account System
# Concepts: Functions, Dictionary
# 👉 Simulate bank operations.
# Requirements:
# Create account (name, balance)
# Deposit money
# Withdraw money
# Check balance?
 
# Dictionary to store account details
account = {}
 
# Function to create account
def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    account["name"] = name
    account["balance"] = balance
    print(" Account created successfully!")
 
# Function to deposit money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        account["balance"] += amount
        print(f" Deposited ₹{amount}")
    else:
        print(" Invalid amount")
 
# Function to withdraw money
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f" Withdrawn ₹{amount}")
    else:
        print(" Insufficient balance")
 
# Function to check balance
def check_balance():
    print(f" Account Holder: {account['name']}")
    print(f" Balance: ₹{account['balance']}")
 
# Menu-driven program
while True:
    print("\n===== Bank Menu =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print(" Thank you for using our bank system!")
        break
    else:
        print( "Invalid choice, try again.")
 
# 8.voting system
# Voting System
# Concepts: Dictionary, Loop
# 👉 Count votes for candidates.
# Requirements:
# Store candidates and votes
# Add vote
# Display winner?
votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}
 
def cast_vote():
    print("\nCandidates:")
    for candidate in votes:
        print(candidate)
    choice = input("Enter candidate name to vote: ")
    if choice in votes:
        votes[choice] += 1
        print(" Vote casted successfully!")
    else:
        print(" Invalid candidate")
def show_results():
    print(" Vote Count:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
 
def show_winner():
    winner = max(votes, key=votes.get)
    print(f" Winner is {winner} with {votes[winner]} votes!")
 
while True:
    print("\n===== Voting Menu =====")
    print("1. Cast Vote")
    print("2. Show Results")
    print("3. Show Winner")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        cast_vote()
    elif choice == "2":
        show_results()
    elif choice == "3":
        show_winner()
    elif choice == "4":
        print(" Exiting voting system")
        break
    else:
        print(" Invalid choice")
 
# 9.course enrollment system
# Concepts: List + Dictionary
# 👉 Manage student enrollments.
# Requirements:
# Add student with course list
# Update courses
# Display student details?
# Dictionary to store students and their courses
students = {}
 
def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma-separated): ").split(",")

    courses = [course.strip() for course in courses]
    students[name] = courses
    print(" Student added successfully!")
 
 
def update_courses():
    name = input("Enter student name: ")
    if name in students:
        print(f"Current courses: {students[name]}")
        action = input("Add or Remove course? (add/remove): ").lower()
        if action == "add":
            course = input("Enter course to add: ")
            students[name].append(course)
            print(" Course added!")
        elif action == "remove":
            course = input("Enter course to remove: ")
            if course in students[name]:
                students[name].remove(course)
                print(" Course removed!")
            else:
                print(" Course not found")
        else:
            print(" Invalid action")
    else:
        print(" Student not found")
 
 
def display_students():
    if not students:
        print("No student records found.")
    else:
        print(" Student Details:")
        for name, courses in students.items():
            print(f"{name}: {', '.join(courses)}")
while True:
    print("\n===== Course Menu =====")
    print("1. Add Student")
    print("2. Update Courses")
    print("3. Display Students")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_courses()
    elif choice == "3":
        display_students()
    elif choice == "4":
        print(" Exiting system")
        break
    else:
        print(" Invalid choice")
 
#MiniProject10
def convert_number(num):
    print(" Number Conversions:")
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")

def format_number(num):
    print(" Formatted Number:")
    print(f"With commas: {num:,}")

def scientific_notation(num):
    print("\n🔬 Scientific Notation:")
    print(f"{num:.2e}")
while True:
    print("\n===== Number Utility Menu =====")
    print("1. Convert Number")
    print("2. Format Number")
    print("3. Scientific Notation")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ["1", "2", "3"]:
        num = int(input("Enter a number: "))
        
        if choice == "1":
            convert_number(num)
        elif choice == "2":
            format_number(num)
        elif choice == "3":
            scientific_notation(num)
    
    elif choice == "4":
        print(" Exiting tool")
        break
    else:
        print(" Invalid choice")
