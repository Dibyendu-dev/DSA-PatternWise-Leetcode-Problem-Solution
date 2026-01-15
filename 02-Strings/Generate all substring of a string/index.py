def generate_all_substr(s):
    substr=[]
    n=len(s)

    for i in range(n):
        for j in range(i+1,n+1):
            substr.append(s[i:j])
    return substr

my_str = "madam"
all_str =generate_all_substr(my_str)
print(f"{my_str}:{all_str}")