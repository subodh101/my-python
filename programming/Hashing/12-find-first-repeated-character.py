"""
https://practice.geeksforgeeks.org/problems/find-first-repeated-character/0

"""
for i in range(int(input())):
    s = str(input().strip())
    k = set()
    ans = -1
    for c in s:
        if c not in k:
            k.add(c)
        else:
            ans = c
            break

    print(ans)
