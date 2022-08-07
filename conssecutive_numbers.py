def consecutive(arr):
    arr.sort()
    missing = 0
    for i in range(len(arr)-1):
        missing += arr[i+1] - arr[i] - 1
    return missing