# you have to count the number of valleys user crosses during the journey 
# ( how many times he reurned to the sea level between the start and end point)
def countingValleys(n, s):
    v=0
    sea = True
    count = 0
    for i in range(n):
        if s[i] == 'U':
            v += 1
        if s[i] == 'D':
            v -= 1
        if v == 0:
            sea = True
        if v < 0 and sea == True:
            count += 1
            sea = False
    print(count)

countingValleys(10, "UDUUUDUDDD")


# UDUUUDUDDD   ------ 0
#      /\/\
#     /    \
# _/\/      \_

# UDDDUDUU     ------  1

# _/\      _
#    \    /
#     \/\/