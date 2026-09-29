n=int(input("enter no :"))
arr=[]

for i in range(n):
    x=int(input("enter no :"))
    arr.append(x)


for j in range(len(arr)):
    mini=j
    for k in range(j+1,len(arr)):
        if arr[k]<arr[mini]:
            mini=k
            arr[mini],arr[j]=arr[j],arr[mini]

print("smallest=",arr[0])
print("2nd smallest=",arr[1])
print("largest",arr[-1])
print("2nd largest",arr[-2])




