n=int(input("enter no :"))
arr=[]
for i in range(n):
    num=int(input("enter a no :"))
    arr.append(num)
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]

print(sum)