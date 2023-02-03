
import math

def getMBC(sAB,sBC):
    angle=0
    AB=float(sAB)
    BC=float(sBC)
    #Pythagoras Theorem
    AC=math.sqrt(AB**2+BC**2)
    MC=AC/2
    #Trigonometric basics
    alpha=math.atan(AB/BC)
    #Cosine rule
    MB=math.sqrt( BC**2+MC**2-2*(BC*MC)*math.cos(alpha) )
    #Sine rule
    theta=math.asin( MC*(math.sin(alpha)/MB) )
    #Degrees conversion
    angle=math.degrees(theta)
    return round(angle)

if __name__ == '__main__':
    AB = input()
    BC = input()
    import time
    start_time = time.time()
    print(str(getMBC(AB,BC))+"\°")
    print("--- %s seconds ---" % (time.time() - start_time))