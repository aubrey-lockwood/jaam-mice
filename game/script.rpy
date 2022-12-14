# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define default_speed = 70

define w = Character("Wizard", who_color="#13D1E9", what_slow_cps=default_speed, what_slow_abortable=True)
define boss = Character("Boss", who_color="#F6B414", what_slow_cps=default_speed, what_slow_abortable=True)

define narrator = Character("", who_color="#209D02", what_slow_cps=default_speed, what_slow_abortable=True)
define thoughts = Character("", who_color="#C55226", what_slow_cps=default_speed, what_slow_abortable=True)

define miro = Character("Miro", who_color="#5032c7", what_slow_cps=default_speed, what_slow_abortable=True)
define rosalia = Character("Rosalía", who_color="#d42f68", what_slow_cps=default_speed, what_slow_abortable=True)
define cecily = Character("Cecily", who_color="#6197ed", what_slow_cps=default_speed, what_slow_abortable=True)

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

    define player = Character("[playerName]")

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

    label part2:
        stop music
        scene bg black
        # show  OUTSIDE LIBRARY (FIXME)

        narrator "You open your eyes and find yourself staring at the door to the library in a high school."
        narrator "A calendar on the wall lists the date as November 14th, 2021. People are trying to finish up their college applications."

        thoughts "(Where am I? Is this a school? Am I... a student here?)"
        thoughts "(What is going on?)"

        menu enter_library:
            ""

            "Walk through the Door":
                $iHaveToPutABlockHere = 0
        label miro:

            # VIEW OF MIRO AT TABLE (FIXME)

            thoughts "(I think I recognize him. Where do I recognize him from?)"

            # GET CLOSER TO MIRO (FIXME)

            thoughts "(Oh, I think I remember him from his application)"

            menu view_application_miro:
                "(Oh, I think I remember him from his application)"
                
                "View application":

                    show screen applicationView(12)
                    window hide

                    $ui.interact()

                    hide screen applicationView


            thoughts "(I feel like I should talk to him)"

            player "Hey, I think I recognize you"

            miro "Oh, hi. I'm not sure I can say the same for you. Are you a new student here?"

            player "Oh, uh, yeah."

            player "I just transferred here."

            narrator "He goes back to his work, and looks to be ending the conversation"

            menu pester_miro:
                narrator "He goes back to his work, and looks to be ending the conversation"

                "My name's [playerName]":

                    miro "Hi. I'm Miro."

            player "Are you working on an application?"

            narrator "He seems somewhat surprised that you're still here."

            miro "Yeah, I have to finish this one by tomorrow."

            miro "*sigh*"

            miro "But actually I'm just realizing now that my application is basically worthless because I don't have any extracurriculars."

            miro "...at least none that I can put on here..."

            miro "...and this is my top school too!"

            player "Wait, what do you mean about extracurriculars you can't put down?"

            miro "Well..."

            miro "..."

            miro "Are you... like... cool?"

            player "I'd like to think so"

            miro "Okay, so I've worked at a couple restaurants around here to help my mom out, but they were all under the table or whatever."

            miro "...which means I haven't had time to do any sports or clubs on top of saving time to study and, like, being there for some friends who really needed it recently. "
                
            player "Whoa, I never really knew people had jobs like that in high school."

            miro "Yeah, honestly I know a lot of people around here who work these types of jobs."

            miro "I've honestly met most of my close friends working these restaurant jobs."

            miro "I actually only talk to a couple people here, like my friend Cecily and this guy named Jonathan that everyone seems to know."

            miro "Anyways, uh, sorry"

            miro "I don't usually just talk about stuff this openly with random people"
            
            miro "I think it's just the stress"

            player "Well, I think I have to get going. I hope you're able to figure your application out!"

            miro "Thanks!"

            miro "and uh... let me know if you need help finding classes or whatever."

            player "Thanks! Will do."

            window hide

            menu miro_application2:
                "Check the application again":
                    show screen changedApplicationView(12)
                    $ui.interact()
                    hide screen changedApplicationView

            menu leave_library:
                "Leave Library?"

                "Go to the Bathroom":
                    $iHaveToPutABlockHere = 0

        label rosalia:
            
            #show BATHROOM (FIXME)

            

            narrator "You walk into the bathroom and see a girl standing in front of the mirror, applying lip gloss very carefully."

            narrator "You almost meet eyes, but you look away after she gives you an intimidating look."

            #show Rosalia (FIXME)

            menu:
                narrator "You almost meet eyes, but you look away after she gives you an intimidating look."

                "Leave":
                    rosalia "Where do you think you're going?"

                    player "Uh, what?"

                    rosalia "Oh, I just meant like..."

                    rosalia "You don't have to leave just because I'm here."

                    player "Okay..."

                    player "...thanks?"

                "Stay":
                    $iHaveToPutABlockHere = 0
            
            thoughts "(Wait, I think she might be one of the applicants too)"
            window hide
            menu rosalia_application:
                thoughts "(Wait, I think she might be one of the applicants too)"

                "View Application":
                    hide window
                    show screen applicationView(13)
                    $ui.interact()
                    hide screen applicationView

            thoughts "(Maybe I should talk to her, like I talked to Miro."

            player "Hey, you wouldn't happen to be Rosalía by chance, would you?"

            rosalia "Who's asking?"

            player "Me?"

            rosalia "And who are you, exactly?"

            player "Oh, I'm a new student here. I just transferred."

            rosalia "Ugh, imagine transferring here. I would NOT want to be you."

            rosalia "This school kinda sucks."

            player "What do you mean?"

            rosalia "Well, there aren't many extracurricular activities offered here that look good on college applications."

            rosalia "I had to do almost all of mine, like, in the community, or whatever."

            rosalia "But because there wasn't much to do here, that meant that there is a lot of pressure on community service, at least for me."

            rosalia "Thanks Mom!"

            player "Well, how are the people here? It seems like they're pretty nice."

            rosalia "I'm not entirely sure, actually."

            rosalia "I've never really had time to focus on the whole friend thing"

            rosalia "and even when I do try to talk to people, everyone seems, like, intimidated or something."

            rosalia "The only person I kinda know is Jonathan. Have you met him?"

            rosalia "He's nice. I don't know, but it doesn't really matter." 
            
            rosalia "I just have to get to college and get as far away from here as I can."

            #FINISH ROSALIA SECTION (FIXME)

        label cecily:
            
            narrator "You walk out of the bathroom, and see a girl fumbling with items in her locker. She's tossing items into an athletic bag, and as you walk by..."
            
            narrator "*SMACK*" #Sound effect (FIXME)

            cecily "Oh my god! I'm so sorry!"

            menu:
                cecily "Oh my god! I'm so sorry!"

                "Don't worry, it's fine":
                    $iHaveToPutABlockHere = 0

                "OW!":
                    $iHaveToPutABlockHere = 0
            
            cecily "Sorry, I can't believe I was that careless. I'm so late for the volleyball bus-"

            paSystem "Volleyball players, the bus to today's tournament will be delayed until further notice."

            paSystem "On another note: If anyone has seen the bus driver, please contact office staff."

            cecily "Well, I guess I rushed for nothing."

            narrator "She sits down next to her locker, catching her breath"

            thoughts "(Another person from the applications! I should check hers again...)"

            menu:
                "(Another person from the applications! I should check hers again...)"

                "View application":
                    window hide                    
                    show screen applicationView(11)
                    $ui.interact()
                    hide screen applicationView


            cecily "This team is so tiring..."

            cecily "I love being the captain, but between the team, classes, and filling out applications, I'm always running."

            cecily "I'm Cecily, I don't think we've met before"

            player "I'm [playerName], I'm new here."

            cecily "Oh, cool. Hopefully you've got all your applications all figured out already."

            player "How is your application going?"

            cecily "I have no idea what to do with my essay."

            cecily "I feel like I can barely talk about anything I did in high school"

            cecily "I've poured my life into the volleyball team here, but it's so hard to talk about, with my transiton happeing in the middle of it all."

            cecily "The friends I made through volleyball and all the work involved in getting to where I am is so
            important to me, but I feel like I'll have to do so much explaining if I even mention I'm a trans athlete."

            player "What do you mean?"

            cecily "I guess it's just that people have made it such an issue."

            cecily "It stresses me out every day, and I have no clue who's going to be reading this"

            cecily "Like, even a bunch of 'well meaning, progressive people' don't know anything about how my life works."

            cecily "I end up feeling like I have to walk them through every step of understanding basic things about me."

            player "That sounds difficult. How did you manage that?"

            cecily "My friends are a huge help, especially Miro."

            cecily "Despite being busy literaly all the time, he's dropped everything more than once to help when I've been overwhelmed by everything."
            
            player "Oh, I met Miro earlier! He seemed..."

            menu:
                player "Oh, I met Miro earlier! He seemed..."

                "Cold":
                    cecily "Yeah, I think that's a lot of peoples' first impression of him."

                    cecily "But if you get to know him, you kinda figure him out."

                    cecily "He's really good at listening, and is actually willing to put in work to help his friends."

                "Stressed":

                    cecily "Yeah, he's really worried about applications."

                    cecily "He says he doesn't have any extracurriculars he car record"

                    cecily "It's honestly crazy to me that anyone could look at him and think he's not doing enough."

                    cecily "I usually worry he's doing too much..."

                    cecily "Not only does he literally work jobs to support his family, but he's the kind of person to really 
                    put in work to support his friends."

                    player "He sounds like a really good friend"

                    cecily "Yeah, between him and Jonathan, I've got a lot of support here"

                    player "People keep mentioning Jonathan. How is he?"

                    cecily "Oh, Jonathan is great! He's kinda involved in everything here a little bit."

                    cecily "Like, he's not on the volleyball team or anything, but he does scorekeeping for our games."

                    narrator "Suddenly, a door slams open" #Sound effect? (FIXME)

                    narrator "A man zooms past you in the hallway, heading for the main entrance!"

                    cecily "Is that... the bus driver?"

                    cecily "OH!"

                    cecily "That's definitely him. Uh, I gotta run!"

                    narrator "Cecily quickly grabs her bag and sprints after the fleeing bus driver"


    
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
