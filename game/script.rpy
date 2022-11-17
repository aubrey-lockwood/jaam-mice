# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define w = Character("Wizard", who_color="#13D1E9")

# The game starts here.
label start:


    $ character1 = "Hùng Vasylyna"
    $ character2 = "Leila Rana"
    
    $ player_name = renpy.input("What is your name, Delightful Contestant?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="iclickedtofastthroughthisgameiforgotmyownname"
    define c1 = Character(player_name, who_color="#e91313")
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
            "Fascinating!"

    menu Game1_2:
        w "And where do you live?"
        "In a tree":
            "Wow, really?"
        
        "Under a bridge":
            "Wow, really?"

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
            "Wow, I'd hate to have that many fingers!"
    
    "Our contestants have finished the first part of their applications. They deserve a big round of applause!"



    # Game 2

    screen 

    

        

    # This ends the game.
    return
