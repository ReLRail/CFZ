def insertions_sort(l):
    ret = []
    for i in l:
        ret = insert(i,ret)
    return ret

def insert(e,l):
    if not len(l):
        l.append(e)
        return l
    for i in range(len(l)):
        if e < l[i]:
            l.insert(i,e)
            return l
    l.append(e)
    return l

    
l = [12, 11, 13, 5, 6] 
print(insertions_sort(l))
