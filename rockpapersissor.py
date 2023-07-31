from random import randint

c = ["Rock", "Paper", "Scissors"]
comp_choice = c[randint(0,2)]
player_choice = 1
comp_win = 0
player_win = 0
while player_choice == 1:
    player_choice=input("Chose Rock, Paper, Scissors?\n")
    comp_choice = c[randint(0,2)]
    if player_choice == "Rock":
        if player_choice == comp_choice:
            print("Tie! Computer Chose:",comp_choice,"Player Chose:",player_choice)
            print("Score")
            print("computer win:",comp_win)
            print("Player Win:",player_win)

        elif player_choice == "Rock":
            if comp_choice == "Paper":
                print("You Lose! Computer Chose:",comp_choice,"Player Chose:",player_choice)
                comp_win+=1
                print("Score")
                print("Computer's Score:",comp_win)
                print("player's Score:",player_win)

            else:
                print("You Win! Computer chose:",comp_choice,"Player chose:",player_choice)
                player_win+=1
                print("Score")
                print("Computer win:",comp_win)
                print("Player win:",player_win)

        elif player_choice == "Scissors":
            if comp_choice == "Rock":
                print("You Lose!  Computer chose:",comp_choice,"Player chose",player_choice)
                comp_win+=1
                print("Score")
                print("Computer Win:",comp_win)
                print("Print Win:",player_win)
            else:
                print("You Win! Computer Chose:",comp_choice,"Player Chose:",player_choice)
                player_win+=1
                print("Score")
                print("Computer win:",comp_win)
                print("Player win:",player_win)
        else:
            print("Are you DUMB! Choose the correct option.")
