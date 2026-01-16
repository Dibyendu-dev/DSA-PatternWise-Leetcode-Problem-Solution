def is_palindrome(str):
    if len(str) <=1:
        return True
    n = len(str)
    mid = n // 2

    oddlength = expand(str,mid,mid)
    evenlength = expand(str,mid-1,mid)

    return oddlength == n or evenlength == n

def expand(str,left,right):
    while left >= 0 and right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1
    return right - left - 1

p = is_palindrome("madam")
print(p)