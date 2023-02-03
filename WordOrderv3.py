class Count_x:
    def __init__(self):
        self.myList=[]
        self.myCount=0

def count_and_places(listA,lenA,itemA):
    obj=Count_x()
    ind=[]
    count=0
    for x in range(lenA):
        if listA[x]==itemA:
            count+=1
            ind.append(x)
    listB=list(listA)
    deleted=0
    if count>1:
        for x in range(1,len(ind),1):
            listB.pop(ind[x]-deleted)
            deleted+=1
    obj.myCount=count
    obj.myList=listB
    return obj

if __name__=='__main__':
    n=int(input())
    l=list()
    for i in range(n):
        newWord=input()
        l.append(newWord)
    g=list(l)
    i=0
    c=0
    h=list()
    while True:
        tmp=count_and_places(g,len(g),g[i])
        g=tmp.myList
        h.append(tmp.myCount)
        i+=1
        if i+1>len(g):
            break

    print(len(h))
    string=" ".join([str(item) for item in h])
    print(string)