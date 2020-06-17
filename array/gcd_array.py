def gcd(a,b):
    while((a%b)>0):
        gcd=a%b
        a=b
        b=gcd
    return b
       
arr=[]
num=int(input("Enter size: "))
print("Enter Elements: ")
for i in range(num):
   ele=int(input()) 
   arr.append(ele)
temp=arr[0]
for i in range(num):
    temp=gcd(arr[i],temp)
print("GCD =",temp)