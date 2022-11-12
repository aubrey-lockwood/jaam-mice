# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("A random student")

# The game starts here.
label start:

    # Show a background.
    # add a file to the images directory to show it.
    scene bg black
    show part1
    
    play music "audio/office.mp3"

    # These display lines of dialogue.
    "Welcome to your office. As a college admissions officer, you'll be deciding whether to admit applicants to your university"
    
    stop music fadeout 1
    with Dissolve(0.5)
    scene bg black
    show part2

    "Next, you'll find yourself back in high school, meeting unique people and choosing how to create your own college application"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy

    e "Hello there! You must be the new transfer student!"
    e "Ope, Gotta run. See yah! Don't be late for class!!!"

    hide eileen happy

    with Dissolve(0.5)
    scene bg black
    show part3

    "Finally, mysterious magic will take you to a bizarre, high stakes game show"

    # This ends the game.
    return
