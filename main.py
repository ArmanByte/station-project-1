# Libraries
import random

# Information For User
print("""
Heu, let's play a game.
You'll have to provide me with words, and I will generate text based on templates.
You can either choose a template randomly or pick one of three options.

Type 0 for random template or 1 to choose template.
""")

def choose_template():
    print("""
Now you have to choose the templates.
Input 0 to: Choose the template.
Input 1 to: See the first template.
Input 2 to: See the second template.
Input 3 to: See the third template.
    """)
    temp_choice = input("Choice [0/1/2/3]: ")
    if temp_choice == "1":
        print(first_template)
    elif temp_choice == "2":
        print("Coming soon")
    elif temp_choice == "3":
        print("Coming soon")

def random_template():
    r_number = random.randint(1, 3)

# User Choice
choice = input("Choice [0/1]: ")
if choice == "0":
    random_template()
    print("Random template was chosen.")
elif choice == "1":
    choose_template()
else:
    print("Wrong input. Please try again.")

# Inputs
number = input("Input first number: ")
second_number = input("Input second number: ")
measure = input("Input measure of time: ")
transportation = input("Mode of transportation: ")
adjective = input("Input first adjective: ")
second_adjective = input("Input second adjective: ")
third_adjective = input("Input third adjective: ")
noun = input("Input first noun: ")
second_noun = input("Input second noun: ")
third_noun = input("Input third noun: ")
fourth_noun = input("Input fourth noun: ")
color = input("Input color: ")
body_part = input("Input part of the body: ")
second_body_part = input("Input second part of the body:")
verb = input("Input verb: ")
silly_word = input("Input silly word: ")


first_template = (f"""It was about {number} {measure} ago when I arrived at the hospital in a {transportation}.
The hospital is a/an {adjective} place, there are a lot of {second_adjective} {noun} here.
There are nurses here who have {color} {body_part}.
If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {second_noun} {second_number}.
Today I talked to a doctor and they were wearing a {third_noun} on their {second_body_part}.
I heard that all doctors {verb} {fourth_noun} every day for breakfast.
The most {third_adjective} thing about being in the hospital is the {silly_word} {noun}!
""")
print(temp1)