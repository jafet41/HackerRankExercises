def getRealUnits(V,left,right):
	limit=min(left,right)
	realUnits=0
	for i in range(len(V)):
		if V[i]<limit:
			tmp=limit-V[i]
			realUnits+=tmp
	return realUnits

def waterUnits(A):
	#Para 2 elementos o menos
	if len(A)<=2:
		return 0
	#Mas de 3 elementos
	peeks=[A[0],A[0]]
	indexPeek_0=0
	hasDesc=False
	accumDesc=0
	accumAsc=0
	water_units=0
	valley=[]
	for i in range(0,len(A)-1):
		#Saving area in a valley
		if A[i]>A[i+1]:
			hasDesc=True
			valley.append(A[i+1])
		elif A[i]<=A[i+1] and hasDesc==True:
			aux=(peeks[0]-A[i+1]) if peeks[0]>=A[i+1] else 0
			valley.append(A[i+1])
		
		#Update right peek	
		if (i+2)<len(A) and i>=0 :
			if A[i]<A[i+1] and A[i+2]<=A[i+1]:
				peeks[1]= A[i+1]
				water_units+=getRealUnits(valley,peeks[0],peeks[1])
				valley=[]
		elif (i+1)==(len(A)-1):
			if A[i]<A[i+1] :
				peeks[1]= A[i+1]
				water_units+=getRealUnits(valley,peeks[0],peeks[1])
				valley=[]
		

		if A[i+1]>=peeks[0]:
			#Reset for new Valley
			hasDesc=False
			peeks[0]=A[i+1]
			peeks[1]=A[i+1]
	return water_units

if __name__ == '__main__':
	#[3,1,0,1,2,3,2,3,2,5,2,1,0,1,2]
	inA=[3,1,0,1,2,3,2]
	print("Ans = ",waterUnits(inA))