def solution(A):
    # Write your code in Python 3.8.10
    if len(A)==1 and A[0]<1:
        return 1
    elif len(A)==1 and A[0]>=1:
        return A[0]+1     
    s=[]
    for n in range(0,len(A)-1):
        if abs(A[n+1]-A[n])>=2 and A[n]>0 and A[n+1]>0:
            s.append(min(A[n],A[n+1])+1)
        elif A[n]<=0 and A[n+1]<=0:
            s.append(1)
        elif A[n]<=1 and A[n+1]<=1:
            s.append(2)
        elif (A[n]<=0 and A[n+1]>1) or (A[n]>1 and A[n+1]<=0):
            s.append(1)

    s.sort()
    t=[]
    [t.append(x) for x in s if x not in t]
    print(t)
    setT=set(t)
    A_Set=set(A)
    setC=setT.difference(A_Set)
    final=list(setC)
    print(final)
    if len(final)==0:
        return max(A)+1
    elif len(final)==1:
        return final[0]
    elif len(final)>1:
        return min(final)

if __name__=='__main__':
    inputA= [1,-2,-3]
    print("La Solucion es: ",solution(inputA))





    