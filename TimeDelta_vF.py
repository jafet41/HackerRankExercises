#!/bin/python3
import math
import os
import random
import re
import sys
# Leap Years Helpers 
def isLeap(year):
    isL=False
    if year%4==0 and (year%100!=0 or year%400==0):
        isL=True
    return isL
def nextLeap(year):
    for i in range(8):
        if isLeap(year+i):
            return year+i
def howManyLeaps(y1,y2,m1,m2):
    leaps=0
    diff=abs(y2-y1)
    #Same year case
    if diff==0 :
        leaps=1 if isLeap(y1) and ( (m1<=2 and m2>2) or (m2<=2 and m1>2) ) else 0
        return leaps
    #Different year case
    smaller= y1 if y1<y2 else y2
    higher= y2 if y1<y2 else y1
    smaller_M= m1 if y1<y2 else m2
    higher_M= m2 if y1<y2 else m1
    if isLeap(smaller) and smaller_M<=2:
        leaps+=1
    nextYear=nextLeap(smaller+1)
    while nextYear<=higher:
        if nextYear<higher:
            leaps+=1
            nextYear=nextLeap(nextYear+1)
        elif nextYear==higher and higher_M>2:
            leaps+=1
            break
        elif nextYear==higher and higher_M<=2:
            break
    return leaps

# Complete the time_delta function below.
def time_delta(t1, t2):
    Months=['Jan','Feb','Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    Days_Moths=[31,28,31,30,31,30,31,31,30,31,30,31]
    t1_l=t1.split()
    t2_l=t2.split()
    #YEARS
    year1=int(t1_l[3])
    year2=int(t2_l[3])
    #MONTHS
    month1=Months.index(t1_l[2])+1
    month1_d=0
    for x in range(month1):
        month1_d+=Days_Moths[x]
    month2_d=0
    month2=Months.index(t2_l[2])+1
    for x in range(month2):
        month2_d+=Days_Moths[x]
    #DAYS
    day1=int(t1_l[1])
    day2=int(t2_l[1])
    #Epoch Convertion
    y1S=year1*365*86400
    m1S=month1_d*86400
    d1S=day1*86400
    y2S=year2*365*86400
    m2S=month2_d*86400
    d2S=day2*86400
    #Dates in seconds
    date1_S=y1S+m1S+d1S
    date2_S=y2S+m2S+d2S
    
    #Hrs Mins and Secs
    hh1=int(t1_l[4][:2])
    hh2=int(t2_l[4][:2])
    mm1=int(t1_l[4][3:5])
    mm2=int(t2_l[4][3:5])
    ss1=int(t1_l[4][6:8])
    ss2=int(t2_l[4][6:8])
    ss_Abs1=hh1*3600+mm1*60+ss1
    ss_Abs2=hh2*3600+mm2*60+ss2

    ss_Abs1+=date1_S
    ss_Abs2+=date2_S
    
    #Timezone
    tz1_H=int(t1_l[5][1:3])
    tz1_M=int(t1_l[5][3:])
    tz2_H=int(t2_l[5][1:3])
    tz2_M=int(t2_l[5][3:])

    tz1=tz1_H*3600+tz1_M*60
    tz2=tz2_H*3600+tz2_M*60
    tz_Diff=0

    if t1_l[5][0]=='-':
        tz1*=-1
    if t2_l[5][0]=='-':
        tz2*=-1
    ss_Abs1-=tz1
    ss_Abs2-=tz2
    ss_Final=abs(ss_Abs2-ss_Abs1)

    ss_Final+=howManyLeaps(year1,year2,month1,month2)*86400

    return str(int(ss_Final))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()