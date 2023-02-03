def fibb(n=50):
    i=0
    i_next=1
    result=0
    for x in range(n):
            result=i+i_next
            i=i_next
            i_next=result
    return result
print(fibb())
print(fibb(20))
