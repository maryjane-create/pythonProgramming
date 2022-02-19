rock="rock"
paper="paper"
scissors="scissors"
playerCount=0
player1=0
player2=0

while playerCount<=5:

 user1= input("enter rock paper or scissors")
 user2=input("enter rock paper or scissors")
 if (user1 == "rock" and user2 == "scissors"): print("player two wins")
 player2 = player2 + 1
 if (user1 == "scissors" and user2 == "rock"): print("player two wins")
 player1 = player1 + 1

# elif(user1=="scissors" and user2=="rock"):print("player one wins")
# player2=player2+1
 if(user1=="paper" and user2=="rock"):print("player one wins")
 player1=player1+1
 if (user1 == "rock" and user2 == "paper"): print("player two wins")
 player2 = player2 + 1

# elif(user1=="rock" and user2=="paper"):print("player two wins ")
 if(user1=="scissors" and user2=="paper"):print("player one wins")
 player1=player1+1
 if (user1 == "paper" and user2 == "scissors"): print("player two wins")
 player2 = player2 + 1
# elif(user1=="paper" and user2=="rock"):print("player two wins ")



 playerCount=playerCount+1
 print(player1, player2)


    # player1n=input("enter number")
    # player1n=int (player1n)
    #
    # if(player1n<49):player1=player1+1
    # if(player1n>49):player2=player2+1
    # playerCount= playerCount+1
    #
    # print("number for player one is ", player1, "number of player two is ", player2)