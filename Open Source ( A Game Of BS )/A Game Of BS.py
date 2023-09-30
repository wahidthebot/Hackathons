import random
from tkinter import *

BS = None
Truth = None
randomcard = ""
bot_option = ""
root = Tk()
root.geometry('900x600')
root.resizable(0, 0)
root.configure(background='#25283D')
root.title("Truth or BS card game.")

canvas = Canvas(root, width=900, height=600, background='#25283D')
canvas.pack()
canvas.create_line(0, 300, 900, 300, fill="black", width=2)

# Both user and bot start with 5 cards
BOT_Cards = 5
USER_Cards = 5
USER = None

# Initialize USER_Coins and BOT_Coins
USER_Coins = 0
BOT_Coins = 0

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Initialize bot_choice
bot_choice = 0

# Create StringVar for dynamic labels
bot_cards_var = StringVar()
user_cards_var = StringVar()
game_over_label = None  # Declare game_over_label as a global variable

def update_card_labels():
    # Update the labels with the current card counts
    bot_cards_var.set("Bot Cards: " + str(BOT_Cards))
    user_cards_var.set("User Cards: " + str(USER_Cards))

def PlayRandomCard():
    global play_cards, BOT_Cards, USER_Cards, randomcard, fakecard, game_over_label  # Declare these as global
    play_cards = Button(root, text="Play card", padx=60, bg='#445552', command=CreateOptions)
    play_cards.pack()
    play_cards.place(x=355, y=570)

    random_rank = random.choice(ranks)
    random_suit = random.choice(suits)
    randomcard = random_rank + " of " + random_suit

    while True:
        fake_rank = random.choice(ranks)
        fake_suit = random.choice(suits)
        fakecard = fake_rank + " of " + fake_suit
        if fakecard != randomcard:
            break

    textcolor = 'black'
    color = random_suit
    if random_suit == 'Hearts':
        color = '#FF0000'  # Red
    elif random_suit == 'Diamonds':
        color = '#add8e6'  # Light Blue
    elif random_suit == "Spades":
        color = 'green'
    elif random_suit == "Clubs":
        color = 'black'
        textcolor = 'white'
    backgroundcolor = color

    button4 = Button(root, text=str(randomcard), padx=80, height=2, width=30, bg=backgroundcolor, fg=textcolor)
    button4.pack()
    button4.place(x=260, y=400)
    root.after(2000, lambda: button4.pack_forget())  # Hide the card after 2 seconds

def CreateOptions():
    global bot_choice, BS, Truth, randomcard, bot_option, game_over_label  # Declare these as global

    def set_bs():
        global USER, BOT_Cards, USER_Cards, bot_choice, bot_option
        USER = 0
        bot_choice = random.randint(0, 1)

        if bot_choice == 0:
            bot_option = "telling the truth"
        if bot_choice == 1:
            bot_option = "telling a lie"

        update_coins_and_reset()
        update_card_labels()  # Update card counts

        game_over_label.config(text="The user claims they have a " + fakecard + "\nBot claims the user is " + bot_option)
        
        PlayRandomCard()  # Add this line to play a new card

    def set_truth():
        global USER, BOT_Cards, USER_Cards, bot_choice, randomcard, bot_option, game_over_label  # Add randomcard and game_over_label to the global variables
        USER = 1
        bot_choice = random.randint(0, 1)

        if bot_choice == 0:
            bot_option = "telling the truth"
        if bot_choice == 1:
            bot_option = "telling a lie"

        update_coins_and_reset()

        # Update the label text with the new random card claim and bot's claim
        game_over_label.config(text="The user claims they have a " + randomcard + "\nBot claims the user is " + bot_option)

        update_card_labels()  # Update card counts

        if USER_Cards == 0 or BOT_Cards == 0:
            BS["state"] = DISABLED
            Truth["state"] = DISABLED
            play_cards["state"] = DISABLED
            
            if BOT_Cards > USER_Cards:
                label.config(text="TheBot Wins")
            if USER_Cards > BOT_Cards:
                label.config(text="User Wins")
            

        PlayRandomCard()  # Add this line to play a new card

    BS = Button(root, text="BS", padx=60, bg='#92374D', command=set_bs)
    BS.pack()
    BS.place(x=5, y=450)

    Truth = Button(root, text="Truth", padx=60, bg='#B1B7D1', command=set_truth)
    Truth.pack()
    Truth.place(x=740, y=450)
    
    global label
    label = Label(root, text="", font=("Arial", 18))
    label.pack()
    label.place(x=5, y=150)

    # Add the game_over_label
    global game_over_label  # Declare game_over_label as a global variable
    game_over_label = Label(root, text="", font=("Arial", 18))
    game_over_label.pack()
    game_over_label.place(x=0, y=10)

def update_coins_and_reset():
    global USER_Coins, BOT_Coins, bot_choice, BOT_Cards, USER_Cards, game_over_label  # Add game_over_label to global variables
    if USER == 1:
        if bot_choice == 1:
            BOT_Cards += 1
            USER_Cards -= 1
        else:
            USER_Cards += 1
            BOT_Cards -= 1
    else:
        if bot_choice == 0:
            USER_Cards += 1
            BOT_Cards -= 1
        else:
            BOT_Cards += 1
            USER_Cards -= 1

    if USER_Cards == 0 or BOT_Cards == 0:
        if USER_Cards > BOT_Cards:
            result_text = "User wins!"
        elif USER_Cards < BOT_Cards:
            result_text = "Bot wins!"
        else:
            result_text = "It's a tie!"

        game_over_label.config(text=result_text)
        game_over_label.place(x=370, y=50)
        
        if USER_Cards == 0 or BOT_Cards == 0:
            BS["state"] = DISABLED
            Truth["state"] = DISABLED
            play_cards["state"] = DISABLED

        BS["state"] == "disabled"
        Truth["state"] == "disabled"

UsernameUser = Label(root, textvariable=user_cards_var, bg='black', fg='white', padx=40)
UsernameUser.pack()
UsernameUser.place(x=5, y=350)
update_card_labels()


UsernameBot = Label(root, textvariable=bot_cards_var, bg='black', fg='white', padx=40)
UsernameBot.pack()
UsernameBot.place(x=5, y=250)

# Start the game by playing the first card
PlayRandomCard()

root.mainloop()
