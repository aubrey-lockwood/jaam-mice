﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define w = Character("Wizard", who_color="#13D1E9")
# The game starts here.
label start:

    jump game_two
    $ character1 = "Hùng Vasylyna"
    $ character2 = "Leila Rana"
    
    $ playerName = renpy.input("What is your name, Delightful Contestant?")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName ="iclickedtofastthroughthisgameiforgotmyownname"
    scene bg black
    show part3

    play music "audio/part3music.mp3" 

    w "HELLOOOOOOOOO! And welcome to the College Application Game Show!!! Your only source of non-stress-inducing, college application based entertainment- that may or may not have any real life consequences!!"

    w "Today we welcome our newest contestant: [playerName]!!!!"

    w "How do you feel [playerName]? Are you ready to create your perfect application????"

    menu ready:
        w "How do you feel [playerName]? Are you ready to create your perfect application????"
        "Yes":
            w "Alrighty then, let’s..."
            play sound "audio/applytocollegechant.mp3" fadeout 1.0
            w "APPLY TO COLLEGE!!!"
        
        "No":
            play sound "audio/laughtrackshort.mp3" fadeout 1.0
            w "Sucks for you I guess!!! We're doing it anyway!"
            w "Let's..."
            play sound "audio/applytocollegechant.mp3" fadeout 1.0
            w "APPLY TO COLLEGE!!!"
        

    w "First up, you must decide on your background information." 
        
    w "Now remember, the choices you make now will impact you forever and are extremely important."

    w "Anyywaayyysss, let’s play"

    label game1:
        
    menu Game1_1:
        w "What kind of family do you have?"
        "Elf":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Fascinating!"
        "Goblin":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Fascinating!"

    menu Game1_2:
        w "And where do you live?"
        "In a tree":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Wow, really?"
        
        "Under a bridge":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Wow, really?"

    menu Game1_3:
        w "Next up, what do you like to eat for dinner?"
        "Acorns":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Great choice!"
        "Horse chesnuts":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Great choice!"
    menu Game1_4:
        w "How many fingers do you have?"
        "More than seven":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Wow, I'd hate to have that many fingers!"
        "Less than three":
            play sound "audio/selectionnoiselow.mp3" fadeout 1.0
            w "Wow, I'd hate to have that many fingers!"
    
    stop music
    w "Our contestants have finished the first part of their applications. They deserve a big round of applause!"

    play music "audio/part3music.mp3" 

    label game_two:
        w "Starting part 2, the resume!!!"
    # Game 2

    $ extra_curic = {}

    show screen textbutton_screen
    screen textbutton_screen:
        #window id "window":
        vbox:
            spacing 10
            textbutton "help":
                align (0.5, 0.5)
                action AddToSet(extra_curic, "help")
                # give me a sec I got to fix this unaction RemoveFromSet(e_C,"help")

    " "
    hide screen textbutton_screen
    w "so did you do a thing?? [extra_curic]"
        

    # This ends the game.
    return
