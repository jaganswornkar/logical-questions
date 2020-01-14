def divisorCounter(n):
    count = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            count += 1
            # print(i)
    return count

# print('count :',divisorCounter(28))

n = 1
tn = 1
while tn > 0:
    result = divisorCounter(tn)
    if result > 500:
        print(result)
        break
    else:
        print(tn,divisorCounter(tn))

    n+=1
    tn += n

# print(divisorCounter(76576500))