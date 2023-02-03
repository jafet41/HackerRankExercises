def binary_search(list_num, first_index, last_index, to_search):
    if last_index >= first_index:       
        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]
        if mid_element == to_search:
            return mid_index
        elif mid_element > to_search:
            new_position = mid_index - 1
            return binary_search(list_num, first_index, new_position, to_search)
        elif mid_element < to_search:
            new_position = mid_index + 1
            return binary_search(list_num, new_position, last_index, to_search)
    else:
        return -1

def computeHappiness(n,m,l1,A,B):
    h=0
    sortA=list(A)
    sortB=list(B)
    sortA.sort()
    sortB.sort()
    for x in l1:
        if binary_search(sortA,0,len(sortA)-1,x)>-1:
            h+=1
        if binary_search(sortB,0,len(sortB)-1,x)>-1:
            h+=-1
    return h

if __name__=='__main__':
    n,m = [int(i) for i in input().strip().split()]
    l1 = [int(k) for k in input().strip().split()]
    A = [int(j) for j in input().strip().split()]
    if len(A)!=m:
        print("Error de longitud de elementos en A")
        print(A)
    B = [int(l) for l in input().strip().split()]
    if len(B)!=m:
        print("Error de longitud de elementos en B")
        print(B)
    print(computeHappiness(n,m,l1,A,B))
