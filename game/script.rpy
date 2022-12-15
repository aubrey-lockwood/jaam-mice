# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define default_speed = 70

define w = Character("Wizard", who_color="#13D1E9", what_slow_cps=default_speed, what_slow_abortable=True, image="w")
define w_slow = Character("Wizard", who_color="#13D1E9", what_slow_cps=4, what_slow_abortable=False, image="w")
image w neutral = Image("wizard_neutral.png", xalign=0.155, yalign=0.36, xsize=100, ysize=100)

define mysterious = Character("Mysterious Voice", who_color="#13D1E9", what_slow_cps=default_speed, what_slow_abortable=True, image="w")

define boss = Character("Boss", who_color="#F6B414", what_slow_cps=default_speed, what_slow_abortable=True)

define narrator = Character("", who_color="#209D02", what_slow_cps=default_speed, what_slow_abortable=True)
define thoughts = Character("", who_color="#C55226", what_slow_cps=default_speed, what_slow_abortable=True)


define answ1 = True
define answ2 = False

define m = Character("Miro", who_color="#5032c7", what_slow_cps=default_speed, what_slow_abortable=True)
image mi = Image("miro standing.png", xalign=0.155, yalign=0.36, xsize=40, ysize=40)
define mk = Character("miroh@mclaud.org computer screen", who_color="#5032c7", what_slow_cps=default_speed, what_slow_abortable=True)
define rosalia = Character("Rosalía", who_color="#d42f68", what_slow_cps=default_speed, what_slow_abortable=True)
image ro = Image("rosalia standing.png", xalign=0.155, yalign=0.36, xsize=40, ysize=40)
define cecily = Character("Cecily", who_color="#6197ed", what_slow_cps=default_speed, what_slow_abortable=True)
image ce = Image("cecily standing.png", xalign=0.155, yalign=0.36, xsize=40, ysize=40)
define jeremiah = Character("Jeremiah", who_color="#d19900", what_slow_cps=default_speed, what_slow_abortable=True)
image je = Image("jeramiah standing.png", xalign=0.155, yalign=0.36, xsize=40, ysize=40)
define jonathan = Character("Jonathan", who_color="#24500d", what_slow_cps=default_speed, what_slow_abortable=True)
image jo = Image("jonathan standing.png", xalign=0.155, yalign=0.36, xsize=40, ysize=40)
define paSystem = Character("PA System", what_slow_cps=default_speed, what_slow_abortable=True)

# The game starts here.
label start:


    label part1:

    scene bg black
    show bg black

    $ playerName = renpy.input("What is your name, admissions officer?")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName ="iclickedtofastthroughthisgameiforgotmyownname"

    define player = Character("[playerName]", what_slow_cps=default_speed, what_slow_abortable=True)

    show bg officeclosed:
        zoom 0.4

    play music "audio/UARTS_Admissions_Office_White_Noise.mp3"

    show bg bosspresent with fade

    boss "Hello [playerName]. I have a nice new stack of applications for you to go through today."

    #Shortcut for Julia's Testing: DELETE THIS FOR FINAL

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
                if (not renpy.call_screen("firstApplicationSort", i)):
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
        narrator "Make sure to take care of that correctly!" # narrator style potentially clashes with usage later in this case, possibly revisit (FIXME)

        "You go to get a bandage."

        show bg breakroom with fade

        narrator "Which bandage will you use?"
        
        show screen bandaids

        if ui.interact():
            hide screen bandaids
            jump finalApps2
        hide screen bandaids

        stop music
        
        jump part2
                

                        

    label part3:
        stop music
        scene bg black
        show bg gameshow:
            zoom 0.4
        show w neutral:
            zoom 0.2
        with fade
            

    play music "audio/part3music.mp3" #MUSIC DISABLED FOR SANITY

    w "HELLOOOOOOOOO! And welcome to the College Application Game Show!!! Your only source of non-stress-inducing, college application based entertainment- that may or may not have any real life consequences!!"

    w "Today we welcome our newest contestant: [playerName]!!!!"

    w "How do you feel [playerName]? Are you ready to create your perfect application????"


    window hide


    show screen binaryQ("Are you ready to create the perfect application?", "Yes", "No")
    if ui.interact(): 
        hide screen binaryQ

        w "Alrighty then, let’s..."
        play sound "audio/applytocollegechant.mp3" fadeout 1.0
        w_slow "APPLY TO COLLEGE!!!"
        $renpy.pause(delay = 5.0, hard = True)
        
        
    else:
        hide screen binaryQ

        play sound "audio/laughtrackshort.mp3" fadeout 1.0
        w "Sucks for you I guess!!! We're doing it anyway!"
        w "Let's..."
        play sound "audio/applytocollegechant.mp3" fadeout 1.0
        w_slow "APPLY TO COLLEGE!!!"
        $renpy.pause(delay = 5.0, hard = True)
        

    w "First up, you must decide on your background information." 
        
    w "Now remember, the choices you make now will impact you forever and are extremely important."

    w "Anyywaayyysss, let’s play"

    label game1:
        
    w "What kind of family do you have?"
    window hide
    show screen binaryQ("What kind of family do you have?", "Elf", "Goblin")
    if ui.interact():
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Fascinating!"
    else:
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Fascinating!"
    hide screen binaryQ

    
    w "And where do you live?"
    window hide
    show screen binaryQ("And where do you live?", "In a tree", "Under a bridge")
    if ui.interact():
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Wow, really?"
    else:
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Wow, really?"
    hide screen binaryQ

    w "Next up, what do you like to eat for dinner?"
    window hide
    show screen binaryQ("Next up, what do you like to eat for dinner?", "Acorns", "Horse Chestnuts")
    if ui.interact():
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Great choice!"
    else:
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Great choice!"
    hide screen binaryQ

    w "How many fingers do you have?"
    window hide
    show screen binaryQ("How many fingers do you have?", "More than seven", "Less than three")
    if ui.interact():
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Wow, I'd hate to have that many fingers!"
    else:
        play sound "audio/selectionnoiselow.mp3" fadeout 1.0
        w "Wow, I'd hate to have that many fingers!"
    hide screen binaryQ
    
    stop music

    w "Our contestants have finished the first part of their applications. They deserve a big round of applause!"

    play music "audio/part3music.mp3" #MUTED FOR SANITY

    # Game 2
    label game2:
    
    w "Starting part 2, the resume!!!"

    $ ec = {"Ferret training", "Blaseball", "Hackey Sack for Unicorns", "Troll Hair Designs", "Bed Frame Wood Testing", "Graveyard Patrol Volunteering", "Sitting on Babies", "The Toot Town Fart Symphony", "Wings for Fairies", "Ladder Testing", "Portabella Mushroom Connoisseur", "Pizza Throwing Club"}
    # This is a dictionary mapping a period to a ???? 
    default player_ec = {'?','?'}

    show screen game2
    $ ui.interact()
    hide screen game2
    
    w "A perfectly understandable response from our contestant!"

    stop music

    w "Another big round of applause for [playerName]!"

    label game3:

    play music "audio/part3music.mp3" 
    #MUTED FOR SANITY

    w "Last, but certainly not least, you must write your very own personal statement."

    w "You must provide words of the specified type in order to complete your story about a lesson you have learned by overcoming a difficulty in your life."

    w "When you're all done with that, I'll read your story in front of all these strangers!" 

    window hide
    show screen binaryQ("Are you ready?", "Sure", "Does it even matter anymore?")
    if ui.interact():
        w "Alrighty then, let's get started!"

    else:
        w "Nope! Let's get started!"
    hide screen binaryQ

    show screen textInput("Enter a number!")
    $ age = ui.interact()
    hide screen textInput

    show screen textInput("Enter a type of family relation, like 'sister' or 'cousin'!")
    $ relativeType = ui.interact()
    hide screen textInput

    show screen textInput("Enter a verb ending in ing, like 'jumping'!")
    $ verb = ui.interact()
    hide screen textInput

    show screen textInput("Enter a noun, like 'frog'!")
    $ nounLoser = ui.interact()
    hide screen textInput

    show screen textInput("Enter a regular adjective, like 'silly'!")
    $ adjectiveTeacher = ui.interact()
    hide screen textInput

    show screen textInput("Enter a class you might take at a high school, like 'American Literature'!")
    $ highSchoolClass = ui.interact()
    hide screen textInput

    show screen textInput("Enter a person's name!")        
    $ relativeName = ui.interact()
    hide screen textInput

    show screen textInput("Enter an adjective, like 'wonderful'!")
    $ adjective = ui.interact()
    hide screen textInput

    show screen textInput("Enter a number!")
    $ testScore = ui.interact()
    hide screen textInput

    show screen textInput("Enter a year in high school, like 'sophomore' or 'first year'")
    $ highSchoolYear = ui.interact()
    hide screen textInput

    show screen textInput("Enter a location, like 'Alcatraz'!")
    $ location = ui.interact()
    hide screen textInput

    show screen textInput("Enter a superlative adjective (ending in -est), like 'easiest'!")
    $ adjectiveSuper = ui.interact()
    hide screen textInput

    w "Okay! It's time to read your story!"

    window hide
    hide w neutral
    show bg gameshowscreen
    show screen readStory()
    with fade
    $ui.interact()
    
    label ending:

    show bg gameshow

    show w neutral:
            zoom 0.2

    w "Alright, now that you have crafted your resume, your activities, and written your personal statement, your application is ready to be reviewed by our wonderful panel of judges!"

    w "...and by panel of judges, I mean me and all of the voices that speak to me. Haha!"

    w "Please wait a few seconds while we deliberate."

    menu:

        "Yes! I'm so ready!":
            w "Awesome, now let's see that decision..."
            w_slow "......................................."
            
            $renpy.pause(delay=5, hard=True)

        "No! I don't even want to know...":
            w "Me neither! Haha. Let's see that decision anyway..."
            w_slow "......................................."
            $renpy.pause(delay=5, hard=True)

    if (renpy.random.randint(1,2) == 1):
        show screen accepted()
        w "Oh wow, congradulations! It seems like all your hard work really paid off."
    
    else:
        show screen rejected()
        w "Ooh... that's gotta hurt."
        w "Oh well, guess you'll have to try harder next time."

        player "Wait, why didn't I get in?"

        w "Eh, I guess I just didn't feel like it."

        player "But how is that in any way fair?"

        w "Well, I guess it isn't. Haha"

    w "Well, now you that you have your college decision from the official College Application Game Show do you want to..."
    
    w "Go back to the high school community, with all the real people you met, even if you might not get into college."

    w "Or............"

    w "Go back to your life as an admissions officer, even after you've learned everything you have about these people you're making decisions about."

    menu:
        "What will you choose?"

        "Go back to the high school community":
            $iHaveToPutABlockHere = 0

        "Go back to your life as an admissions officer":
            $iHaveToPutABlockHere = 0

    w "That's the end! Thanks for playing!!"

    scene bg black
    hide screen accepted
    hide screen rejected

    show screen credits

    $ui.interact()


    # This ends the game.
    return 
