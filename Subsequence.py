def isSubsequence(s,t):
    k = 0
    if s =="":
        return True
    
    for i in range(len(t)):
        if t[i] == s[k]:
            k+=1
        if k == len(s):
            return True

    return False

print(isSubsequence('abc', 'ahbgdc'))