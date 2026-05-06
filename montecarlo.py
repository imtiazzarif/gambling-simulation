import matplotlib.pyplot as plt
import numpy as np
def diceRoll():
    roll = np.random.randint(1, 101)
    return roll>50
def bet(bal,bet,Nbet):
    newBal = bal
    n=0
    cntX=[]
    balY=[]
    while newBal-bet >= 0 and n < Nbet:
        n+=1
        if diceRoll():
            newBal = newBal + bet
        else:
            newBal = newBal - bet

        cntX.append(n)
        balY.append(newBal)
    plt.plot(cntX,balY)
cnt=0
while cnt < 100:
    bet(10000,100,1000)
    cnt+=1
plt.xlabel('number of bets')
plt.ylabel('balance')
plt.show()

