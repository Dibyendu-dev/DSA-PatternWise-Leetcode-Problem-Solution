def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr,low,high):
    pivot = arr[low]
    i = low 
    j = high    
    while i < j:
        while i <= high-1 and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot and j >= low+1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr, 0, n - 1)
    
    for val in arr:
        print(val, end=" ")