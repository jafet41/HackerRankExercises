if __name__=='__main__':
    n=int(input())
    l=list()
    for i in range(n):
        newWord=input()
        l.append(newWord)
    counts = [l.count(x) for x in l]
    print(counts)
    mySet=set(l)
    print(len(mySet))
    str1=""
    for x in range(len(mySet)):
        str1+=str(counts[x])+" "
    print(str1)