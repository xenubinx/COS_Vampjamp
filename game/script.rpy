# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aurel")
define l = Character("Lark")
define m = Character("Micah")
define s = Character("Isadora")
define p = Character("[mc]")




image splash1 = "splash1.png"
image splash2 = "splash2.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash1 
    with dissolve
    with Pause(0.5)

    play sound "honk.ogg"
    show splash2 with vpunch
   
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    "Test"
    "Twest test taahf"

    

    # This ends the game.

    return
