def linearSearch(arr,x):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1;  

arr=[]
num=int(input("Enter size: "))
print("Enter Elements: ")
for i in range(num):
   ele=int(input()) 
   arr.append(ele)
x=int(input("Number search: "))
y=linearSearch(arr,x)
print(y)