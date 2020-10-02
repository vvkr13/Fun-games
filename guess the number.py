import random
print("-----WELCOME TO ' GUESS THE NUMBER GAME ' ---------------")
while True:
    n = int(input("ENTER CHANCES"))
    if n < 6:
        break
    else:
        print("you cannot more than 5 chances ")
x = random.randint(1, 20)
print("GUESS THE NUMBER IN BETWEEN 1 TO 20")
print(f"YOU'VE GOT {n} CHANCES TO GUESS")
i = 1
while i <= n:
    play=int(input("GUESS THE NUMBER:"))
    if play == x:
        print(f"YOU GUSSED IT RIGHT  {i}th attempt")
        break
    else:
        print(f"TRY AGAIN ! Reamining {5 - i} attempts")
        if play > x:
            print("the number is lesser than ", play)
        else:
            print("the number is bigeer than ", play)
    i = i + 1
print("-----------------------------------")
if x == play:
    print("you won")
else:
    print("you lost and the number is:", x)
