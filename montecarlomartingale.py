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
blown=0
def martingale(bal,bet,Nbet):
    newBal = bal
    n = 0
    newBet=bet
    cntX = []
    balY = []
    while newBal - newBet >= 0 and n < Nbet:
        n += 1
        if diceRoll():
            newBal = newBal + newBet
            newBet=bet
        else:
            newBal = newBal - newBet
            newBet=newBet*2

        cntX.append(n)
        balY.append(newBal)
    if(n<Nbet):
        global blown
        blown+=1
    plt.plot(cntX, balY)

cnt=0
total=100
while cnt < total:
    martingale(10000,100,1000)
    cnt+=1
plt.xlabel('number of bets')
plt.ylabel('balance')
print("blown rate :",blown/total*100)
plt.show()