import random

RPS_dict = {
        "R" : "Rock",
        "P" : "Paper",
        "S" : "Scissors"
        }

win = 0
while win != 1:    
    key = random.choice(list(RPS_dict))
    computer_choice = RPS_dict[key]
    user_choice = input("Enter a choice: R (Rock), P (Paper), S (Scissors): ")

    if user_choice == "R" or user_choice == "P" or user_choice == "S":
        print("\nPlayer ({}): CPU ({})".format(RPS_dict[user_choice], computer_choice))
    else:
        while user_choice != "R" and user_choice != "P" and user_choice != "S":
            print("\nInvalid input! Try again")
            user_choice = input("Enter a choice: R (Rock), P (Paper), S (Scissors): ")
            if user_choice == "R" or user_choice == "P" or user_choice == "S":
                print("\nPlayer ({}): CPU ({})".format(RPS_dict[user_choice], computer_choice))
                break

    while user_choice == key:
        print(f"\nBoth players chose {computer_choice}. It is a tie. Try again")
        user_choice = input("Enter a choice: R (Rock), P (Paper), S (Scissors): ")
        key = random.choice(list(RPS_dict))
        computer_choice = RPS_dict[key]
        if user_choice != key:
            print("\nPlayer ({}): CPU ({})".format(RPS_dict[user_choice], computer_choice))

    if user_choice == "R":
        if computer_choice == "Scissors":
            print("\nRock smashes scissors! Player wins!")
            win = 1
        
    elif user_choice == "P":
        if computer_choice == "Rock":
            print("\nPaper covers rock! Player wins!")
            win = 1

    elif user_choice == "S":
        if computer_choice == "Paper":
            print("\nScissors cuts paper! Player wins!")
            win = 1
