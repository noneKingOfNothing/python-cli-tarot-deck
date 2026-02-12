#    Python CLI Tarot Deck

#    Draws a given number of tarot cards from the deck and present them to the user.

#    credit 'astrology.com/article/order-of-tarot-cards' for the tarot card list

#we need random numbers, line references, system tools (to exit), and ollama's chat to interact with LLMs'
import random , linecache , sys
from ollama import generate

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
        print()
        print(line)


# ask for the number of cards to draw and fire the function to pull the right number:
print(2 * '\n')
number_to_draw = input("How many cards would you like to draw from the deck? Please use a numeral.    ")

#add space to make things readable
print(2 * '\n')

# fire the function to draw cards
draw_cards(number_to_draw)


# ask if the user wants an interpretation of the draw. If no: exit, if yes: turn the card list into a string and send the string to an llm with ollama.
print(2 * '\n')
yes_or_no = input("Would you like an interpretation?  ")

if yes_or_no == 'yes':
   drawn_card_tracker = ', '.join(drawn_card_tracker)
   response = generate(
       model='dolphin-llama3:8b',
       prompt=f'You are a professional tarot card reader. Please tell me what symbols appear in the following cards and what the cards mean. They are {drawn_card_tracker}'
       )
   print(2 * '\n')
   print(response.response)
   print(2 * '\n')

else:
    sys.exit()

    
