# Sum of array with sutracting each index

li = [1,5,7,8,10]
add = sum(li)
arr1 = []
print("sum is", add)
for i in range(len(li)):
    a = add - li[i]
    arr1.append(a)

print(arr1)