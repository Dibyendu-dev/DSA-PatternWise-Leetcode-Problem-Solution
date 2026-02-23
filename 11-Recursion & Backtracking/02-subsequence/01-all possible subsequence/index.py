def findSubsequences(curr, arr, subArr, res):
    if curr == len(arr):
        res.append(subArr.copy())
        return

    #  Include the current element in the subsequence
    subArr.append(arr[curr])

    # Recurse to the next element
    findSubsequences(curr + 1, arr, subArr, res)

    # Backtrack: Remove the current element and
    # explore the next possibility
    subArr.pop()

    #  Do not include the current element in the subsequence
    findSubsequences(curr + 1, arr, subArr, res)


if __name__ == "__main__":
    arr = [1, 2, 3]

    # Temporary list to store the 
    # current subsequence
    subArr = []

    # Resultant list to store all subsequences
    res = []

    # Call the function to find all subsequences
    # starting from index 0
    findSubsequences(0, arr, subArr, res)

    for subsequence in res:
        print(" ".join(map(str, subsequence)))