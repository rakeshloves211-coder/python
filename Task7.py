#TASK1 :



# Task 1: Encapsulation (User Class)

class User:
    def __init__(self):
        self.__user_name = None  
        self.__pwd = None    

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name  

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

u = User()
u.set_user("Rakesh", "3456")
u.register()
u.login()


# Task 2: Inheritance

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")



s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.login()
t.faculty_greet()



# Task 3: Method Overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


# Run
s = Student()
f = Faculty()

s.greet()
f.greet()


# Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Run
user = User()
user.login().greet().register()



# Task 5: Combined Real-Time System

class User:
    users_count = 0  

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Run
s1 = Student("RAKESH", "789")
f1 = Faculty("KUMAR", "234")

s1.login().greet().register()
f1.login().greet().register()

print("Total Users:", User.users_count)