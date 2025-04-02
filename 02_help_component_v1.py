from tkinter import *
from functools import partial


class StartGame:
    """
    Initial game interface (asks users the bet amount)
    """

    def __init__(self):
        """
        gets bet amount from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # strings for labels
        intro_string = "Welcome to Blackjack!"

        bet_string = "How much do you want to bet?"

        # List of labels to be made (text | font | fg)
        start_labels_list = [
            ["Blackjack", ("Arial", "16", "bold"), None],
            [intro_string, ("Arial", "12"), None],
            [bet_string, ("Arial", "12", "bold"), "#009900"],

        ]

        # Create labels and add them to reference list.

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary.
        self.choose_label = start_label_ref[2]

        # Frame so that entry box and button can be in the same row
        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        # create bet entry
        self.bet_entry = Entry(self.entry_area_frame, font=("Arial", "28", "bold"), width=10)
        self.bet_entry.grid(row=1, column=0, padx=10, pady=30)

        # create play button...
        self.play_button = Button(self.entry_area_frame, font=("Arial", "16", "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play",
                                  width=10, command=self.check_bet)
        self.play_button.grid(row=2, column=0)

    def check_bet(self):

        bet_amount = self.bet_entry.get()

        self.choose_label.config(fg="#009900", font=("Arial", "12", "bold"))
        self.bet_entry.config(bg="#FFFFFF")

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

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.game_heading_label = Label(self.game_frame, text=f"Blackjack - Current bet ${current_bet:.2f}",
                                        font=("Arial", "16", "bold"))
        self.game_heading_label.grid(row=0)

        self.help_button = Button(self.game_frame, text="Help",
                                  font=("Arial", "14", "bold"),
                                  fg="#FDF4E9", bg="#981C1E",
                                  padx=10, pady=10,
                                  command=self.to_help)
        self.help_button.grid(row=1)

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
