from xml.dom import minicompat


def great(n):
    k=n[0]
    for i in range(len(n)-1):
        if (n[i+1]>k):
            k=n[i+1]
    return k


def small(n):
    k=n[0]
    for i in range(len(n)-1):
        if (k>n[i+1]):
            k=n[i+1]
    return k


L=[12,15,25,45,8,99,200]
print(great(L))
print(small(L))
