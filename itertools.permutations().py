from itertools import permutations

A = input().split()
charList = []
for i in A[0]:
    charList.append(i)
charList.sort()
charList = ''.join(charList)

n = int(A[1])

data = list(permutations(charList, n))
for _ in data:
    print (''.join(_))