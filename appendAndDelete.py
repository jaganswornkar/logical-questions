# s = "hackerhappy"
# t = "hackerrank"
# k = 9
# for ops_left in reversed(range(1, k + 1)):
#     if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
#         break
#     s = s[:-1]
# print "Yes" if len(t) - len(s) <= ops_left else "No"


s="hackerhappy"
t="hackerrank"
k=9

def me(s,t,k):
    l=0
    if len(s)<len(t):
        l=len(s)
    else:
        l=len(t)
    
    common = ''
    differ = ''
    for i in range(l):
        if( s[i] == t[i] ):
            common += s[i]
        else:   
            differ = t[i:]
            break
    else:
        differ = t[i+1:]

    append_len = len(differ)

    copy_s = s
    for j in range( k - append_len ):
        copy_s = copy_s[:-1]
        k -= 1
        if len(copy_s) < len(common):
            append_len += 1
        if ( k <= append_len ):
            break
    for a in range(k):
        if len(copy_s) >= len(t):
            break
        else:
            copy_s += t[len(copy_s)]
    if copy_s == t:
        return "Yes"
    else:
        return "No"

print(me(s,t,k))