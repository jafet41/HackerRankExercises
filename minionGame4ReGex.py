from itertools import combinations
import re

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
        subRE='(?='+s+')'
        countSub=len(re.findall(subRE,s))
        if s[0] in vowels:
            if countSub>1 and s not in toSkip:
                toSkip.append(s)
                kevinScore+=countSub
            elif countSub==1:
                kevinScore+=countSub
            elif s in toSkip:
                continue
        else:
            if countSub>1 and s not in toSkip:
                toSkip.append(s)
                stuartScore+=countSub
            elif countSub==1:
                stuartScore+=countSub
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