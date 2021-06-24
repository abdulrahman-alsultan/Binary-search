def binary(list, l, r, v):
    if r < l:
        return -1
    else:
        mid = l + (r - l)
        if list[mid] == v:
            return mid
        if list[mid] > v:
            return binary(list, l, mid - 1, v)
        else:
            return binary(list, mid + 1, r, v)


arr = [2, 3, 4, 10, 40]
x = 10

result = binary(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")