from tkinter import *


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

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.game_heading_label = Label(self.game_frame, text=f"Blackjack - Current bet ${current_bet:.2f}",
                                        font=("Arial", "16", "bold"), bg="#042B01", fg="#FDF4E9")
        self.game_heading_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Black Jack")
    StartGame()
    root.mainloop()
