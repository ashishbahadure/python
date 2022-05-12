


# Write a program which print fibonacci series of number


first = 1
second = 1
num = int(input("Enter number\n"))
print(first)
print(second)
for i in range(0, num):
    third = first + second
    print(third)
    first = second
    second = third
   
    
