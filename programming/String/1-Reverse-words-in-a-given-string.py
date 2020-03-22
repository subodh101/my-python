"""
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
"""

for i in range(int(input())):
    x = str(input())
    if "." in x:
        x = x.split(".")[::-1]
        x = ".".join(x)
    print(x)
