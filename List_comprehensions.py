x = int(input('Enter first integer input for `X` : '))
y = int(input('Enter second integer input for `Y` : '))
z = int(input('Enter third integer input for `Z` : '))
n = int(input('Enter integer input for `N` : '))

result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
                result.append([i,j,k])
print(result)

