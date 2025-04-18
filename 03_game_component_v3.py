from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import random


class StartGame:
    """
    Initial game interface (asks users the bet amount)
    """

    def __init__(self):
        """
        gets bet amount from user
        """

        self.start_frame = Frame(padx=10, pady=10, bg="#042B01")
        self.start_frame.grid()

        # strings for labels
        intro_string = "Welcome to Blackjack!"

        bet_string = "How much do you want to bet?"

        # List of labels to be made (text | font | fg)
        start_labels_list = [
            ["Blackjack", ("Arial", "16", "bold")],
            [intro_string, ("Arial", "12")],
            [bet_string, ("Arial", "12", "bold")],

        ]

        # Create labels and add them to reference list.

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               bg="#042B01", fg="#FDF4E9",
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary.
        self.choose_label = start_label_ref[2]

        # Frame so that entry box and button can be in the same row
        self.entry_area_frame = Frame(self.start_frame, bg="#042B01")
        self.entry_area_frame.grid(row=3)

        # create bet entry
        self.bet_entry = Entry(self.entry_area_frame, font=("Arial", "28", "bold"),
                               width=10, bg="#10460C", fg="#FDF4E9")
        self.bet_entry.grid(row=1, column=0, padx=10, pady=30)

        # create play button...
        self.play_button = Button(self.entry_area_frame, font=("Arial", "16", "bold"),
                                  fg="#FDF4E9", bg="#981C1E", text="Play",
                                  width=10, command=self.check_bet)
        self.play_button.grid(row=2, column=0)

    def check_bet(self):

        bet_amount = self.bet_entry.get()

        self.choose_label.config(fg="#FDF4E9", font=("Arial", "12", "bold"))
        self.bet_entry.config(bg="#FDF4E9")

        error = "Oops - Please choose a number more than zero."
        has_errors = "no"

        # checks that the amount of rounds is above 0
        try:
            bet_amount = float(bet_amount)
            if bet_amount > 0:
                # clear entry box and reset instruction label so
                # that when users play a new game, they don't see an error message
                self.bet_entry.delete(0, END)
                self.choose_label.config(text="How much would you like to bet?")
                # invoke play class and take across bet amount
                Play(bet_amount)
                # hide root window
                root.withdraw()
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display error if necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial", "10", "bold"))
            self.bet_entry.config(bg="#F4CCCC")
            self.bet_entry.delete(0, END)


class Play:
    """
    Interface for playing blackjack
    """

    def __init__(self, current_bet):
        self.play_box = Toplevel()

        # frame for gameplay
        self.game_frame = Frame(self.play_box, padx=10, pady=10, bg="#042B01")
        self.game_frame.grid()

        self.game_heading_label = Label(self.game_frame, text=f"Blackjack - Current bet ${current_bet:.2f}",
                                        font=("Arial", "16", "bold"), bg="#042B01", fg="#FDF4E9")
        self.game_heading_label.grid(row=0)

        # frame for buttons
        self.button_frame = Frame(self.game_frame, padx=10, pady=10, bg="#042B01")
        self.button_frame.grid(row=5)

        # make buttons here
        self.help_button = Button(self.button_frame, text="Help",
                                  font=("Arial", "14", "bold"),
                                  fg="#FDF4E9", bg="#040014",
                                  padx=10, pady=10,
                                  command=self.to_help)
        self.help_button.grid(row=0)

        # create frames for cards
        self.dealer_frame = LabelFrame(self.game_frame, borderwidth=0)
        self.dealer_frame.grid(row=2, column=0)

        self.player_frame = LabelFrame(self.game_frame, borderwidth=0)
        self.player_frame.grid(row=3, column=0)

        # put cards in frames
        self.dealer_label = Label(self.dealer_frame, text="", bd=0, bg="#042B01")
        self.dealer_label.pack(ipady=10)

        self.player_label = Label(self.player_frame, text="", bd=0, bg="#042B01")
        self.player_label.pack(ipady=10)

        # labels for score displays
        self.opp_card_label = Label(self.game_frame, text="Opponent Cards",
                                    font=("Arial", "12"), bg="#042B01", fg="#FDF4E9")
        self.opp_card_label.grid(row=1)

        self.user_card_label = Label(self.game_frame, text=f"User Cards",
                                     font=("Arial", "12"), bg="#042B01", fg="#FDF4E9")
        self.user_card_label.grid(row=4)

        # call to deal initial cards
        self.shuffle()

    def shuffle(self):
        # define deck
        suits = ["diamond", "clubs", "hearts", "spades"]
        values = range(1, 14)

        global deck
        deck = []

        for suit in suits:
            for value in values:
                deck.append(f'{suit} {value}')

        # create our players
        global dealer, player
        dealer = []
        player = []

        # get the dealer card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to dealer list
        dealer.append(card)
        # output card to screen

        # needs to be global so it gets used!!!
        global dealer_image
        dealer_image = self.resize_cards(f'cos_images/{card}.png')
        self.dealer_label.config(image=dealer_image)

        # get the player card
        card = random.choice(deck)
        # remove card from deck
        deck.remove(card)
        # append card to player list
        player.append(card)
        # output card to screen

        player_image = self.resize_cards(f'cos_images/{card}.png')
        self.player_label.config(image=player_image)

    # Resize the cards
    def resize_cards(self, card):
        # open image
        our_card_img = Image.open(card)

        # resize image
        our_card_resized = our_card_img.resize((120, 161))

        # output the card
        global our_card_image
        our_card_image = ImageTk.PhotoImage(our_card_resized)

        # return card
        return our_card_image

    def to_help(self):
        """
        Shows help menu for the game
        :return:
        """
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and bg colour
        self.help_box = Toplevel()
        background = "#042B01"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # if users press cross at top, closes help
        # and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help", fg="#FDF4E9",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To win blackjack, you must get as close to 21 as " \
                    "possible without going over. You need to beat your " \
                    "opponent's score, but if they get 21, they win! " \
                    "Scoring: K = 13, Q = 12, J = 11, 10 = 10 etc... A = 1"

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left", fg="#FDF4E9")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="OK", bg="#981C1E",
                                     fg="#FDF4E9",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set bg colour for everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Black Jack")
    StartGame()
    root.mainloop()
