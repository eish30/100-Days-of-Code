from random import randint
print("Ready to challenge the computer for a Rock Paper Scissors game?")
ch1 = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors-"))
ch2 = randint(0,2)
while True:
    if ch1==0:
        if ch2==0:
            print("Computer chose rock. It's a draw!")
            ch1 = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors-"))
            ch2 = randint(0,2)
        elif ch2==1:
            print("Computer chose paper. It wins! Better luck next time....")
            break
        elif ch2==2:
            print("Computer chose scissors. You win!!!")
            break
    elif ch1==1:
        if ch2==0:
            print("Computer chose rock. You win!!!")
            break
        elif ch2==1:
            print("Computer chose paper. It's a draw!")
            ch1 = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors-"))
            ch2 = randint(0,2)
        elif ch2==2:
            print("Computer chose scissors. It wins! Better luck next time....")
            break
    elif ch1==2:
         if ch2==0:
            print("Computer chose rock. It wins! Better luck next time....")
            break
         elif ch2==1:
            print("Computer chose paper. You win!!!")
            break
         elif ch2==2:
            print("Computer chose scissors. It's a draw!")
            ch1 = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors-"))
            ch2 = randint(0,2)
    else:
        print("You typed an invalid number, you lose!")