def isIsomorphic(s,t):

    sdict = {}
    tdict = {}

    for i,j in zip(s,t):
        if i not in sdict and j not in tdict:
            sdict[i] = j
            tdict[j] = i
        elif i not in sdict or j not in tdict or sdict[i]!= j or tdict[j] != i:
            return False
    return True

print(isIsomorphic('egg', 'add'))