CONDUCTOR1=18
CONDUCTOR2=82

posConductor1 = CONDUCTOR1
posConductor2 = CONDUCTOR2

encuentro = 0

for i in range(CONDUCTOR1, CONDUCTOR2):
    posConductor1 += 1
    posConductor2 -= 1
    if(posConductor1 == posConductor2):
        encuentro = posConductor1


print(f"Los conductores se encuentran en el km {encuentro}")