def rotation_rr(arr,k,d):
    for i in range(d):
        temp=arr[k-1]
        for j in range(k-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=temp   

def rotation_lr(arr,k,d):
    n=len(arr)
    for i in range(d):
        temp=arr[k]
        for j in range(k,n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp                  

arr=[]
num=int(input("Enter Size: "))
print("Enter Elements: ")
for i in range(num):
    ele=int(input())
    arr.append(ele)
num_of_rotation=int(input("Enter number of rotations: "))  
l=len(arr)  
l1=int(l/2)
rotation_rr(arr,l1,num_of_rotation) 
rotation_lr(arr,l1,num_of_rotation)
print("Half Rotation of Array first right then left: ")
print(*arr)  