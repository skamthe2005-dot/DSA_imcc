n=int(input("enter no :"))
arr=[]

for i in range(n):
    x=int(input("enter no :"))
    arr.append(x)

print(arr)
rev=[]
for j in range(len(arr)-1,-1,-1):
    rev.append(arr[j])

print("original array", arr)
print("reverse array",rev)