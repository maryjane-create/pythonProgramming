








playerCount=0
player1=0
player2=0
while playerCount<=10:
    player1n=input("enter number")
    player1n=int (player1n)

    if(player1n<49):player1=player1+1
    if(player1n>49):player2=player2+1
    playerCount= playerCount+1

    print("number for player one is ", player1, "number of player two is ", player2)