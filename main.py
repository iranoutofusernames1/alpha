import random
import string
import re

from phrases import phraselibrary
from words import wordlibrary

def alpha():
   math_pattern = re.compile(r'\d+\s*[+\-*/]\s*\d+')
   bridges = [" also, ", " and... ", " uhhhhh... ", " oh, and "]
   debugoption = input("""Would you like to enable debug mode?
(Y | N) : """).lower()
   print("Alpha: Hello! I am Alpha, a simple chatbot!")
   while True:
       replies = [] # Reset every reply; stops Alpha from just loosing it over time.
       found_match = False
       user_input = input("You: ").lower()
       words = user_input.split() # Splits the words
       if debugoption == "y":
           print("NETWORK: " + str(words))
      
       words_set = set(user_input.split())

       # Math check
       math_match = math_pattern.search(user_input)

       if math_match:
           expression = math_match.group()
    
           try:
               result = eval(expression)
               print(f"Alpha: ooh, let me think... {expression} = {result}!")
               print("")
               found_match = True  

           except ZeroDivisionError:
               print("Alpha: AAAAAAAAAAAAAAAAAHHHHHHHHHHHH!!!!!!!!!!!!!!!")
               print("")
               found_match = True
        
           except Exception:
               print("Alpha: Uhm...  I had a error, sorry!")
               print("")
               found_match = True

       # Phrase check
       for name, data in phraselibrary.items():
           for trigger_set in data['triggers']:
               if trigger_set.issubset(words_set):
                   if data['reply'] not in replies:
                       replies.append(data['reply'])
                       if debugoption == "y":
                           print(f"NETWORK:phraselibrary-{data['reply']}")
                       found_match = True
                   break

       # Word check
       for word in words:
           clean_word = word.strip(string.punctuation) # TODO: ADD A WAY TO RECOGNIZE PUNCTUATION
           for word_name, word_data in wordlibrary.items(): # Does this for every word in the library
               if clean_word in word_data['versions']:
                   reply = random.choice(word_data['reply'])
                   if reply not in replies: # Only add if it's not a duplicate
                       replies.append(reply)
                   if debugoption == "y":
                       print(f"NETWORK:wordlibrary-{clean_word}={word_name}")
                   found_match = True
                   break

       if replies:
           if len(replies) > 1:
               connector = random.choice(bridges)
               print(f"Alpha: {connector.join(replies)}")
           else:
               print(f"Alpha: {replies[0]}")   
               print("")         
       elif not found_match:
           print("Alpha: I don't understand... at least, not yet! I'm still growing!")
           print("")

alpha()
