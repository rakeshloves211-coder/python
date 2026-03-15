#Bitwise Operator Tasks
#1
a=10
b=6
print(a & b)

#2
x=12
y=5
print(x | y)

#3
num = 8
print(~num)

#4
a=15
b=9
print(a^b)

#5
num = 7
print(num << 2)

#6
num = 20
print(num >> 1)

#7

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

print(num1 & num2)


#8


num3 = int(input("Enter the value of num3: "))
num4 = int(input("Enter the value of num4: "))
print(num3 ^ num4)


#STRING TASKS:

#9
a = "hi"
print(a * 4)

#10
b = "python"
print(b * 3)

#11
c = "super"
d = "man"
print(c + d)

#12
e = "hello"
f = " "
g = "world"
print(e + f + g)

#13

name = input("Enter the name: ")
print(name * 5)

#14

name1 = input("Enter the name1: ")
name2 = input("Enter the name2: ")
print(name1 + name2)


#INPUT AND TYPE CASTING TASKS

#15

name = input("Enter your name: ")
print(type(name))


#16

age = input("Enter the age: ")
age = int(age)
print(type(age))


#17

h = int(input("Enter the value of h= "))
i = int(input("Enter the value of i= "))
print(h + i)


#18

j = int(input("Enter the value of j= "))
k = int(input("Enter the value of k= "))
print((j + k) / 2)


#19

j = int(input("Enter the value of j = "))
k = int(input("Enter the value of k= "))
print(3 * j * 2 + k - 2)


#20

a = input("Enter the va;lue of a = ")
print("Before type casting: ", type(a))
a = int(a)
print("The value after type casting: ", type(a))


#UNIT DIGIT TASKS

#21

num = input("Enter the number: ")
print("The last digit of the num: ", num[-1])


#22 

num = int(input("Enter the num = "))
num = num % 10
print("The unit digit of the num = ", num)


#23

num = int(input("Enter the num = "))
num = num // 10
print("The num after removing the last digit = ", num)

 
#24

num = int(input("Enter the num = "))
num = (num //10) %10
print("The second last digit of the num = ", num)


#25

num = input("Enter the num = ")
print("The last digit of the num = ", num[-1])


#IF STATEMENT TASKS

#26

if 10>=5 :
    print("10 is greater than or equal to 5")

#27

num = int(input("Enter the num = "))
if num > 50 :
    print("The value is greater than 50")


#28

age = int(input("Enter the age = "))
if age >= 18 :
    print("The person age is greater than or equal to 18")


#29
num = 125
if num > 100:
    print("The number is greater than 100")


#30
num = 10
if num >= 0:
    print("The number is greater")


#IF ELSE TASKS

#31
num = 4
if num % 2 ==0:
    print("The number is even")
else:
    print("The number is odd")

#32

marks = int(input("Enter the marks= "))
if marks >= 35 :
    print("the person passed the exam")
else:
    print("the person got failed")


#33
num = -3
if num >=0 :
    print("The number is positive")
else:
    print("The number is negative")

#34
num = 12
if num > 10 :
    print("The number is greater than 10")
else:
    print("The number is not greater than 10")


#NESTED IF TASKS

#35

age = int(input("Enter the age= "))
height = int(input("Enter the height= "))
weight = int(input("Enter the weight= "))
if age >= 18:
    if height >=160:
        if weight >=60:
            print("The candidate is selected for the job")
else:
    print("The candidate is rejected for the job")


#36

marks = int(input("Enter the marks= "))
age = int(input("Enter the age= "))
if marks >= 60:
    if age >= 17:
        print("You are selected for the admission")
else:
    print("You are not selected for the program")


#37

age = int(input("Enter the age= "))
height = int(input("Enter the height= "))
weight = int(input("Enter the weight= "))
if age>=16:
    if height>=150:
        if weight>=50:
            print("The candidate is selected for the sports")
else:
    print("The candidate is not selected for thew program")


#MATCH STATEMENT TASKS

#38

day = int(input("Day = "))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("fridauy")
    case 6:
        print("saturday")
    case 7:
        print("sunday")



#39

number = int(input("Enter the number = "))
match number:
    case 1:
        print("red")
    case 2:
        print("blue")
    case 3:
        print("green")

    
#40

num = int(input("Enter the number = "))
match num:
     case 1:
          print("apple")
     case 2:
          print("mango")
     case 3:
          print("orange")
     case 4:
          print("banana")
          
          