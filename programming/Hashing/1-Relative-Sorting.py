"""
https://practice.geeksforgeeks.org/problems/relative-sorting/0

"""

for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = dict()
    for e in a:
        if e in m:
            m[e]+=1
        else:
            m[e]=1
    ans = []
    for e in b:
        if e in m:
            t = [e for j in range(m[e])]
            ans+=t
            m.pop(e)

    k = []
    for e in m:
        k+=[e for j in range(m[e])]
    ans+=sorted(k)
    for a in ans:
        print(a, end=" ")
    print()
