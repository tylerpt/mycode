import random

answer = input("Would you like to play a game? y/n ")

rps = {"rock":1, "paper":2, "scissors":3}

if answer == "y":
    choice = input("Choose rock, paper, or scissors: ")
    #our_choice = random.choice(["rock", "paper", "scissors"])
    our_choice = ('scissors')
    #print(choice, our_choice)
    print('i chose', our_choice)
    while choice == "rock":
        if our_choice == "paper":
            print('well i picked paper')
            break
        elif our_choice == "rock":
            print('me too')
            break
        elif our_choice == 'scissors':
            print('rock beats scissors')
            break
    while choice == "paper":
        if our_choice == "paper":
            print('me too')
            break
        elif our_choice == "rock":
            print('paper beats rock')
            break
        elif our_choice == "scissors":
            print("scissors beats paper")
            break
    while choice == "scissors":
        if our_choice == "paper":
            print("scissors beats paper")
            break
        elif our_choice == "rock":
            print("rock beats scissors")
            break
        elif our_choice == "scissors":
            print('me too')
            break