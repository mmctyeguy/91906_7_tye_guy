import csv
import random

file = open("deck.csv", "r")
all_cards = list(csv.reader(file, delimiter=","))
file.close()

all_cards.pop(0)

# lists to hold card data
held_cards = []
opponent_cards = []
user_cards = []

# loop to deal initial cards
while len(held_cards) < 4:
    dealt_card = random.choice(all_cards)
    all_cards.remove(dealt_card)
    held_cards.append(dealt_card)

# from initial dealings split cards
# between user and opponent
user_cards.extend(held_cards[:2])
opponent_cards.extend(held_cards[-2:])

# temporary print statements to check values
print(held_cards)
print("")
print(user_cards)
print("")
print(opponent_cards)

# basic loop to deal another card
deal_again = input("another card?")
if deal_again == "yes":
    dealt_card = random.choice(all_cards)
    all_cards.remove(dealt_card)
    held_cards.append(dealt_card)
    user_cards.append(dealt_card)
else:
    print("ok")

# print to check new card is added
print(user_cards)
print("")
print(held_cards)




