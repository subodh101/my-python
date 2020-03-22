"""
https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0

"""
from itertools import permutations

for i in range(int(input())):
    x = permutations(str(input()))
    a = []
    for y in list(x):
        a.append("".join(y))
    for c in sorted(a):
        print(c, end=" ")
    print()
