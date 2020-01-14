''' The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain? '''

# Solution

def chainCount(n):
    count = 1
    while n > 1:
        if n%2 != 0:
            n = n*3 +1
        else:
            n = n//2
        count += 1
    return (count)

largestChain = 0
starting_number = 0
for n in range(1000000):
    count = chainCount(n)
    if count > largestChain:
        largestChain = count
        starting_number = n
    # print(n,count)


print(" largest chain :",largestChain,'\n','starting number :',starting_number)