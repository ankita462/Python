# Time complexity : O(n)
# Auxiliary Space : O(1)

def gcd(a,b):
    while((a%b)>0):
        R=a%b
        a=b
        b=R
    return b    

def rotation_lr(arr,d):
    n=len(arr)
    r=gcd(n,d)
    for i in range(r):
        temp=arr[i]
        j=i
        while(1):
            k=j+r
            if(k>=n):
                k=k-n
            if(k==i):
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp            

arr=[]
num=int(input("Enter Size: "))
print("Enter Elements: ")
for i in range(num):
    ele=int(input())
    arr.append(ele)
num_of_rotation=int(input("Enter number of rotations: "))    
rotation_lr(arr,num_of_rotation);  
print("Left Rotation of Array: ")
print(*arr)  