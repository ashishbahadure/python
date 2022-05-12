# Write a binary search function which search an item in a sorted list
# The function should return the index of element to be searched in the list

a=[1,2,3,4,5]
n = int(input("Enter number"))

for i in range(0,len(a)):
    # print(a[i])
    if(n == a[i]):
        print("The number is present in the list at index ",i);
        break;
    else:
        print("The number is not present in the list")