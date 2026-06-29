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



#We can  use the append() function to add elements to the end of the list 

numbers.append(6)
print(numbers)

# Useful Functions

arr = list(map(int, input("Enter numbers of the array: ").split()))

if arr:
    print("The array is :", arr)
    print("The length of the array is :", len(arr))
    print("The maximum value is :", max(arr))
    print("The minimum value is :", min(arr))
    print("The sum of the array is :", sum(arr))
else:
    print("The array is empty ")



