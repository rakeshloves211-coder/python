
#TASK1:

def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role.title()
    }
 
users = [
    create_user("Rakesh", 24, "devops"),
    create_user("Manoj", 26, "frontend"),
    create_user("Venkat", 28, "backend"),
]
 
for user in users:
    print(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}")



#TASK2:


def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average
 
total, avg = calculate_total(25, 30, 35, 40, 45, 50)
print(f"\nTotal: {total}, Average: {avg}")



#TASK3:

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")
 
print("\nSystem Config:")
system_config(mode="debug", version=1.0, max_retries=3, timeout=30)


#TASK4:

def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0:
        return 1
    return n * factorial(n - 1)
 
print("\nFactorial Results:")
for n in [0, 3, 9, -2]:
    print(f"  factorial({n}) = {factorial(n)}")


#TASK5:

def square_generator(n):
    for i in range(n):
        yield i*i
 
gen = square_generator(5)
lst = [i*i for i in range(5)]
 
print(type(gen))
print(type(lst))


#TASK6:

print("\nDivision Program:")
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid numbers")
finally:
    print("Program Completed")



#TASK7:

users = [

    {"name": "Rakesh",   "age": 26, "role": "Developer"},

    {"name": "Manoj",   "age": 34, "role": "Devops"},

    {"name": "Krishna",   "age": 28, "role": "Python"},

    {"name": "Kmaal", "age": 40, "role": "java"},

    {"name": "Naveen",    "age": 25, "role": "quality analyst"},

]
 
file = open("team_data.txt", "w")
 
for user in users:

    line = "Name: " + user["name"] + ",  Age: " + str(user["age"]) + ",  Role: " + user["role"] + "\n"

    file.write(line)
 
file.close()

print("team_data.txt has been created and data is written!\n")
 
file = open("team_data.txt", "r")
 
print("Contents of team_data.txt :")

print("=" * 25)
 
content = file.read()

print(content)
 
file.close()
 
print("=" * 25)

print("Is the file closed? :", file.closed)