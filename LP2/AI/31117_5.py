# 31117 - Udayan Chavan - K1
# ASSIGNMENT 5 - Develop an elementary chatbot for a suitable customer interaction application.
# ================================================================================================

import nltk
from nltk.chat.util import *

# Checking for specific keywords in the user input and giving an appropriate response
pairs = [
    # ------- Basic conversation --------
    [
        (r"(.*)my name is(.*)"),
        ["Hello%2, how are you today?",]
    ],
    [
        (r'(.*)fine(.*)|(.*)good(.*)|(.*)well(.*)'),
        ["Good to know, how can I help you?",]
    ],
    [
        (r'(.*)hi(.*)|(.*)hey(.*)|(.*)hello(.*)'),
        ['Hey there, how can I help you?', 'Hi! how can I be of your assistance?', 'Hello, what can I help you with?']
    ],
    [
        (r'(.*)help(.*)|(.*)show(.*)'),
        ["Sure, I can help you with it.", "Sure, I will show it right away",]
    ],
    [
        (r'(.*)thank you(.*)|(.*)thanks(.*)|(.*) ty (.*)'),
        ['Welcome!', 'You are Welcome!', 'Glad I could help!']
    ],
    # -------- General Information ---------
    [
        (r'(.*)name of company(.*)|(.*)company name(.*)|(.*)name of your company(.*)'),
        ['I represent XYZ Travel Agency.', 'I am employed by XYZ Travel Agency.', 'I work at XYZ Travel Agency.']
    ],
    [
        (r'(.*)popular destinations(.*)|(.*)popular cities(.*)|(.*)popular spots(.*)'),
        ['You can refer to our website for a list of trending destinations.', 'Check out our special plans for popular destinations on our website.']
    ],
    [
        (r'(.*)cost(.*)|(.*)price(.*)|(.*)expense(.*)'),
        ['You can refer to our website for detailed pricing plans.', 'Please check out our exclusive deals each Friday.']
    ],
    # -------- Ticket booking ---------
    [
        (r'(.*)book(.*)|(.*)booking(.*)|(.*)reserve(.*)'),
        ['Please enter the date of travel: ']
    ],
    [
        (r'(.*)date (.*)'),
        ['Buses on %2 are available. Please enter the bus number according to our website: ']
    ],
    [
        (r'(.*)bus (.*)'),
        ['Thanks for choosing bus %2. Now please enter the seats you want to book: ']
    ],
    [
        (r'(.*)seats (.*)'),
        ['Thank you for booking %2. I will now take you to the payment section.']
    ],
]

# ------------------------------------------------------------------------------

def chatbot():
    print("Hello, Welcome to XYZ Travel Agency. How can I help you?")
    cb = Chat(pairs, reflections)
    
    while True:
        q = input("")
        cb.respond(q)
        if q == "quit":
            break;
        if cb.respond(q) is None: 
            print("Sorry I did not understand. Please contact us at XYZtravels@gmail.com / +91 1234567890")
        else:
            print(cb.respond(q))
    
chatbot()

'''
SAMPLE INPUT

hey / hello
my name is udayan
i am doing well
tell me the company name
what are some popular destinations
what would be the cost of a trip to Paris

- i want to reserve a seat
- book a ticket
- need to make a booking

bus b1
date 24/06/2022
seats s1 s2 s3

thanks
'''

'''
============================================================
OUTPUT:
Hello, Welcome to XYZ Travel Agency. How can I help you?
>Hello xyz
Hello, what can I help you with?

>my name is Udayan
Hello udayan, how are you today?

>i am fine
Good to know, how can I help you?

>tell me the name of your company
I am employed by XYZ Travel Agency.

>suggest some popular destinations
You can refer to our website for a list of trending destinations.

>what would a paris trip cost me
You can refer to our website for detailed pricing plans.

>i need to book a ticket
Please enter the date of travel: 

>date 3/05/2022
Buses on 3/05/2022 are available. Please enter the bus number according to our website: 

>Bus B22
Thanks for choosing bus b22. Now please enter the seats you want to book: 

>seats S1 S2 S33 S45
Thank you for booking s1 s2 s33 s45. I will now take you to the payment section.

>thanks 
You are welcome!
'''