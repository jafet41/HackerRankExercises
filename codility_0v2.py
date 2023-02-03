def solution(A):
    # Write your code in Python 3.8.10
    # Wrong Solution, it doesnt work for some cases
    bajo=A[0]
    alto=A[0]

    for i in range(len(A)):
        if A[i]<=0:
            continue
        if A[i]==(bajo-1):
            bajo=A[i]
        elif A[i]==(alto+1):
            alto=A[i]
        else:
            if A[i] < (bajo-1):
                bajo=A[i]
                alto=A[i]
    if bajo==1:
        return alto+1
    else:
        return 1

if __name__=='__main__':
    inputA= [1,3,6,4,1,2]
    print("La Solucion es: ",solution(inputA))