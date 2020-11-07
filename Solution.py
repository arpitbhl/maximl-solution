tchar=26

def Max_DisChar(str, n):
    count = [0] * tchar

    for i in range(n):
        count[ord(str[i])-97] += 1

    max_dis = 0
    for i in range(tchar):
        if (count[i] != 0):
            max_dis = max_dis + 1

    return max_dis

def BruteFindSub(l):
    max=Max_DisChar(l,len(l))
    m=0
    count=0
    # Here we are checking for every substring
    res = [l[i: j] for i in range(len(l))
           for j in range(i + 1, len(l) + 1)]
    for i in range(len(res)):
        if(len(res[i])==len(set(res[i])) and len(res[i])<=max):
            if(m<len(set(res[i]))):
                m=len(set(res[i]))
    return m

# This will take less time
def FindSub(l):
    max = Max_DisChar(l, len(l))
    m = 0
    count = 0
    # here we are checking only for the max char length it will take time but will take less than first
    res=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)+1):
            if(len(l[i:j])<=max):
                res.append(l[i:j])
            else:
                break
    for i in range(len(res)):
        if (len(res[i]) == len(set(res[i])) and len(res[i]) <= max):
            if (m < len(set(res[i]))):
                m = len(set(res[i]))
    return m
str=input()
f=FindSub(str)
print(f)
