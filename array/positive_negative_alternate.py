# Time Complexity: O(n) where n is number of elements in given array.
# Auxiliary Space: O(1)

def alternative_positive_negative(arr):
    

arr=[]
num=int(input("Enter Size: "))
print("Enter Elements: ")
for i in range(num):
    ele=int(input())
    arr.append(ele)  
alternative_positive_negative(arr);  
print(*arr)  