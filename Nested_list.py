# print the names of second lowest scored students
_dict = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    _dict[name] = score
keys=list(_dict.keys())
keys.sort()

values=list(set(_dict.values()))
values.sort()

for i in keys:
    if (_dict[i] == values[1]):
        print(i)
