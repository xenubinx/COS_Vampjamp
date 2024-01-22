# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Au = Character("Aurel")
define L = Character("Lark")
define M = Character("Micah")
define I = Character("Isadora")
define MC = Character("[MC_name]")



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

    $ aurel_goodend = 0
    $ lark_goodend = 0 
    $ micah_goodend = 0
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
    

    Au "Here's how it looks with one choice."

    menu:
        "choice 1":
            pass
    
    L "Here's how it looks with two choices."

    menu:
        "choice 1":
            pass

        "choice 2":
            pass
    
    M "Three."

    menu:
        "choice 1":
            pass

        "choice 2":
            pass

        "I really want to kiss you right now.":
            pass

    I "Five with the hover background changes."

    menu:
        "The Tower"(card = "tower"):
            pass
        "The Fool"(card = "fool"):
            pass
        "Default Card":
            pass
        "The Chariot"(card = "chariot"):
            pass
        "The Lovers"(card = "lovers"):
            pass
    
    "pogchamp"

    menu:
        I "This version allows for there to still be a textbox at the bottom without looking too bad."
        "The Tower"(card = "tower"):
            pass
        "The Fool"(card = "fool"):
            pass
        "Default Card":
            pass
        "The Chariot"(card = "chariot"):
            pass
        "I really want to kiss you right now."(card = "lovers"):
            pass
    
    I "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    
    menu:
        "micah":
            jump micah

        "aurel":
            jump aurel

        "lark":
            jump lark

    return
