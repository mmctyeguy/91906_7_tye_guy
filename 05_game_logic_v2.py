from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("900x650")
root.configure(background="green")
root.title("Blackjack game")


# Resize the cards
def resize_cards(card):
    # open image
    our_card_img = Image.open(card)

    # resize image
    our_card_resized = our_card_img.resize((120, 198))

    # output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resized)

    # return card
    return our_card_image


# shuffle the cards
def shuffle():
    # Clear all the old cards from previous games
    dealer_label_1.config(image="")
    dealer_label_2.config(image="")

    player_label_1.config(image="")
    player_label_2.config(image="")
    player_label_3.config(image="")
    player_label_4.config(image="")
    player_label_5.config(image="")

    # define deck
    suits = ["diamond", "clubs", "hearts", "spades"]
    values = range(1, 14)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{suit} {value}')

    # create our players
    global dealer, player, dealer_spot, player_spot, pscore, dscore
    dealer = []
    player = []
    dealer_spot = 0
    player_spot = 0
    pscore = []
    dscore = []

    # shuffle 2 cards for player and dealer
    dealer_hit()
    dealer_hit()
    player_hit()
    player_hit()
    # put number of cards left in title bar
    root.title(f"Blackjack game - {len(deck)} cards left")


def dealer_hit():
    global dealer_spot
    if dealer_spot < 3:
        try:
            # get the dealer card
            dealer_card = random.choice(deck)
            # remove card from deck
            deck.remove(dealer_card)
            # append card to dealer list
            player.append(dealer_card)
            # output card to screen

            global dealer_image1, dealer_image2

            # resize and set cards in labels
            if dealer_spot == 0:
                dealer_image1 = resize_cards(f'cos_images/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image1)
                # increment dealer spot counter
                dealer_score(dealer_card)
                dealer_spot += 1
            elif dealer_spot == 1:
                dealer_image2 = resize_cards(f'cos_images/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image2)
                # increment dealer spot counter
                dealer_score(dealer_card)
                dealer_spot += 1

            # put number of cards left in title bar
            root.title(f"Blackjack game - {len(deck)} cards left")
        except:
            root.title(f"Blackjack - No cards in deck")


def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            # get the player card
            player_card = random.choice(deck)
            # remove card from deck
            deck.remove(player_card)
            # append card to player list
            player.append(player_card)
            # output card to screen

            global player_image1, player_image2, player_image3, player_image4, player_image5

            # resize and set cards in labels
            if player_spot == 0:
                player_image1 = resize_cards(f'cos_images/{player_card}.png')
                player_label_1.config(image=player_image1)
                # increment player spot counter
                player_score(player_card)
                player_spot += 1
            elif player_spot == 1:
                player_image2 = resize_cards(f'cos_images/{player_card}.png')
                player_label_2.config(image=player_image2)
                # increment player spot counter
                player_score(player_card)
                player_spot += 1
            elif player_spot == 2:
                player_image3 = resize_cards(f'cos_images/{player_card}.png')
                player_label_3.config(image=player_image3)
                # increment player spot counter
                player_score(player_card)
                player_spot += 1
            elif player_spot == 3:
                player_image4 = resize_cards(f'cos_images/{player_card}.png')
                player_label_4.config(image=player_image4)
                # increment player spot counter
                player_score(player_card)
                player_spot += 1
            elif player_spot == 4:
                player_image5 = resize_cards(f'cos_images/{player_card}.png')
                player_label_5.config(image=player_image5)
                # increment player spot counter
                player_score(player_card)
                player_spot += 1

            # put number of cards left in title bar
            root.title(f"Blackjack game - {len(deck)} cards left")
        except:
            root.title(f"Blackjack - No cards in deck")


def dealer_score(dealer_card):
    # split out card values
    dealer_card = int(dealer_card.split()[1])
    dscore.append(dealer_card)


def player_score(player_card):
    # split out card values
    player_card = int(player_card.split()[1])
    pscore.append(player_card)


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# create frames for cards
dealer_frame = LabelFrame(my_frame, text="dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# put dealer cards in frames
dealer_label_1 = Label(dealer_frame, text="")
dealer_label_1.grid(row=0, column=0, padx=20)

dealer_label_2 = Label(dealer_frame, text="")
dealer_label_2.grid(row=0, column=1, padx=20)

# put player cards in frames
player_label_1 = Label(player_frame, text="")
player_label_1.grid(row=1, column=0, padx=20)

player_label_2 = Label(player_frame, text="")
player_label_2.grid(row=1, column=1, padx=20)

player_label_3 = Label(player_frame, text="")
player_label_3.grid(row=1, column=2, padx=20)

player_label_4 = Label(player_frame, text="")
player_label_4.grid(row=1, column=3, padx=20)

player_label_5 = Label(player_frame, text="")
player_label_5.grid(row=1, column=4, padx=20)

# create score label
score_label = Label(root, text="SCORE!", font=("Arial", "14"))
score_label.pack(pady=10)

# create a button frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=10)

card_button = Button(button_frame, text="Hit Me!", font=("arial", "20"),
                     command=player_hit)
card_button.grid(row=0, column=0, padx=10)

stand_button = Button(button_frame, text="Stand", font=("arial", "20"))
stand_button.grid(row=0, column=1)

shuffle()

if __name__ == "__main__":
    root.mainloop()
