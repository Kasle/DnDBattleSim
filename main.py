import tokens as t
import matplotlib.pyplot as plt

mat = 10000
aWc = 0
bWc = 0
aWin = [0 for i in range(mat)]
bWin = [0 for i in range(mat)]

for win in range(mat):
    a = t.creature()
    b = t.creature()

    while True:
        aAtt = a.attack()
        bAtt = b.attack()

        if aAtt[0] >= b.ac:
            #print("a hit!", aAtt)
            b.hp-=aAtt[1]
        #else:
            #print("a missed!", aAtt)
        if b.hp <= 0:
            #print("a wins!")
            aWc+=1
            break
        
        if bAtt[0] >= a.ac:
            a.hp-=bAtt[1]
            #print("b hit!", bAtt)
        #else:
            #print("b missed!", bAtt)
        if a.hp <= 0:
            #print("b wins!")
            bWc+=1
            break
    aWin[win] = aWc
    bWin[win] = bWc

print(aWc/bWc)

plt.plot(aWin)
plt.plot(bWin)
plt.show()

    
    
