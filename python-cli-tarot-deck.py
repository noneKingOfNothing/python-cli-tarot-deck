#    Python CLI Tarot Deck

#    Draws a given number of tarot cards from the deck and present them to the user.

#    credit 'astrology.com/article/order-of-tarot-cards' for the tarot card list

# grab the library to generate random numbers and linecache to pull the proper line
import random , linecache

'''make a function that uses a random number to reference one of the lines
in a list of card names, use a list to make sure you don't pull two of the same cards'''

def draw_cards(number_to_draw):
    for x in range(0 , int(number_to_draw)):
        drawn_card_tracker = []
        i = random.randint(1, 78)
        if i in drawn_card_tracker == True:
            i = random.randint(1, 78)
        else:
            drawn_card_tracker.append(i)
        line = linecache.getline('./cardnames.txt', i)
        print(line)

# ask for the number of cards to draw and fire the function to pull the right number:
number_to_draw = input("How many cards? Please use a numeral.")
draw_cards(number_to_draw)


    
