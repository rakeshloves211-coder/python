#SECTION 1:

#1
numbers = [ ]
for i in range(1 , 51):
    numbers.append(i)
print(numbers)


#2
numbers = []
for i in range(1 , 101) :
    if i % 2 == 0 :
        numbers.append(i)
print(numbers)


#3
numbers = []
for i in range(1,101):
    if i % 3 ==0:
        numbers.append(i)
print(numbers)


#4
numbers = []
for i in range(1,71):
    if i % 7 == 0:
        numbers.append(i)
print(numbers)


#5
add = 0
for i in range(1,101):
    add = add + i
print(add)

#6
for i in range(50, 0, -1):
    print(i)


#7
numbers = []
for i in range(1,101):
    if i % 3 == 0:
        numbers.append(i)
print(len(numbers))


#8
numbers = []
for i in range(1,11):
    numbers.append(i**2)
print(numbers)


#10
'''
n= int(input("Enter the value = "))
for i in range(1, n+1):
    print(n)

'''
#SECTION2:

#11

num = 1
while num <=20:
    print(num)
    num += 1


#12
'''
num = int(input("Enter the value = "))
factorial = 1
if num<= 0:
    print("Sorry")
else:
    i = 1
    for i in range(i, num+1):
        factorial = factorial * i
        i += 1
    print(factorial)
'''

#13
'''
num = int(input("Enter the number = "))
revised_num = 0
while num> 0:
    digit = num % 10
    revised_num = revised_num * 10 + digit
    num = num // 10
print(revised_num)
'''

#14
'''
num = int(input("Enter the number= "))
count = 0 
while num> 0:
    count += 1
    num = num // 10
print(count)
'''

#15
'''
user = ''
while not user == "stop":
    user = input("Enter the value: ")
    if user == "stop":
        print("Stopped")
'''

#SECTION 3:

#16
for i in range(1 , 5):
    for j in range(i):
        print("*", end="")
    print()  


#17

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()

#18
for i in range(1,6):
    for j in range(1,11):
        result = i * j
        print(result)
    print()

#19
for i in range(1,4):
    for j in range(1,4):
        print("A B C")
    print()

#20
for i in range(1,10):
    print(i, end = " ")
    if i % 3 == 0:
        print()

#STRING BASICS:

#21
name = "Hello world"
print(len(name))

#22
'''
text =input( )
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count += 1
        print(count)

'''
#23
'''
text = input( )
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i.isalpha() and i not in vowels:
        count += 1
        print(count)
'''

#24
'''
text = input( )
reversed_text = ""
for i in text:
    reversed_text = i +reversed_text
print(reversed_text)
'''


#25
'''
text = input( )
if text ==text[::-1]:
    print("The text is a palindrome")
else:
    print("The text is not a palindrome")
'''


#SECTION 5

#26
text = "rakeshvarma"
print(text[0:6])

#27
text = "rakeshvarma"
print(text[-3: ])

#28
text = "rakesh"
print(text[:: -1])

#29
'''
text = input()
print(text[1])
'''


#30
text = "rakesh"
result = text[1:-1]
print(result)


#SECTION 6

#31
numbers = [1, 2, 3, 4, 5]

total = sum(numbers)
print(total)


#32
numbers = [1, 2, 3, 4, 5]
maximum_number = max(numbers)
print(maximum_number)


#33
numbers = [1,2,3,4,5]
minimum_number = min(numbers)
print(minimum_number)


#34
numbers = [1,2,3,4,5]
length_number = len(numbers)
print(length_number)


#35
'''
fruits = ["apple", "banana", "orange"]
fruit = input()

if "apple" in fruit:
    if "banana" in fruit:
        if "orange" in fruit:
            print("It is in the list")
else:
    print("It is not in the list")

'''

#SECTION 7

#36
'''
items = []
for i in range(3):
    item = input(i +1)
    items.append(item)
print(items)
'''


#37
fruits = ["banana", "orange", "apple"]
fruits.insert(1, "kiwi")
print(fruits)


#38
fruits = ["orange", "apple", "banana"]
fruits.remove("orange")
print(fruits)


#39
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)