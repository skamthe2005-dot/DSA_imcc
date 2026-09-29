n=int(input("enter no :"))
arr=[]

for i in range(n):
    x=int(input("enter no :"))
    arr.append(x)

even=0
odd=0

for j in range(len(arr)):
    if arr[j] % 2 == 0:
        even+=1
    else:
        odd+=1

print("even no:",even)
print("odd no :",odd)