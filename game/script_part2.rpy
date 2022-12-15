label part2:
    stop music
    scene bg black
    # show  OUTSIDE LIBRARY (FIXME)

    "........."
    show w neutral:
        zoom 0.2
    pause(0.25)
    hide w neutral
    "........."
    "Some time has passed. Your head hurts terribly and you don't remember anything since you grabbed that bandaid...."
    menu wake_up:
        thoughts "That bandaid? Did I lose too much blood and pass out?"
        "Open eyes":
            "You're eyelids are too heavy"
            jump wake_up
        "Listen":
            "You hear a gentle hummm and some distant chatter."
            "Wait."
            "Was that a quiet chuckle?"

    mysterious"Ah. So you've finally regained your consciousness. I was afraid you wouldn't wake up at all."
    menu:
        "...":
            player "..."
        "Who... are you?":
            player "Who... are you?"
        "Why can't I open my eyes?":
            player "Why can't I open my eyes?"
    mysterious"No matter, no matter! I am on a limited.... schedule, so you could say."
    mysterious"I'll only say it once, so pay close attention"
    menu:
        mysterious "Ready?"
        "Ready.":
            player "Ready"
        "(Try to nod)":
            "You unsuccesfully try to nod"
        "...":
            player "..."
    mysterious "You, the lucky soul, have been selected to play, ermmmm a game."
    mysterious "Now after speanding ungodly tedious hours sorting through idiotic students' meaningless papers... YOU, "
    mysterious "yes, YOU"
    mysterious "Can finally have the Overly-Romanticized High School Story you've always dreamed of!"
    mysterious "Pretty sweet, am I right?"
    menu:
        "Go on...":
            player "Go on..."
        "What's the Catch?":
            player "What's the Catch?"
            mysterious "Well aren't you a smart one"
        "I'm Listening":
            player "I'm Listening"
        "I'm sorry, but who are you again?":
            player "I'm sorry, but who are you again?"
            mysterious "Anxious are we?"
            mysterious "Well, there's far more pressing matters you should fret about."
    mysterious "You see. If you want to return to your nice little bubble of a life,"
    mysterious "(I seem to remember you were so close to getting the promotion out of that awful department)"
    mysterious "to ever see your family, "
    mysterious "friends,"
    mysterious "or dragon--uh, bearded dragon that is--Wait no, uh dog! Or was it a cat..." 
    mysterious "Forget it! Or whatever god awful creature you humans decided to domesticate this time."
    mysterious "Point is, if you dont want to be stuck in this hellish teenage nightmare,"
    mysterious "Then you,"
    mysterious "BETTER"
    mysterious "GET IN"
    show w neutral:
        zoom 0.2
    w_slow "TO COLLEGE"
    w "Ahhhahahahaha HAHAHAHAHAHA"
    w "Ahaha HA haha... ha"
    w "ha"
    w "...."
    w "Oh, and it only counts for the university you were employed at."
    w "Unfortunately high standards they had, didn't they?"
    w "But, don't worry!"
    w "You have a whole month for that."
    w "The third month of school's already begun here at Mclaudin Prepatory School, but I've ensured your teachers will be accomadating." 
    w "Er... Mostly."
    w "You're schedule's in the front pocket of your bag, along with nessesary school supplies."
    w "Best of luck."
    w "You'll need it."
    hide w neutral

    scene bg black
    #show bg black

    narrator "You are finally able to open your eyes and find yourself in a high school hallway"
    show school hallway background at center:
        zoom 0.4
    narrator "A calendar on the wall lists the date as November 14th, 2021"
    narrator "You're in the same clothes(albeit blood free) and your work-bag-now-backpack is swung over your shoulder."

    menu where_to:
        "Travel down the hallway":
            "At the end of the hall is the restroom."
            "Your bladder and bowels feel fairly empty so you turn back."
            jump where_to
        "Walk through the door for LIBRARY":
            $iHaveToPutABlockHere = 0
    label miro:
        scene bg black
        show bg black
        show library background

        "It seems you are in the far recesses of the Mclaudin Prepatory School Library"
        "The quite numerous collection of books dots the shelves along with many storage boxes for what seems like an ambitious reorginization project."
        "You continue wandering the maze of back shelves."
        "...."
        #typing sound
        show mi
        "Hidden behind one enclave of forgotten books and storage boxes, sits a desk occupied by a shorter than average student on his computer,"
        "rapidly clicking and typing with more focus than you've seen anyone work on a google doc before."
        menu miro_introduce:
            "Clear your throat":
                "The kid doesn't seem to be able to hear you."
                "Upon closer inspection, he seems to be wearing headphones"
                jump miro_introduce
            "Tap his shoulder":
                "As you get up the courage to disturb this clearly higly productive student from his studies,"
                "You notice his backpack is inscribed with 'Miro H.'"
                "You gently tap Miro's shoulder from behind."
            "Try and get a closer look":
                "You awkwardly manuever around boxes till you are directly beside the desk, and have a clear vantage of the boy's face."
                thoughts "(He looks oddly familiar...)"
                menu view_application_miro:
                    "(Oh, I think I remember him from his application)"
                    
                    "View application":
                        show screen applicationView(12)
                        window hide
                        $ui.interact()
                        hide screen applicationView
                jump miro_introduce
            "Let him be":
                "You leave the boxes behind and wander."
                $ lost = 0;
                menu fork:
                    "You arrive at a fork in the shelves."
                    "Left":
                        "You wind thorugh the narrow shelves"
                        if lost == 0:
                            $ lost += 1
                            jump fork
                        else:
                            if lost == 1:
                                "The maze of a library has spat you out back where the boy from before is typing"
                                "Maybe you should ask him for directions?"
                                jump miro_introduce
                            else:
                                jump fork
                    "Right":
                        "You wind thorugh the narrow shelves"
                        if lost == 0:
                            $ lost -= 1
                            jump fork
                        else:
                            if lost == -1:
                                "The maze of a library has spat you out back where the boy from before is typing"
                                "Maybe you should ask him for directions?"
                                jump miro_introduce
                            else:
                                jump fork
        "The guy seems to notice your tap and continues typing at record speeds without removing his headphones:"
        m "Not now cecily!"
        m "I just finished lab reporting, and now I'm Applicating some more."
        m "Do you see this focus? This is the Miro focus."
        m "And right now, I gotta, nope, oh wait, uh, section 2, nope 3…. "
        m "1, 2, 3… and maybe that there, yeah extra-curriculars sources, section 3 is what…"
        m "Oh, right! Cecily, I should get all this finalized and Ready. To. go. In uh… "
        m "30 or so minutes."
        m "Give or take."
        m "Ah yes beautiful, oh now, the formatting isn't in chronological order. Ope, Fix that…"
        menu attention:
            "Tap Miro's shoulder again":
                "You tap Miro's shoulder again, more urgently."
            "Clear your throat loudly":
                "Bruh."
                "The kid's still wearing headphones."
                "Headphones."
                "HEADPHONES"
                "Are you reading ok?"
                "You can read at a more comftorable pace, you know."
                "Or get your eyes checked."
                jump attention
        "Miro takes off his headphones and swivels his chair to look at you in a singular fluid motion, eyes going wide."
        m "............"
        "Miro blinks at you for a split second,"
        "abruptly puts his headphones back on,"
        "completes the 360° swivel-chair-arc(so he’s back facing his computer)"
        "and resumes hacking away at the keys."
        "..." #Key clicking sound
        "You’re not sure if he notices that you can easily read the computer screen repeatedly writing 'ahhhhhhhhh.'"
        $ keyboard = 0;
        menu typin: 
            "View what Miro's writing":
                mk "ahhhhhhhhhhh"
                if keyboard == 0:
                    mk "AHHHHHHHHHHHHHHHH"
                    mk "HhhhhhhhhhhhHHHHHHhhhhhhhhhhhhhhhhhhhAHhhhhhhhhhhhhhhhhhh"
                    mk "ahahhhhhhhhhhhahhhhhhhhhhhhhahah"
                    mk "ahh"
                    mk "AHHHH"
                    $ keyboard += 1;
                    jump typin
                else:
                    mk "i got mixed up, thought you were a friend..ahhh"
                    mk "i didn't realize ahkhjbfrakldfskl"
            "Tap Miro's shoulder AGAIN":
                "Miro types away unaffected"
                jump typin
            "Remove Miro's Headphones":
                m "What the fuck?"
                player "Sorry! sorry."
                player "I didn't know how else to get your attention."
                "Miro glares at you before snatching back his headphones and returning to typing madly"
                jump typin
        mk "i really thought you were cecily i swear"
        mk "no one else ever really talks to me in the library."
        player "It's all good, don't worry"
        mk "oh ok. umahh"
        mk "you sure?"
        menu:
            "Yeah, it was kind of funny, honestly.":
                player  "Yeah, it was kind of funny, honestly."
                player "Your face?"
                player "Priceless."
                mk "lol"
                mk "truly priceless."
            "I've made so many little mistakes before, it happens":
                player "I've made so many little mistakes before, it happens."
                player "Don't stress it. It doesn't matter."
                player "See? We're chill."
                mk ":)"
        player "......"
        m "......"
        player "......"

        #__________________________
        #MIRO MENU INTERFACE-IN
        $ convo_count = 0;

        menu miro_menu:
            "Miro returns to diligently typing his document."
            "Also, I think I recognize you":
                $ answ1 = True
                player "Also, I think I recognize you"
                mk "oh um. not sure I can say the same for you, but cool."
                mk "you a new student here?"
                menu:
                    "I just transferred here.":
                        player "Oh, uh, yeah."
                        player "I just transferred here."
                        mk "ah, right."
                        mk "i remember hearing somthing about a senior transfer student."
                        mk "must be kind crazy to transfer now."
                        player "Ha. yeah. It for sure is."
                        jump miro_menu
                    "...new... student?":
                        player "...new... student?"
                        mk "so... like a transfer?"
                        player "Uh, yeah! yeah. A transfer"
                    "Well, actually it's a crazy story...":
                        player "Well, actually it's a crazy story..."
                        player "Yep, I got kidnapped by a wizard,"
                        player "And was cursed to live inside of the awkward body of a high school senior."
                        mk "sounds rough"
                        player "It is."
                        mk "so your not the transfer student there's been rumors about"
                        player "Rumors?"
                        player "I... guess I'm just that popular, what can I say."
                        "Shaking his head,"
                        jump miro_menu
            "Well, it's nice to meet you!":
                player "Well, it's nice to meet you!"
                mk "nice to meet you too! XD"
                mk "oh and i'm miro btw"
                player "Oh yeah, I saw that."
                player "Er, your bag..."
                player "It has your name on it."
                mk "that it does."
                player "My name's [playerName]"
                mk "funny, i also saw that"
                player "?"
                mk "oh um, you know you're wearing a name tag right?"
                "Looking down you see a sticker reading 'HELLO MY NAME IS [playerName]' slapped across your shirt"
                "how funny...  -_-"
                $ answ1 = True
                jump miro_menu
            "What are you working on?" if answ1:
                $ answ2 = True
                player "What are you working on?"
                narrator "Miro seems somewhat surprised that you're still here."
                mk "application"
                mk "i've got to finish this one by tomorrow."
                m "*sigh*"
                "Miro pushes the conversation notes to the bottom doc, unable to work efficiently and chat through typing"
                m "Actually, I'm just realizing now that my application is basically worthless because I don't have any extracurriculars."
                m "...at least none that I can put on here..."
                m "...and this is my top school too!"
                jump miro_menu
            "Well, I think I have to get going." if answ2:
                player "Well, I think I have to get going."
                player "I hope you're able to figure your application out!"
                m "Thanks!"
            "Wait, what do you mean about extracurriculars you can't put down?" if answ2:
                player "Wait, what do you mean about extracurriculars you can't put down?"
                m "Well..."
                m "..."
                m "Are you... like... cool?"
                player "I'd like to think so"
                m "Okay, so I've worked at a couple restaurants around here to help my mom out, but they were all under the table or whatever."
                m "...which means I haven't had time to do any sports or clubs on top of saving time to study and, like, being there for some friends who really needed it recently. "
                menu:
                    "I know what you mean, that's really rough":
                        "Miro nods eyes a bit glassy"
                        jump miro_menu
                    "Whoa, I never really knew people had jobs like that in high school.":
                        m "Yeah, honestly I know a lot of people around here who work these types of jobs."
                        m "I've honestly met most of my close friends working these restaurant jobs."
                        m "I actually only talk to a couple people here, like my friend Cecily and this guy named Jonathan that everyone seems to know."
                        m "Anyways, uh, sorry"
                        m "I don't usually just talk about stuff this openly with random people"
                        m "I think it's just the stress"
                        jump miro_menu
        m "Ope and let me know if you need help finding uh classes or whichever thing you transfer students need."
        player "Thanks! Will do."
        player "Actually how do you leave this death trap library?"
        m "Take a left than continue till the red storage boxes, go in between them, exit's on your left"
        "You give a thumbs up before heading off and following Miro's directions"

        hide mi

        window hide
        menu miro_application2:
            "Check the application again":
                show screen changedApplicationView(12)
                $ui.interact()
                hide screen changedApplicationView

        scene bg black
        show school hallway background:
            zoom 0.4

        menu leave_library:
            "You're back in the cooridor from earlier. Again there's only two options in this twisted corner of the school."
            "Return to Library":
                "You wander around the library for even longer than before."
                "You fint Miro's hidden study spot, but the guy has packed off and left now."
                "You wander through bookshelves. were there this many before?"
                thoughts "Great. You're at the desk again."
                thoughts "Hmmm what were Miro's directions again?"
                thoughts "Ah yes. Left, through, Left."
                "You finally managed to leave that treacherous hellish dimention"
                "Best not return anytime soon."
            "Go to the Bathroom down the hall":
                $iHaveToPutABlockHere = 0

    label rosalia:
        #show BATHROOM (FIXME)
        scene bg black
        show bathroom:
            zoom 0.4
        narrator "You walk into the bathroom and see a girl standing in front of the mirror, applying lip gloss very carefully."
        show ro at right

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
                "You wash your hands."
                "Just to have some sort of reason for going into the bathroom"
                "You dry your hands."
        
        rosalia "Ughah. I can't stand this school."
        thoughts "(She also seems familiar...)"
        "You sift through your old work bag that's now a backpack."
        "Commedically enough, the applications you were reading this morning are perfectly preserved."
        thoughts "All of the applications I read today came from this district..."
        window hide
        menu rosalia_application:
            thoughts "(I think she might be one of the applicants too)"
            "Look for the girl's file":
                hide window
                show screen applicationView(13)
                $ui.interact()
                hide screen applicationView
        $ i = 0;
        menu rosalia_main:
            "Hey, you wouldn't happen to be Rosalía by chance, would you?":
                player "Hey, you wouldn't happen to be Rosalía by chance, would you?"
                rosalia "Who's asking?"
                player "Me?"
                rosalia "And who are you, exactly?"
                player "Oh, I'm a new student here. I just transferred."
                rosalia "Ugh, imagine transferring here. I would NOT want to be you."
                rosalia "This school,"
                rosalia "it kinda sucks."
                $i+=1
                if i < 2:
                    jump rosalia_main
            "What's so horrible about the school?":
                player "What's so horrible about the school?"
                rosalia "Well, there aren't many extracurricular activities offered here that look good on college applications."
                rosalia "I had to do almost all of mine, like, in the community, or whatever."
                rosalia "But because there wasn't much to do here, that meant that there is a lot of pressure on community service, at least for me."
                rosalia "Thanks Mom!"
                $i+=1
                if i < 2:
                    jump rosalia_main
            "Are the people here at least nice?.":
                rosalia "I'm not entirely sure, actually."
                rosalia "I've never really had time to focus on the whole friend thing"
                rosalia "and even when I do try to talk to people, everyone seems, like, intimidated or something."
                rosalia "The only person I kinda know is Jonathan. Have you met him?"
                rosalia "He's nice. I don't know, but it doesn't really matter." 
                rosalia "I just have to get to college and get as far away from here as I can."
                $i+=1
                if i < 2:
                    jump rosalia_main
        "Rosalia Finishes putting on her lipgloss, "
        "and with a final pop of her lips, she breezes out of the bathroom."
        hide ro
        menu rosalia_application2:
            ""
            "Check the application again":
                window hide
                show screen changedApplicationView(13)
                $ui.interact()
                hide screen changedApplicationView
    label cecily:
        scene bg black
        show school hallway background at center:
                zoom 0.4

        narrator "You walk out of the bathroom, and see a girl fumbling with items in her locker. She's tossing items into an athletic bag, and as you walk by..."
        narrator "*SMACK*" #Sound effect (FIXME)
        show ce
        cecily "Oh my god! I'm so sorry!"
        menu:
            cecily "Oh my god! I'm so sorry!"
            "Don't worry, it's fine":
                cecily "Sorry, I can't believe I was that careless. I'm so late for the volleyball bus-"
            "(Help pick up some of her dropped items)":
                cecily "Oh thank you so much, you have no idea how-"
        paSystem "Volleyball players, the bus to today's tournament will be delayed until further notice."
        paSystem "On another note: If anyone has seen the bus driver, please contact office staff."
        cecily "*sigh*..."
        cecily "Well, I guess I rushed for nothing."
        narrator "She sits down next to her locker, catching her breath"

        $answ1 = False
        menu cecily_main:
            "She also seems familiar. Check her application":
                window hide
                show screen applicationView(11)
                $ui.interact()
                hide screen applicationView
                jump cecily_main
            "So, volleyball?":
                cecily "This team is so tiring..."
                cecily "I love being the captain, but between the team, classes, and filling out applications, I'm always running."
                jump cecily_main
            "Nice to meet you.":
                player "Nice to meet you."
                player "Now that you don't have to run to your game"
                cecily "I'm Cecily, I don't think we've met before"
                player "I'm [playerName], I'm new here."
                cecily "Oh, are you the senior transfer?"
                player "That's... me all right."
                cecily "Oh, cool. Have you gotten all your applications done already, then?"
                player "It's still a bit of a mystery."
                jump cecily_main
            "How are your college apps going?":
                $answ1 = True
                player "How is your application going?"
                cecily "I have no idea what to do with my essay."
                player "How so?"
                cecily "I feel like I can barely talk about anything I did in high school"
                cecily "I've poured my life into the volleyball team here"
                cecily "but that doesn't mean it's not hard to talk about..."
                cecily "with my transiton happening in the middle of it all."
                cecily "The friends I made through volleyball and all the work involved in getting to where I am is so
                important to me, but I feel like I'll have to do so much explaining if I even mention I'm a trans athlete."
                jump cecily_main
            "What makes you feel like you'll have to explain so much?" if answ1:
                player "What makes you feel like you'll have to explain so much?"
                cecily "I guess it's just that people have made it such an issue."
                cecily "It stresses me out every day, and I have no clue who's going to be reading this"
                cecily "Like, even a bunch of 'well meaning, progressive people' don't know anything about how my life works."
                cecily "I end up feeling like I have to walk them through every step of understanding basic things about me."
                jump cecily_main
            "Your friends sound really awesome and supportive at least." if answ1:
                player "Your friends sound really awesome and supportive at least."
                cecily "Yeah, My friends are a huge help, especially Miro."
                cecily "Despite being busy literaly all the time, he's dropped everything more than once to help when I've been overwhelmed by everything."
                menu:
                    player "Oh, I met Miro earlier! He seemed..."
                    "Introverted":
                        cecily "Yeah, I think that's a lot of peoples' first impression of him."
                        cecily "But if you get to know him, you kinda figure him out."
                        cecily "He's really good at listening, and is actually willing to put in work to help his friends."
                    "Stressed":
                        cecily "Yeah, he's really worried about applications."
                        cecily "He says he doesn't have any extracurriculars he can record"
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
                play sound "audio/door.wav"
                narrator "A man zooms past you in the hallway, heading for the main entrance!"
                player "hmmmmm"
                menu:
                    "Is that... the bus driver?":
                        cecily "OH!"
                    "Wait a second......":
                        cecily "The bus driver!"
                cecily "That's definitely him. Uh, I gotta run!"
                "Cecily quickly grabs her bag and sprints after the fleeing bus driver"
        hide ce
        menu:
            ""
            "Check the application again":
                window hide
                show screen changedApplicationView(11)
                $ui.interact()
                hide screen changedApplicationView
    label jeremiah:
        scene bg black
        show parking lot background:
            zoom 0.4

        narrator "You are in the parking lot and see a guy leaning on his car with his hands crossed."
        narrator "There is music blaring from the stereo of his car."
        thoughts "(Oh, there's another applicant, I think)"

        menu:
            ""

            "View Application":
                window hide
                show screen applicationView(10)
                $ui.interact()
                hide screen applicationView
        
        thoughts "Okay Jeremiah, let's see what you're like."
        narrator "You go up to him"
        show je at right
        player "Hey, I like the music you're playing. Who is it?"
        jeremiah "Well, actually, it's an original performed by me and my band. I'm on drum set."
        $ i = 0;
        menu jeremiah_main:
            "Cool! What's your band called?":
                player "Cool! What's your band called?"
                jeremiah "Jacque Efercon. It's, like, super original."
                jeremiah "You've probably never heard anything like us before."
                player "mmmhhhhmmmmm"
                jeremiah "Jacque Efercon is the name of my dog. I got Jacque Efercon 4ish years ago when he's a small lil pupster."
                jeremiah "He's been our bands mascot ever since. We've kind of all grown up together"
                jeremiah "Well Jacque Efercon IS my best bro first."
                $i+=1
                if i < 2:
                    jump jeremiah_main
            "Hey, I'm [playerName]":
                player "Hey, I'm [playerName]. And your band seems really..."
                player "...interesting..."
                jeremiah "Oh, I'm Jeremiah by the way."
                "You nod."
                $i+=1
                if i < 2:
                    jump jeremiah_main
            "Does your band look good on college applications?":
                player "Does your band look good on college applications, then?"
                jeremiah "Oh yeah, I guess it could. I didn't put it on my application though, because I'm basically guarunteed to get into my top school."
                jeremiah "Both of my parents went there, and they donate like, a couple hundred grand every year too."
                jeremiah "If I don't get in, then the admissions office must have been taken over by aliens or something."
                player "It sounds like you've got everything figured out then."
                jeremiah "Yeah basically. What about you, what are your plans for after high school?"
                menu:
                    player "Oh, uhhh..."
                    "I'm not really sure.":
                        jeremiah "oof. Well you better figure that out soon"
                        jeremiah "If not, you could end up just sitting around all day"
                    "I just transferred here so I think I'm going to try to get my bearings before I make any concrete plans.":
                        jeremiah "So why'd your parents move yah schools so late in the game?"
                        jeremiah "You do anything to piss them off so badly?"
                        player "....."
                    "I might take a gap year or start working.":
                        jeremiah "Pff, good luck with that."
                        player "What's that supposed to mean?"
                        jeremiah "I just meant like, my dad always says that if you don't go to college right after high school, then you're just lazy and going to end up a nobody."
                        thoughts "!!!!"
                        player "Wow, okay..."
                $i+=1
                if i < 2:
                    jump jeremiah_main
        player "It's been... insightful talking to you. I'll see you around."
        jeremiah "Yeah, see ya!"
        narrator "He turns the music back up"
        hide je
        menu:
            "View Application":
                window hide
                show screen changedApplicationView(10)
                $ui.interact()
                hide screen changedApplicationView
        thoughts "(How much does this really tell you about a person?)"
        menu screamin:
            "SCREAM":
                "You let out an extremely satisfying burst of now externalized previously internalized rage"
                player"AHEHHEHAHHHEHAHHHESHESWESHAHAHAAAAAAAAAAWWWWWWWWWW"
                jump screamin
            "Go to Lunch":
                $iHaveToPutABlockHere = 0

    label jonathan:
        scene bg black
        show lunch room background:
            zoom 0.4
    
        narrator "You end up in the cafeteria. You quickly notice there is one person that has captured the attention of many."
        show jo
        thoughts "(Hmmm... that seems like someone else from the applications I should talk to. But who are they?)"

        menu:
            ""
            "View Application":
                window hide
                show screen applicationView(14)
                $ui.interact()
                hide screen applicationView

        thoughts "(Oh! So this is *the* Jonathan that some of the other applicants mentioned.)" 
        thoughts "(Now what do I not know about you?)"
        narrator "You approach him."
        player "Hey, my name is [playerName], are you Jonathan?"
        jonathan "Yeah, I'm Jonathan, live and in the flesh!"
        jonathan "And hi, [playerName], it's nice to meet you. Are you new here?"
        thoughts "(This is starting to feel like Groundhog Day...)"
        player "Yeah, I just transferred."
        jonathan "Ah, that makes sense. You see, I kinda know everyone around here. That's my thing, I guess."
        player "How did you get to know everyone so well?"
        player "Do you play a lot of sports, or are you in a bunch of clubs?"
        jonathan "Not really, haha!"
        jonathan "I just really like going to school events. There's just more opportunities to get to know people."
        jonathan "Plus, once I get to know people, it's even more fun ot go support them at their events!"
        player "Oh, wow. It's awesome that you're so supportive of your friends."
        jonathan "You know what, there's actually a big volleyball game tonight. Are you planning on going?"
        jonathan "It would be a great way for you to meet some people."
        jonathan "I'd be happy to bring you along, if you'd like."
        thoughts "(He seems really nice. The kind of person I'd like as a friend...)"
        hide jo

        menu:
            ""
            "View Application":
                window hide
                show screen changedApplicationView(14)
                $ui.interact()
                hide screen changedApplicationView

        menu:

            ""

            "Go to P.E.":
                $iHaveToPutABlockHere = 0
        show gym background:
            zoom 0.4

        narrator "As you enter the gym, you see a dodgeball heading directly for your head!"

        narrator "*SMACK*"

        show bg black with fade

        jump part3

            
