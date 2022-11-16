from itertools import combinations

def count1(strA,subS):
    count=0
    lenSubS=len(subS)
    for i in range(len(strA)):
        tmp=strA[i:]
        if tmp[:lenSubS]==subS:
            count+=1
    return count

def minion_game(string):
    # your code goes here
    if (not string.isupper()):
        print("Only capital letters accepted")
        return
    if len(string)>1000000:
        return

    vowels = ['A','E','I','O','U']
    stuartScore=0
    kevinScore=0
    #Calculating the Scores
    toSkip=[]

    allSubs= [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]

    for s in allSubs:
        if s[0] in vowels:
            if count1(string, s)>1 and s not in toSkip:
                toSkip.append(s)
                kevinScore+=count1(string, s)
            elif count1(string, s)==1:
                kevinScore+=count1(string, s)
            elif s in toSkip:
                continue
        else:
            if count1(string, s)>1 and s not in toSkip:
                toSkip.append(s)
                stuartScore+=count1(string, s)
            elif count1(string, s)==1:
                stuartScore+=count1(string, s)
            elif s in toSkip:
                continue

    #Getting the winner (if any)
    if stuartScore > kevinScore:
        print("Stuart "+str(stuartScore))
    elif kevinScore >stuartScore:
        print("Kevin "+str(kevinScore))
    elif kevinScore==stuartScore:
        print("Draw")


if __name__ == '__main__':
    s = input()
    import time
    start_time = time.time()
    minion_game(s)
    print("--- %s seconds ---" % (time.time() - start_time))