# The script of the game goes in this file.

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
    
    "HELLOOOOOOOOO! And welcome to the College Application Game Show!!! Your only source of non-stress-inducing, college application based entertainment- that may or may not have any real life consequences!!"

    "Today we welcome our newest contestant: [playerName]!!!!"

    "How do you feel [playerName]? Are you ready to create your perfect application????"

    menu ready:
        "How do you feel [playerName]? Are you ready to create your perfect application????"
        "Yes":


    "Today our contestants are [character1], [character2], and [playerName]!"





    "We'll Start with your family background and demographics. Remember, people at home, you can all see the contestants' answers, but they can't see each other!"



    # Game 1 
    menu Game1_1:
        "What kind of family do you have?"
        "Elf":
            "Fascinating!"
        "Goblin":
            "Fascinating!"

    menu Game1_2:
        "And where do you live?"
        "In a tree":
            "Wow, really?"
        
        "Under a bridge":
            "Wow, really?"

    menu Game1_3:
        "Next up, what do you like to eat for dinner?"
        "Acorns":
            "Great choice!"
        "Horse chesnuts":
            "Great choice!"
    menu Game1_4:
        "How many fingers do you have?"
        "More than seven":
            "Wow, I'd hate to have that many fingers!"
        "Less than three":
            "Wow, I'd hate to have that many fingers!"
    
    "Our contestants have finished the first part of their applications. They deserve a big round of applause!"



    # Game 2

    screen 

    

        

    # This ends the game.
    return
