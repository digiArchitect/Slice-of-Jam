# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lilith = Character("Lili", image = "lilith")
define apollo = Character("Apollo",image="apollo")
define selene = Character("Scene", image="selene")
define player = Character('[name]')
default quip = ""



# The game starts here.

label start:
    $ name = renpy.input("What is your name?", default="Astra").strip()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg stars

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show selene sad

    # These display lines of dialogue.

    selene "Even now you still won’t say anything…"
    menu:
        "What is there to say?":
            show selene angry
            selene "Give me an answer, I’m begging you"
        "The stars are pretty tonight.":
            show selene sad
            selene "The stars are prettier over there [name] come with me"
        "Cats got my tongue I guess":
            show selene sad
            selene "You always know how to lighten the mood… I don’t want to lose that."




    player "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    pause

    return
