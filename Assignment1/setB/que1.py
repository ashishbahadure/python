# Write a program which accept an integer value n and display all prime numbers till n
num = int(input("Enter number\n"))
counter = 0;
for i in range(1,num+1):
    if(num%i == 0):
        counter=counter+1;
        print(i)
    
    


    