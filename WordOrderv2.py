class Count_x:
    def __init__(self):
        self.myList=[]
        self.myCount=0
def count_and_places(listA,lenA,itemA):
    ind=[]
    count=0
    for x in range(lenA):
        if listA[x]==itemA:
            count+=1
            ind.append(x)
    ret=Count_x()
    ret.myList=ind
    ret.myCount=count
    return ret

if __name__=='__main__':
    n=int(input())
    l=list()
    g=list()
    h=list()

    for i in range(n):
        newWord=input()
        l.append(newWord)

    for i in range(len(l)):
        g.append(count_and_places(l,len(l),l[i]).myCount)
        h.append(count_and_places(l,len(l),l[i]).myList)

    y=0
    while y<len(g):
        if len(h[y])>1:
            z=0
            lenHy=len(h[y])
            while z+1<lenHy:
                g.pop(h[y][z+1]-z-y)
                h.pop(h[y][z+1]-z-y)
                z+=1
        y+=1 
    #Sometimes outputs a wrong answer               
    print(g)
