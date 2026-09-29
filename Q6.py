n=int(input("enter no :"))
arr=[]

for i in range(n):
    x=int(input("enter no :"))
    arr.append(x)

print(arr)

uni=[]
uni.append(arr[0])
for j in range(1,len(arr)):
    
    if arr[j] not in uni:
        uni.append(arr[j])

print(uni)

