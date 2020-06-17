def gcd(a,b):
    while((a%b)>0):
        gcd=a%b
        a=b
        b=gcd
    return b

def lcm(a,b):
    return (a*b)/gcd(a,b)


arr=[]
num=int(input("Enter size: "))
print("Enter Elements: ")
for i in range(num):
   ele=int(input()) 
   arr.append(ele)
temp=arr[0]
for i in range(num):
    temp=lcm(arr[i],temp)
print("LCM =",int(temp))