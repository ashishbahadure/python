# Write a program which acceps % integer values and prints "Duplicates"
# if any of the values entered are duplicates otherwise it print " All Unique"
# Example Let 5 integers are 32,45,90,45,6 then output "Duplicates " to be printed

a = [1,2,3,4,1]
print(a)
k = 0
print(len(a))
for i in range(0,len(a)):
    #print("i",i)
    for j in range(i+1,len(a)):
       # print("j",j)
        if(a[i] == a[j]):
            print(a[i],"Dublicate")
            k+=1

print("i",i)
print("j",j)
print("k",k)
if(k==0):
    print("All UNIque");


    
