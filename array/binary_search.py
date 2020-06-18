# Time Complexity = O(log n)

def binarySearch(arr,l,r,x):
    if(r>=l):
        mid=int(l+(r-l)/2)
        if(arr[mid]==x):
            return mid
        if(arr[mid]>x):
            r=mid-1
        else:
            l=mid+1
    return -1                

arr=[]
num=int(input("Enter size: "))
print("Enter Elements: ")
for i in range(num):
   ele=int(input()) 
   arr.append(ele)
x=int(input("Number search: "))
y=binarySearch(arr,0,num,x)
print(y)