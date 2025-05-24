from datetime import date

# ***** get current date for heading and filename *****
today = date.today()

# get day, month, year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

#placeholder
current_bet = 3
# set game_won as true
gamewon = True

file_name = f"game{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("**** Balance ****\n")
    text_file.write(f"Date: {day}/{month}/{year}\n\n")
    if gamewon is True:
        text_file.write(f"Your new balance is...{current_bet}")
    else:
        text_file.write(f"Your new balance is...-{current_bet}")

