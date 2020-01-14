from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

data = list(product(A,B))
for _ in data:
    print (_, end='')

# for i in A:
#     for j in B:
#         print ((i,j), end=' ')