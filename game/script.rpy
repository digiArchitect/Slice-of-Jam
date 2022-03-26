# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lilith = Character("Lili", image = "lilith")
define apollo = Character("Apollo",image="apollo")
define selene = Character("Selene", image="selene")
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
            selene "Give me an answer, I’m begging you."
        "The stars are pretty tonight.":
            selene "The stars are prettier over there [name] come with me."
        "Cats got my tongue I guess":
            show selene sadlaugh
            selene "You always know how to lighten the mood…"
            selene "I don’t want to lose that."




    player "..."
    player "You know I can't go with you selene."
    show selene sad
    selene "Are we really going to throw what we have away?"
    selene "Is this the way that you want this to end"
    player "My answer won’t change. I can't put my life on hold for you."
    player "Besides, do we even have anything to throw away?"
    show selene sad
    selene "So this is it then?"
    menu:
        "Im sorry":
            player "..."
        "I didn't want it to be like this":
            player "..."
        "I guess it is":
            player "..."

    player "..."
    selene "[name] ..."
    selene "I love you."
    selene "Please never forget that"
    hide selene
    player "I'm sorry"
    "I loved you too"


    return
label evilevilwizardman:
