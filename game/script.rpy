﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
label start:


    $ character1 = "TEST"
    $ character2 = "TEST2" 

    $ playerName = "TESTP"

    define w = Character("Wizard", who_color="#13D1E9")

    scene bg black
    show part3
    
    w "HELLOOOOOOOOO! And welcome to the College Application Game Show!!! Your only source of non-stress-inducing, college application based entertainment- that may or may not have any real life consequences!!"

    w "Today we welcome our newest contestant: [playerName]!!!!"

    w "How do you feel [playerName]? Are you ready to create your perfect application????"

    menu ready:
        w "How do you feel [playerName]? Are you ready to create your perfect application????"
        "Yes":
            w "Alrighty then, let’s..."
            w "APPLY TO COLLEGE!!!"
        
        "No":
            play sound "audio/laughtrackshort.mp3" fadeout 1.0
            w "Sucks for you I guess!!! We're doing it anyway!"
            w "Let's..."
            w "APPLY TO COLLEGE!!!"
        

    w "First up, you must decide on your background information." 
        
    w "Now remember, the choices you make now will impact you forever and are extremely important."

    w "Anyywaayyysss, let’s play"


    # Game 1 
    menu Game1_1:
        w "What kind of family do you have?"
        "Elf":
            w "Fascinating!"
        "Goblin":
            w "Fascinating!"

    menu Game1_2:
        w "And where do you live?"
        "In a tree":
            w "Wow, really?"
        
        "Under a bridge":
            w "Wow, really?"

    menu Game1_3:
        w "Next up, what do you like to eat for dinner?"
        "Acorns":
            w "Great choice!"
        "Horse chesnuts":
            w "Great choice!"
    menu Game1_4:
        w "How many fingers do you have?"
        "More than seven":
            w "Wow, I'd hate to have that many fingers!"
        "Less than three":
            w "Wow, I'd hate to have that many fingers!"
    
    w "Our contestants have finished the first part of their applications. They deserve a big round of applause!"



    # Game 2


    # This ends the game.
    return
