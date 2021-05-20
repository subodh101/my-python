# https://algodaily.com/challenges/reverse-a-string/python
# not allowed to use [::-1]

def reverse_string(str1):
    # fill this in
    ans = ""
    for c in str1:
        ans = c + ans

    return ans


print(reverse_string("12345"))
print(reverse_string("123456"))
