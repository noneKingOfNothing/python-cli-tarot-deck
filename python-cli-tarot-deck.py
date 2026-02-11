#    Python CLI Tarot Deck

#    Draws a given number of tarot cards from the deck and present them to the user.

#    credit 'astrology.com/article/order-of-tarot-cards' for the tarot card list

# grab the library to generate random numbers and linecache to pull the proper line
import random , linecache , sys

#make a variable outside the functions to hold drawn cards
drawn_card_tracker = []

#make a function that uses a random number to reference one of the lines in a list of card names, use a list to make sure you don't pull two of the same cards
def draw_cards(number_to_draw):
    for x in range(0 , int(number_to_draw)):
        i = random.randint(1, 78)
        while i in drawn_card_tracker == True:
            i = random.randint(1, 78)
        line = linecache.getline('./cardnames.txt', i)
        line = line.rstrip() # this removes the trailing /n
        drawn_card_tracker.append(line)
        print(line)


# ask for the number of cards to draw and fire the function to pull the right number:
number_to_draw = input("How many cards? Please use a numeral.")
# fire the function to draw cards
draw_cards(number_to_draw)

# ask if the user wants an interpretation. If no: exit, if yes: turn the card list into a string and send the string to an llm with ollama
yes_or_no = input("Would you like an interpretation?")

if yes_or_no == 'no':
    sys.exit()
#else:

    
