n=int(input("enter no :"))
arr=[]

for i in range(n):
    x=int(input("enter no :"))
    arr.append(x)

print(arr)
x=int(input("enter no you want to serach :"))
for j in range(len(arr)):
    if arr[j]==x:
        print("given no is present at",j," th position")
        break
    else:
        print("given no is not present")
        break


