import random
print("**WELCOME**")
print(" ||ROCK PAPER SCISSORS|| ")
name=input("Enter your NAME:")
x=["rock","paper","scissors"]
maxscore=3
computerscore=0
playerscore=0
while playerscore!=maxscore and computerscore!=maxscore:
  playerchoice=input("ENTER rock paper scissors:").lower()
  computerchoice=random.choice(x)

  if playerchoice in x:
    if playerchoice==computerchoice:
      print("TIE!")
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="rock" and computerchoice=="paper":
      computerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="rock" and computerchoice=="scissors":
      playerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="paper" and computerchoice=="scissors":
      computerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="paper" and computerchoice=="rock":
      playerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="scissors" and computerchoice=="rock":
      computerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
    elif playerchoice=="scissors" and computerchoice=="paper":
      playerscore+=1
      print("computer score:",computerscore,"playerscore: ",playerscore)
      print('*'*20)
  else:
    print("check spell")
if playerscore==maxscore:
  print("-----------------------------------------")
  print(f"{name} WON THE GAME")
else:
  print("----------------------------------")
  print(f"{name} LOST THE GAME")
