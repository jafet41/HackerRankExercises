from itertools import groupby

def getGroups(str):
    keys=[]
    groups=[]
    for k, g in groupby(str):
        keys.append(k)
        groups.append(list(g))
    lengths=[len(x) for x in groups]
    return [keys, lengths]

def formatting(inputP):
    res=getGroups(inputP)
    output=""
    for x in range(len(res[0])):
        output+="("
        output+=str(res[1][x]) +", "+str(res[0][x])
        output+=") "
    output.rstrip()
    return output

if __name__=='__main__':
    input1=input()
    print(formatting(input1))