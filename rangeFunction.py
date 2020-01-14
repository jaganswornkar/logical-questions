def Range(f, i=None, diff=None):
    initial = None
    final = f
    if i:
        initial = f
        final = i
    List = []
    i = initial or 0
    while i < final:
        List.append(i)
        i += diff or 1
    return List

# for i in Range(1,10,1):
#     print(i)

