n = int(input())
arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print("The first duplicate element is", arr[i])
            break
        else:
            print("There is no duplicates")
            break
    break
