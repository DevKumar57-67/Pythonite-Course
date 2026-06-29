# Python actually does not have a built-in Array type like C, C++, or Java.

# Instead Python mainly uses Lists.

# Lists are much more powerful.

# When people say

# "Python Array"

# they usually mean

# Python List

# There is also an array module, but beginners should first master lists

#Integers data
numbers = [1,2,3,4,5]
print(numbers)

#Strings data
names = ["Alice","Bob","Charlie"]
print(names)

#Mixed data
data = [10,"Python",True,3.14]
print(data)



print(numbers[1])
print(names[1])
print(data[2])

# BY using the len() function we can find the length of the list
print(len(numbers))
print(len(names))
print(len(data))


#We canu use loops to iterate through ther list and access each element 

for num in numbers:
    print(num)



