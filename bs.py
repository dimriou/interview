arr = [1,2,3,5,7,8,9,11,22,55,66,88]

def binarySearch(arr, start, end, t):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == t:
            return mid
        else:
            if arr[mid] < t:
                return binarySearch(arr, mid + 1, end, t)
            else:
                return binarySearch(arr, start, mid - 1, t)
    else:
        return - 1


start = 0
end = len(arr) - 1
t = 66
print(binarySearch(arr, start, end, t))
