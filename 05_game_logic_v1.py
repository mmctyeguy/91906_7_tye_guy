from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("900x550")
root.configure(background="green")
root.title("Blackjack game")


# Resize the cards
def resize_cards(card):
    # open image
    our_card_img = Image.open(card)

    # resize image
    our_card_resized = our_card_img.resize((150, 218))

    # output the card
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resized)

    # return card
    return our_card_image



# shuffle the cards
def shuffle():
    # define deck
    suits = ["diamond", "clubs", "hearts", "spades"]
    values = range(1, 14)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{suit} {value}')

    # create our players
    global dealer, player, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []

    # get the dealer card
    dealer_card = random.choice(deck)
    # remove card from deck
    deck.remove(dealer_card)
    # append card to dealer list
    dealer.append(dealer_card)
    # output card to screen

    global dealer_image
    dealer_image = resize_cards(f'cos_images/{dealer_card}.png')

    dealer_label.config(image=dealer_image)

    # get the player card
    player_card = random.choice(deck)
    # remove card from deck
    deck.remove(player_card)
    # append card to player list
    player.append(player_card)
    # output card to screen

    global player_image
    player_image = resize_cards(f'cos_images/{player_card}.png')

    player_label.config(image=player_image)

    # get the score
    score(dealer_card, player_card)
    # put number of cards left in title bar
    root.title(f"Blackjack game - {len(deck)} cards left")


def deal_cards():
    try:
        # get the dealer card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to dealer list
        dealer.append(card)
        # output card to screen

        global dealer_image
        dealer_image = resize_cards(f'cos_images/{card}.png')

        dealer_label.config(image=dealer_image)

        # get the player card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to player list
        player.append(card)
        # output card to screen

        global player_image
        player_image = resize_cards(f'cos_images/{card}.png')

        player_label.config(image=player_image)

        # put number of cards left in title bar
        root.title(f"Blackjack game - {len(deck)} cards left")
    except:
        root.title(f"Blackjack - No cards in deck")


def score(dealer_card, player_card):
    # split out card values
    dealer_card = int(dealer_card.split()[1])
    player_card = int(player_card.split()[1])

    # compare card numbers
    if dealer_card == player_card:
        score_label.config(text='tie!')
    elif dealer_card > player_card:
        score_label.config(text="Dealer wins!")
        dscore.append("x")
    else:
        score_label.config(text="Player wins!")
        pscore.append("x")


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# create frames for cards
dealer_frame = LabelFrame(my_frame, text="dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# put cards in frames
dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame, text="")
player_label.pack(pady=20)

# create score label
score_label = Label(root, text="", font=("Arial", "14"))
score_label.pack(pady=20)

# create buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("arial", "20"),
                        command=shuffle)
shuffle_button.pack(pady=20)

deal_button = Button(root, text="Get Cards", font=("arial", "20"),
                     command=deal_cards)
deal_button.pack(pady=20)

shuffle()

if __name__ == "__main__":
    root.mainloop()
