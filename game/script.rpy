# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define w = Character("Wizard", who_color="#13D1E9")
define boss = Character("Boss", who_color="#F6B414")
define narrator = Character("", who_color="#209D02")

# The game starts here.
label start:

    label part1:

    scene bg black
    show bg black

    $ playerName = renpy.input("What is your name, admissions officer?")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName ="iclickedtofastthroughthisgameiforgotmyownname"

    show bg officeclosed:
        zoom 0.4

    play music "audio/UARTS_Admissions_Office_White_Noise.mp3"

    show bg bosspresent with fade

    boss "Hello [playerName]. I have a nice new stack of applications for you to go through today."
    boss "Remember, you have to decide whether they should be recommended for admittance to our university or not."
    boss "Don't forget to look back at the specifications I gave you for who should be admitted or not! It's really important that you stick to those rules, because having certain types of students will really make the university look good." # add emphasis on "certain students?"
    
    # MANILA FOLDER APPEARS ON THE DESK (FIXME)

    # RULES APPEAR / GLOW IN CORNER (FIXME)

    # LOOK UP (FIXME)

    boss "Alright, with that, I'll be off. You shouldn't have any issues with this."
    boss "Good luck!"

    show bg officeopen with fade

    show bg desk with fade


    label firstApps:
        window hide
        show screen task("Sort the appplications to decide if they should be recommended or not!")
        python:
            applications = range(10)

            for i in applications:
                if (not renpy.call_screen("applicationSort", i)):
                    renpy.call_screen("wrongSort")
                    renpy.jump("firstApps")
                    renpy.with_statement(fade)
                else:
                    renpy.with_statement(fade)

    hide screen task
    
    hide screen applicationSort
    
    show bg officeopen

    with fade

    show bg bosspresent with fade

    # BOSS REENTERS (FIXME)

    boss "Oh, hi [playerName]! How has application sorting been going?"

    menu howFeel:
        boss "Oh, hi [playerName]! How has applications sorting been going?"

        "Good":
            boss "Well that's good, because I just found a few more for you to categorize as well!"

        "Not so good":
            boss "I'm sorry to hear that."
            boss "Well, luckily you only have a few left."
            boss "Here are the last applications for you to go through today."

    boss "They must've gotten separated from the others, I'm not sure why."
    boss "Here you go!" 
    
    show bg officeclosed with fade
    
    show bg desk with fade

    label finalApps:
        window hide
        show screen task("Sort this second set of applications. Why were they separated?")
        python:
            applications = range(10, 13)

            for i in applications:
                renpy.call_screen("applicationSort", 10)

                if i < 12:
                    renpy.call_screen("wrongSort") # 2 failed iterations

                else:
                    renpy.call_screen("impossibleSortI") # finally forced to click pass

        hide screen task

        label finalApps2:
            show bg desk with fade
            window hide

        show screen task("Sort this second set of applications. Why were they separated?")

        python:
            applications = range(11, 15)

            for i in applications:
                renpy.call_screen("applicationSort", i)

                if renpy.call_screen("impossibleSort"): #if you click "try again", you have to restart this section. Reinforce defeated feeling!
                    renpy.jump("finalApps2")
        
        hide screen task

        show bg bloodydesk

        narrator "Oh no! Looks like you got a paper cut!"
        narrator "Make sure to take care of that correctly!"

        "(You go to get a bandage.)"

        show bg breakroom with fade

        narrator "Which bandage will you use?"
        
        show screen bandaids

        if ui.interact():
            hide screen bandaids
            jump finalApps2
        hide screen bandaids
                

    
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

    # Game 2
    label game2:
    
    w "Starting part 2, the resume!!!"
                
    $ ec = {"Ferret training", "Blaseball", "Hackey Sack for Unicorns", "Troll Hair Designs", "Bed Frame Wood Testing", "Graveyard Patrol Volunteering", "Sitting on Babies", "The Toot Town Fart Symphony", "Wings for Fairies", "Ladder Testing", "Portabella Mushroom Connoisseur", "Pizza Throwing Club"}
    # This is a dictionary mapping a period to a ???? 
    default player_ec = {'?','?'}

    show screen game2

    $ ui.interact()
    hide screen game2
    w "so did you do a thing?? [player_ec]"
        

    # This ends the game.
    return
