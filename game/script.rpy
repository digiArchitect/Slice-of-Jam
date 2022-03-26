# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lilith = Character("Lili", image = "lilith")
define apollo = Character("???",image="apollo")
define selene = Character("Selene", image="selene")
define player = Character('[name]')
define outline = Character(None,
                            what_size=60,
                            what_outlines=[(3, "#FF00FF")],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_xalign=0.5,
                            window_yalign=0.5)
define quips = []
default gameName = "Game Name"



# The game starts here.

label start:
    scene black
    play music "audio/ooowee.mp3"
    $ name = renpy.input("What is your name?", default="Astra").strip()


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg stars with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show selene sad with dissolve

    # These display lines of dialogue.

    selene "You still won’t say anything…"
    menu:
        "What is there to say?":
            selene "Give me an answer, I’m begging you."
            python:
                quips.append("I've got nothing to say")
        "The stars are pretty tonight.":
            selene "The stars are prettier over there [name] come with me."
            python:
                quips.append("haha you're brighter than the sun")
        "Cats got my tongue":
            show selene sadlaugh
            selene "You always know how to lighten the mood…"
            selene "I don’t want to lose that."
            python:
                quips.append("Cats got your tongue?")





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

    hide selene  with dissolve
    player "I'm sorry"
    "I loved you too"
    call initMonologue
    return



label initMonologue:

    scene black with fade
    "We both knew it wouldn’t work, but she wanted me to leave with her."
    "I had to break it off right?"
    "Right?"
    "Keeping things going wouldn't be fair to me, or to her."
    "..."
    "I dont know."
    "I just don’t know ..."
    "What the fuck I’m gonna do now."

    call evilwizardman
    return


label evilwizardman:
    scene bg park
    "???" "What’s got you down, sport?"
    outline "LAME ENDING"
    call credits
    return







label lameEnding:
    apollo "Ho ho ho! I knew you would make the right choice. At the drop of the hat, I will fix your prob-"
    player "I said no."
    apollo "You... you said no?"
    player "I’m going to process my emotions in a healthy way. Talking with friends, excercising. I don’t want any shady business. Go away."
    apollo "Well then… I suppose I’ll be off."
    player "Good. I’m off then."
    return



label credits:
    #Shoutout to DaFool on lemmasoft for the template credit code
    scene bg stars #replace this with a fancy background
    #I have no idea how to make sure it doesnt past the letter count
    show cred at Move((0.5, 3.0), (0.5, 0.0), 25, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show game:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide game
    with Pause(20)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return
init python:
    #The appending is purely stylistic I just hate it when code goes over
    #the character count when I know how to deal with it lol
    credits = [['Art', 'Zach Zhou'], ['Story', 'Ben Brown']]
    credits.append(['Story', 'Kevin Jeudy'])
    credits.append(['Story', 'Jylah Bah'])
    credits.append(['Programming', 'Jylah Bah'])
    credits.append(['Music', 'Ben Brown'])
    credits.append(['Music', 'Sumant Sagar'])
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Created for:\n Northeastern Slice of Jam{size=80} \n"
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()  #Don't forget to set this to your Ren'py version

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    #image jam = Text("{size=80}Created for Northeastern Slice of Jam 2022",
    image game = Text("{size=80}game name", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
