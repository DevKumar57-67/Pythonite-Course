#Comments in python 


#Python syntax
print("Hello, Pythonite")

print("This is python programming language")

#Adding sum
print(5+6)

# Variables in Python
x = 45
y = 5.6
sum = x+y

print("the sum is ", sum)

#Input/Output in python 
name= input("Enter your name: ")
print("Hello", name, "Welcomee to Python prograsmming language")

# Data Types in Python
# For finding the data type of the variable we use the type() function

x = 55.7
print("the data type is ", type(x))

#A basic Calculator in python 

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sum = x+y
diff = x-y
prod = x*y
quot = x/y 
mod = x%y

print("The sum is ", sum)
print("The difference is ", diff)
print("The product is ", prod)
print("The quotient is ", quot)
print("The modulus is ", mod)
print("The modulus is ", mod)


#Conditions in Python 
#Conditional Statements are used to perform different actions based on different conditions

#Voting Eligibility in Python 
age = int(input("Enter your age: "))
if (age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Loops in Python 
#Loops are used to execute a block of code repeatedly until a cerain condition is met.
#Loops are of two types: 
#1. For Loop
#2. While Loop

# A basic loop syntax

for i in range(5):
    print("This is a for loop", i)




    
# Functions in Python
# Functions are the blocks of code that are designed to perform a specific tasks 

def add(x, y):
    return x+y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum = add(x,y)
print("The sum is", sum)
