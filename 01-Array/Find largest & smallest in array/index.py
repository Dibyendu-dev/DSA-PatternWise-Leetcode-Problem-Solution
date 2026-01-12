def findMinMax(arr):
    n = len(arr)
    maxi = arr[0]
    mini = arr[0]

    for i in range(0,n):
        if arr[i] < mini:
            mini = arr[i]
        elif arr[i] > maxi:
            maxi = arr[i]
        
    return [mini, maxi]

p =findMinMax([5,3,9,0,5,4])
print(f"min, max are",p)