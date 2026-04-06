


# task1

s1 = Student("Asha", 1, "CSE", 60000)

s2 = Student("Ravi", 2, "ECE", 40000)

f1 = Faculty("Dr. Rao", 101, 50000)

tf1 = TempFaculty("Dr. Singh", 102, 35000, "6 months")


print(s1.__dict__)

print(s2.__dict__)

print(f1.__dict__)

print(tf1.__dict__)


# task2

# Create objects

s1 = Student("Asha", 1, "CSE", 60000)

s2 = Student("Ravi", 2, "ECE", 40000)

f1 = Faculty("Dr. Rao", 101, 50000)

tf1 = TempFaculty("Dr. Singh", 102, 35000, "6 months")

for user in [s1, s2, f1, tf1]:

    print(user.get_details())

#8 final challenge

users = [

    Student("Asha", 1, "CSE", 60000),

    Student("Ravi", 2, "ECE", 40000),

    Faculty("Dr. Rao", 101, 50000),

    TempFaculty("Dr. Singh", 102, 35000, "6 months")

]

print("---- All User Details ----")

details = list(map(lambda u: u.get_details(), users))

for d in details:

    print(d)

    print("\n---- Sorted by User ID ----")

sorted_users = sorted(users, key=lambda u: u.get_details())

for u in sorted_users:

    print(u.get_details())

    print("\n---- Only Students ----")

students = list(filter(lambda u: isinstance(u, Student), users))

for s in students:

    print(s.get_details())

    print("\n---- High Salary Faculty ----")

high_salary = list(filter(lambda u: hasattr(u, 'salary') and u.salary > 40000, users))

for h in high_salary:

    print(h.get_details())

    student_fees = list(map(lambda s: s.fees, students))

total_fees = reduce(lambda x, y: x + y, student_fees)

print("\nTotal Student Fees:", total_fees)

faculty = list(filter(lambda u: hasattr(u, 'salary'), users))

salaries = list(map(lambda f: f.salary, faculty))

total_salary = reduce(lambda x, y: x + y, salaries)

print("Total Faculty Salary:", total_salary)
 
# task 3 sorting

class Student: 

    def __init__(self, name, fees):

        self.name = name

        self.fees = fees

    def __repr__(self):

        return f"{self.name} - {self.fees}"


class Faculty:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

    def __repr__(self):

        return f"{self.name} - {self.salary}"


# ✅ Create lists OUTSIDE the class

students = [

    Student("Asha", 60000),

    Student("Ravi", 40000),

    Student("Neha", 80000)

]

faculty = [

    Faculty("Dr. Rao", 50000),

    Faculty("Dr. Kumar", 25000),

    Faculty("Dr. Singh", 35000)

]

#  Sorting

students.sort(key=lambda x: x.fees)

print("Students sorted by fees:", students)

faculty.sort(key=lambda x: x.salary)

print("Faculty sorted by salary:", faculty)


# task 4

# Using existing students list

names = list(map(lambda s: s.name, students))

print("Student Names:", names)

# task5

high_fee_students = list(filter(lambda s: s.fees > 50000, students))

high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("High Fee Students:", high_fee_students)

print("High Salary Faculty:", high_salary_faculty)


# task6 reduce

from functools import reduce

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees Collected:", total_fees)

print("Total Faculty Salary:", total_salary)

# task7

# Task 7: Higher Order Functions


class Student:

    def __init__(self, name, age, grade):

        self.name  = name

        self.age   = age

        self.grade = grade

    def get_details(self):

        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):

        return self.grade >= 50


def process_users(users, func):

    return list(map(func, users))


# Sample students

students = [

    Student("siri", 20, 85),

    Student("bhavya",   22, 45),

    Student("Divya", 21, 78),

    Student("sneha", 23, 38),

    Student("kajal",   20, 92),

]

# Get details of all students

print("All Student Details:")

details = process_users(students, lambda s: s.get_details())

for detail in details:

    print(" ", detail)

# Get names of all students

print("\nAll Student Names:")

names = process_users(students, lambda s: s.name)

for name in names:

    print(" ", name)

# Get passing students (grade >= 50)

print("\nPassing Students:")

passing = list(filter(lambda s: s.is_passing(), students))

passing_details = process_users(passing, lambda s: s.get_details())

for detail in passing_details:

    print(" ", detail)

# Get grades of all students

print("\nAll Grades:")

grades = process_users(students, lambda s: s.grade)

for grade in grades:

    print(" ", grade)
 
# users.py

class User:

    def __init__(self, name, id):

        self.name = name
self.id = id


class Student(User):

    def __init__(self, name, id, dept, fees):

        super().__init__(name, id)  # reuse parent constructor

        self.dept = dept

        self.fees = fees


class Faculty(User):

    def __init__(self, name, id, salary):

        super().__init__(name, id)  # reuse parent constructor

        self.salary = salary


class TempFaculty(Faculty):

    def __init__(self, name, id, salary, duration):

        super().__init__(name, id, salary)  # reuse Faculty constructor

        self.duration = duration


        # task2

from abc import ABC, abstractmethod


# Abstract Base Class

class AbstractUser(ABC):

    @abstractmethod

    def get_details(self):

        pass


# child class

class User(AbstractUser):

    def __init__(self, name, id):

        self.name = name
self.id = id


def get_details(self):

        return f"User: {self.name}, ID: {self.id}"


class Student(User):

    def __init__(self, name, id, dept, fees):

        super().__init__(name, id)

        self.dept = dept

        self.fees = fees

    def get_details(self):

        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):

    def __init__(self, name, id, salary):

        super().__init__(name, id)

        self.salary = salary

    def get_details(self):

        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):

    def __init__(self, name, id, salary, duration):

        super().__init__(name, id, salary)

        self.duration = duration

    def get_details(self):

        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"
    
 