d={'B':"BattleShip",'C':"Cruiser",'D':'Destroyer','F':'Frigate'}
t=int(input())
for i in range(t):
    s=input().upper()
    print(d.get(s))