# FILE NAME - coin_toss.py

# NAME: Blake Lemarr
# DATE: 03/02/2026
# BRIEF DESCRIPTION: A program that returns heads or tails depending on the number generated. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!

import random

number: int = random.randint(1, 100)

if number > 50:
    print('Tails')
else:
    print('Heads')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

It was disregardining my instincts to simplify it since I know that
I could just reduce it to print(random.choice(["Heads", "Tails"])).

'''
