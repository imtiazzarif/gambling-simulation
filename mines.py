import numpy as np
import matplotlib.pyplot as plt
tiles_h=5
tiles_v=5
n_mines=3
opened=4
profitable=0
blown=0
total_tiles=tiles_h*tiles_v
def mines(total_t,total_m,n_open):
    p_win=1
    for i in range(0,n_open):
        p_win*=((total_t-total_m-i)/(total_t-i))
    ran=np.random.rand()
    return [p_win<ran,p_win]
def bet(balance,bet_amount,n_bets):
    bal=balance
    n=0
    global total_tiles
    global n_mines
    global opened
    global profitable
    global blown
    current_bet_amount=bet_amount
    n_x=[]
    bal_y=[]
    while bal-current_bet_amount>=0 and n<n_bets:
        n+=1
        z=mines(total_tiles,n_mines,opened)
        wl=z[0]
        multi=(1/z[1])*.965
        if wl :
            bal+=current_bet_amount*multi
        else:
            bal-=current_bet_amount
        if bal<current_bet_amount:
            current_bet_amount=bal
        else:
            current_bet_amount=bet_amount
        n_x.append(n)
        bal_y.append(bal)
    plt.plot(n_x,bal_y)
    if bal==0:
        blown+=1
    elif bal>balance:
        profitable+=1
sim=0
n_gamblers=1000
while sim<n_gamblers:
    sim+=1
    bet(100,10,1000)
plt.show()
blown/=(n_gamblers/100)
profitable/=(n_gamblers/100)
print("profitable(%) :",profitable)
print("blown (%) :",blown)
print("in loss (%) :",100-blown-profitable)
