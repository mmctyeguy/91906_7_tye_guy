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

        self.help_button = Button(self.entry_area_frame, text="Help",
                                  font=("Arial", "16", "bold"), fg="#FDF4E9", bg="#040014",
                                  width=10, command=self.to_help)
        self.help_button.grid(row=3, column=0, pady=10)

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
            self.bet_entry.config(bg="#F4CCCC", fg="#040014")
            self.bet_entry.delete(0, END)

    def to_help(self):
        """
        Shows help menu for the game
        :return:
        """
        DisplayHelp(self)


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

        self.hit_me_button = Button(self.button_frame, text="Hit Me!", fg="#FDF4E9", bg="#981C1E",
                                    command=self.player_hit, font=("Arial", "16", "bold"),
                                    width=10)
        self.hit_me_button.grid(row=0, column=0, padx=5, pady=5)

        self.stand_button = Button(self.button_frame, text="Stand", fg="#FDF4E9", bg="#040014",
                                   command=self.stand(current_bet), font=("Arial", "16", "bold"),
                                   width=10)
        self.stand_button.grid(row=0, column=1, padx=5, pady=5)

        # create frames for cards
        self.dealer_frame = LabelFrame(self.game_frame, borderwidth=0)
        self.dealer_frame.grid(row=2, padx=20, ipadx=20)

        self.player_frame = LabelFrame(self.game_frame, borderwidth=0)
        self.player_frame.grid(row=3, ipadx=20, pady=10)

        # put dealer cards in frames
        self.dealer_label_1 = Label(self.dealer_frame, text="")
        self.dealer_label_1.grid(row=0, column=0, padx=20)

        self.dealer_label_2 = Label(self.dealer_frame, text="")
        self.dealer_label_2.grid(row=0, column=1, padx=20)

        # put player cards in frames
        self.player_label_1 = Label(self.player_frame, text="")
        self.player_label_1.grid(row=1, column=0, padx=20)

        self.player_label_2 = Label(self.player_frame, text="")
        self.player_label_2.grid(row=1, column=1, padx=20)

        self.player_label_3 = Label(self.player_frame, text="")
        self.player_label_3.grid(row=1, column=2, padx=20)

        self.player_label_4 = Label(self.player_frame, text="")
        self.player_label_4.grid(row=1, column=3, padx=20)

        self.player_label_5 = Label(self.player_frame, text="")
        self.player_label_5.grid(row=1, column=4, padx=20)

        # labels for score displays
        self.opp_card_label = Label(self.game_frame, text="Opponent Cards",
                                    font=("Arial", "12"), bg="#042B01", fg="#FDF4E9")
        self.opp_card_label.grid(row=1)

        self.user_card_label = Label(self.game_frame, text=f"User Cards",
                                     font=("Arial", "12"), bg="#042B01", fg="#FDF4E9")
        self.user_card_label.grid(row=4)

        # call to deal initial cards
        self.shuffle()

    # shuffle the cards
    def shuffle(self):
        # Clear all the old cards from previous games
        self.dealer_label_1.config(image="")
        self.dealer_label_2.config(image="")

        self.player_label_1.config(image="")
        self.player_label_2.config(image="")
        self.player_label_3.config(image="")
        self.player_label_4.config(image="")
        self.player_label_5.config(image="")

        # define deck
        suits = ["diamond", "clubs", "hearts", "spades"]
        values = range(1, 14)

        global deck
        deck = []

        for suit in suits:
            for value in values:
                deck.append(f'{suit} {value}')

        # create global variables to store cards, spot values and scores
        global dealer, player, dealer_spot, player_spot, pscore, dscore
        dealer = []
        player = []
        dealer_spot = 0
        player_spot = 0
        pscore = []
        dscore = []

        # shuffle 2 cards for player and dealer
        self.dealer_hit()
        self.dealer_hit()
        self.player_hit()
        self.player_hit()

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

    def dealer_hit(self):
        global dealer_spot
        if dealer_spot < 3:
            try:
                # get the dealer card
                dealer_card = random.choice(deck)
                # remove card from deck
                deck.remove(dealer_card)
                # append card to dealer list
                dealer.append(dealer_card)
                # output card to screen

                global dealer_image1, dealer_image2

                # resize and set cards in labels
                if dealer_spot == 0:
                    dealer_image1 = self.resize_cards(f'cos_images/{dealer_card}.png')
                    self.dealer_label_1.config(image=dealer_image1)
                    # increment dealer spot counter
                    self.dealer_score(dealer_card)
                    dealer_spot += 1
                elif dealer_spot == 1:
                    dealer_image2 = self.resize_cards(f'cos_images/{dealer_card}.png')
                    self.dealer_label_2.config(image=dealer_image2)
                    # increment dealer spot counter
                    self.dealer_score(dealer_card)
                    dealer_spot += 1

                # TEMPORARY DISPLAY
                self.opp_card_label.config(text=f"Opponent Score: {sum(dscore)}")
                # put number of cards left in title bar
                root.title(f"Blackjack game - {len(deck)} cards left")
            except:
                root.title(f"Blackjack - No cards in deck")

    def player_hit(self):
        global player_spot
        if player_spot < 5 and sum(pscore) < 21:
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
                    player_image1 = self.resize_cards(f'cos_images/{player_card}.png')
                    self.player_label_1.config(image=player_image1)
                    # increment player spot counter
                    self.player_score(player_card)
                    player_spot += 1
                elif player_spot == 1:
                    player_image2 = self.resize_cards(f'cos_images/{player_card}.png')
                    self.player_label_2.config(image=player_image2)
                    # increment player spot counter
                    self.player_score(player_card)
                    player_spot += 1
                elif player_spot == 2:
                    player_image3 = self.resize_cards(f'cos_images/{player_card}.png')
                    self.player_label_3.config(image=player_image3)
                    # increment player spot counter
                    self.player_score(player_card)
                    player_spot += 1
                elif player_spot == 3:
                    player_image4 = self.resize_cards(f'cos_images/{player_card}.png')
                    self.player_label_4.config(image=player_image4)
                    # increment player spot counter
                    self.player_score(player_card)
                    player_spot += 1
                elif player_spot == 4:
                    player_image5 = self.resize_cards(f'cos_images/{player_card}.png')
                    self.player_label_5.config(image=player_image5)
                    # increment player spot counter
                    self.player_score(player_card)
                    player_spot += 1

                # display score
                self.user_card_label.config(text=f"User Score: {sum(pscore)}")
                if sum(pscore) > 21:
                    end_window = Toplevel()  # Create a new window
                    end_window.title("Game Over! You lost")
                    end_window.geometry("250x150")
                # put number of cards left in title bar
                root.title(f"Blackjack game - {len(deck)} cards left")
            except:
                root.title(f"Blackjack - No cards in deck")

    def dealer_score(self, dealer_card):
        # split out card values
        dealer_card = int(dealer_card.split()[1])
        dscore.append(dealer_card)

    def player_score(self, player_card):
        # split out card values
        player_card = int(player_card.split()[1])
        pscore.append(player_card)

    def stand(self, current_bet):
        """
        checks who won
        :return:
        """

        if sum(pscore) > 21:
            gamewon = False
        elif sum(dscore) > 21:
            gamewon = True
        elif sum(pscore) == 21 and sum(pscore) > sum(dscore):
            gamewon = True
        elif sum(pscore) > sum(dscore):
            gamewon = True
        elif sum(dscore) == 21:
            gamewon = False
        else:
            gamewon = False

        self.end_game(gamewon, current_bet)

    def end_game(self, gamewon, current_bet):

        # create end screen window
        end_window = Toplevel()
        end_window.title("Game Over!")
        end_window.geometry("300x300")
        end_window.config(bg="#042B01")
        end_window.grid()

        end_frame = Frame(end_window, padx=10, pady=10, bg="#042B01")
        end_frame.grid()

        end_label = Label(end_frame, text="Game Over", fg="#FDF4E9", bg="#042B01", font=("Arial", "16", "bold"))
        end_label.grid(row=0, padx=80)

        game_label = Label(end_frame, text="", fg="#FDF4E9", bg="#042B01", font=("Arial", "14", "bold"))
        game_label.grid(row=2, pady=10)

        bet_label = Label(end_frame, text="", fg="#FDF4E9",
                          bg="#042B01", font=("Arial", "12"))
        bet_label.grid(row=3)

        play_button = Button(end_frame, text="Play Again!", fg="#FDF4E9", font=("Arial", "12", "bold"), bg="#981C1E",
                             width=10)
        play_button.grid(row=4, pady=100, ipadx=10, ipady=5)

        if gamewon is True:
            game_label.config(text="You won!")
            bet_label.config(text=f"Your new balance is...{current_bet}")
        else:
            game_label.config(text="You lost...")
            bet_label.config(text=f"Your new balance is...-{current_bet}")


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


if __name__ == "__main__":
    root = Tk()
    root.title("Black Jack")
    StartGame()
    root.mainloop()
