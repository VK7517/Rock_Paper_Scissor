import random
# mapped={'r':0,'p':1,'s':2}
choices=['r','p','s']
emojis={'r':'🪨','p':'📃','s':'✂️'}
answer={'r':'s','p':'r','s':'p'}
while(True):
    user_choice=input("Rock(r)/Paper(p)/Scissor(s): ")
    if(user_choice not in choices):
        print("Invalid Choice")
        continue
    computer_choice = random.choice(choices)
    print(f"You Choose: {emojis[user_choice]}")
    print(f"Computer Choose: {emojis[computer_choice]}")

    if(answer[user_choice]==computer_choice):
    if(answer[user_choice]==computer_choice):
    if(answer[user_choice]==computer_choice):
        print("You Won!!!!🔥🔥🔥")
    else:
        print("You Loose!")

    play=input("Want to play: (y/n) ")
    if(play=='n'):
        break