# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lillith = Character("Lilli", image = "Lilli")
define eckle = Character("Eckle",image="eckle")
define selene = Character("Selene", image="Selene")
define player = Character('[name]')
define lola = Character('Lola', image="Lola")
define outline = Character(None,
                            what_size=40,
                            what_outlines=[(3, "#FF00FF")],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_xalign=0.5,
                            window_yalign=0.5)

default gameName = "Game Name"
image bg starryTwo = "starsTwo.png"
image bg starryOne = "starsOne.png"
image bg dayPark = "park daylight.png"
image bg nightPark = "park night.png"
image bg bar = "bar.png"
transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0






# The game starts here.

label start:
    scene black
    play music "audio/melancholy.mp3"
    $ name = renpy.input("What is your name?", default="Astra").strip()
    $ barName = "TJ's"


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg starryTwo with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show selene sad with dissolve


    # These display lines of dialogue.

    selene "You still won’t say anything…"
    menu:
        "What is there to say?":
            selene "Give me an answer, I’m begging you."
        "The stars are pretty tonight.":
            selene "The stars are prettier over there [name] come with me."
        "Cats got my tongue...":
            show selene sad-smile with dissolve
            selene "You always know how to lighten the mood…"
            selene "I don’t want to lose that."




    show selene sad with dissolve
    player "..."
    player "You know I can't go with you selene."
    selene "Are we really going to throw what we have away?"
    selene "Is this the way that you want this to end?"
    player "My answer won’t change. I can't put my life on hold for you."
    player "Besides, do we even have anything to throw away?"
    show selene sad-smile with dissolve
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
    selene "Please never forget that."
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
    scene bg dayPark with fade
    show eckle neutral with fade
    play sound "audio/poof.mp3" volume 1.0
    "???" "What’s got you down, sport?"
    "Huh?"
    "What was that?"
    "???" "Don't play coy, sport!"
    eckle "It's me!"
    player "Do..."
    player "Do I know you?"
    eckle "Dont't joke, kid! You know me!"
    show eckle smile with dissolve
    play music "audio/eckleTheme.mp3" fadeout 1.0
    eckle "Your old pal Eckle!"
    eckle "Seems you're down on youre luck, eh?"
    "Anyone could guess that.. I probably look pathetic."
    eckle "Lady troubles?"
    "..."
    eckle "Don't worry, champ! I have sure got the fix for you!"
    player "I dont want a fix. I want to be with Selene."
    eckle "But she’s gone now, isn’t she? Far, far away? Never to be seen again?"
    "How did he know that?"
    "Who the fuck is this guy?"
    player "I'm leaving."
    eckle "Fine then! Leave! Then you’ll never see what could’ve been!"
    player "What could've been?"
    eckle "Aha! I see I’ve piqued your interest! Now beg me to tell you more!"
    player "Don't push your luck."
    eckle "There may be a quick fix for your loneliness!"
    eckle "All you have to do is drink this potion and the void in your heart will be no longer!"
    eckle "So, what do you say to my proposal?"
    menu:
        "Drink it":
            eckle "Ho ho ho! I knew you would make the right choice. At the drop of the hat, I will fix your problem! Just drink up!"

        "Don't drink it":
            jump lameEnding
    "You drink the potion."
    eckle "Good luck!"
    hide eckle with fade
    eckle "AHAHAHAHAHAHA!!!"
    scene black with fade
    player "What a sketchy guy… I guess I’ll go home then…"
    jump scene4

    return

label scene4:
    "A couple days later....."
    scene bg nightPark with dissolve
    play music "audio/maintheme.mp3" fadeout 1.0
    player "God, what a busy day. I didn’t think that project would take so long."
    player "I haven’t even looked at the time. It’s probably two a.m. already…"
    "???" "Whoa! Watch out!"
    player "Ouch..."
    show lilli neutral with dissolve
    "???" "I’m so sorry! I didn’t mean to run into you! I wasn’t looking where I was-"
    player "It’s fine, just watch where you’re going next time. Seriously, it’s really not a big deal. I just scraped my knee a little."
    "???" "What are you doing out this late anyway?"
    player "I could ask you the same question. What is a stranger doing running into people in the middle of the night?"
    "???" "Fine. Then I’ll tell you my name, and then we won’t be strangers anymore."
    player "That wasn't my point-"
    lillith "I’m Lilli! What’s your name?"
    player "Uhh [name]."
    lillith "[name]! Thats a nice name !"
    player "Thanks. My parents gave it to me."
    show lilli smile with dissolve
    lillith "Hah! You've got jokes!"
    show lilli neutral with dissolve
    lillith "You still haven’t answered my original question. What are you doing out at such an ungodly hour?"
    player "I had a project I was working on that ran late. What about you?"
    lillith "Not much of a talker, huh?"
    lillith "Anyways, I was at TJ's Bar."
    player "TJ's, huh? I haven't been."
    lillith "We should go sometime!"
    "We?"
    "Who does she think “We” is anyway? I just met her!"
    player "Uhh, maybe not... I literally just met-"
    show lilli smile with dissolve
    lillith "How about this park instead? I like nature, too! How about it? 8 p.m. tomorrow!"
    player "Wait it's not that-"
    show lilli smile at right with move
    lillith "Sounds like a plan!"
    lillith "Don't leave me hanging!"
    hide lilli smile with dissolve
    scene black with fade
    "What just happened?"
    "Did a girl just run into me and then ask me out on a date?"
    "That's not a real thing that happens."
    "Wait. That sketchy guy from last night… the potion…"
    "I thought it was all fake… could it have been real?"
    jump scene5










    return


label scene5:
    "I shouldn’t have even come here. This is stupid."
    scene bg dayPark with fade
    "8pm was the time she said… I might be a few minutes late, but she shouldn’t have left by now."
    "Shit, did I even get the time right? It was 8 right-"
    lillith "[name]! Hey~!"
    player "Lilli?"
    show lilli neutral with dissolve
    lillith "Of course it’s me, silly! What, you thought I’d flake on you?"
    player "Uh-Well-I"
    lillith "Its fine, I get it!"
    lillith "Meeting new people is always a little stressful."
    lillith "But don’t worry, you don’t have to be anxious with me."
    show lilli smile with dissolve
    player "... Thank you"
    show lilli neutral with dissolve
    lillith "No need for thank yous! You’re doing the same for me, right?"
    player "Uh- Yeah!"
    player "So..."
    menu:
        "You wanna start walking now?":
            show lilli smile with dissolve
            lillith "Oh, did you think up a route for us? You’re so thoughtful!"
            lillith "I like that."
            player "…Of course! Can’t stand here all night, right? Gotta keep it interesting."
            "Lilli takes your hand"
            lillith "Well then, show me the way, Mr. Interesting."
        "How are you?":
            lillith "I’m good, thank you for asking. You’re such a sweetheart!"
            show lilli smile with dissolve
            lillith "I’m sure I’ll feel better than ever, after tonight."
            player "I feel the same. Talking with you feels… nice."
            lillith "Glad to hear it! We’ve got plenty to go over~"

        "You look great tonight":
            lillith "Oh, you really think so? I did do my best, just for you."
            show lilli smile with dissolve
            lillith "You’re looking pretty good yourself, sweetheart~"
            player "Hah, thanks. Makes us a good pair, doesn’t it?"
            lillith "You do have a point… I wonder what else we have in common?"
    hide lillith with dissolve
    scene black with fade
    "Me and Lilli talked for a while. We actually shared a lot of interests, and even our lives up to that point had been super alike."
    "Huh..."
    "I really just… met someone like this in the park?"
    "Wait. No way it was that stupid potion..."
    "What was even in that shit anyway? Food coloring?"
    scene bg nightPark with dissolve
    show lilli neutral with dissolve
    lillith "What's wrong, [name]? Get Jinxed?"
    player "Wh-Huh?"
    lillith "[name], [name], [name]! There, now you can talk to me again!"
    lillith "What's on your mind?"
    player "Oh, its nothing! Just..."
    menu:
        "How nice your lips look.":
            jump flirt
        "The best way to end the night.":
            jump flirt
        "...Potions.":
            lillith "Hm?"
            lillith "What are you even talking about!?"
            player "Oh- I was just- Uh-"
            show lilli smile with dissolve
            lillith "Oh I know!"
            lillith "‘Potions’ is code for drinks, right? Is that your way of inviting me out for a second date?"
            lillith "You can be direct about that sort of thing, sweetheart! I’m happy to accept~"
            "…I didn’t even say anything!"
            "I wanted to mention the weird guy from yesterday, but…"
            "Nah, I’ll just go with this. Don’t wanna self-sabotage."
            player "…Yeah! You totally got it!"

    player "In that case, we can make plans for another date?"
    lillith "Of course! I’d love to do this again."
    lillith "But before I go…"
    show lilli smile at bounce
    "!!!!!!!!"
    "She kissed me on the forehead!! What the hell!? Why!?"
    "…Is this real!?!?"
    lillith "Ahaha! You’re bright red! Surprised you, didn’t I?"
    "Don’t worry. We’ll continue this next time~"
    show lilli smile at right with move
    hide lilli dissolve
    player "W-wait!"
    player "…She’s gone."
    player "Ahh, this is fucking insane!"
    jump scene6
    return

label flirt:
    lillith "Oh? Are you trying to tell me something, [name]~?"
    show lilli smile with dissolve
    lillith "You’ll have to be more direct than that."
    "Should I just start to lean in? Or should I ask first? Shit, shit…!"
    lillith "Well… I can’t say I don’t feel the same."
    lillith "But I think we should learn more about each other first."
    lillith "Can't rush into a relationship, can we?"
    player "Well, yeah. You’re totally right."



label scene6:
    "I can’t believe Eckle’s potion worked so well. That has to be it right? There’s no way someone so cute and cool would be into me."
    "Almost makes me forget about Selene."
    "I don’t want to think about her right now. I should go somewhere to get it off my mind…"
    "I should go to TJ's. If its good enough for Lilli its good enough for me!"
    scene bg bar with dissolve
    player "Wow… Place looks nice. Lilli has great taste!"
    player "Right, I’m here to numb my head. Time to get to it, then."
    "As I sat down, the bartender approached."
    play music "audio/melancholy.mp3"
    show lola smile with dissolve
    "Bartend" "What can I get you?"
    "Wow, she’s got great style. Suits this place well, I guess…"
    "Heheh. ‘Suits’."
    menu:
        "Something Strong":
            "Bartender" "I hear you. Martini coming up."
        "Something Light.":
            "Bartender" "Lets get you a Bloody Mary."
        "Suprise me":
            "Bartender" "Seems like you'd been in the mood for a Piano Man."
    "..."
    "This seems weirdly familiar?"
    "Think I read online getting that feeling has to do with memory encoding failure."
    "Bartender" "Cat's got your tongue?"
    player "Oh, ah, no- Its nothing."
    player "Just trying to keep my memories straight."
    "Bartender" "At a bar? Haha, might be a little hard."
    lola "By the way, name’s Lola. Like the bunny."
    lola "You?"
    player "Ah, right. I’m [name]. Nice to meet you."
    lola "Same here!"
    lola "Here’s your drink."
    player "Thank you."
    "Well, this’ll do it. Bottoms up."
    scene black with fade
    "..."
    "..."
    "..."
    scene bg bar with dissolve
    "I’ve had a few drinks while talking with Lola. Getting woozy."
    "…Perfect."
    lola "Got something you’re trying to forget, don’t ya?"
    player "Ah? I dunno, Lola… My heads way too fuzzy to think about that stuff."
    player "Get me another, pleaseee…"
    lola "So you were just a lightweight after all!"
    lola "You know, maybe there’s some things you shouldn’t forget."
    lola "Don’t wanna throw away what you had, no?"
    player "..."
    player "I mean, I guess so."
    player "But sometimes I feel the other way."
    player "Mayb-"
    player "!!!!"
    "She’s leaning over the counter now, looking me right in the eye."
    "Its not intense, though. Its soft. Lola’s gaze… feels like safety. Home."
    lola "Whatever you choose, just know you can always come back here."
    lola "Talking with you has been… enlightening."
    lola "I’d like to hear more."
    player "U-Um, sure thing!"
    player "Actually, I’ll probably be back here soon."
    player "Got a date coming up, definitely have to decompress after."
    lola "So you’re a playboy, are ya?"
    lola "In that case, good luck. looking forward to hearing more!"
    "…"
    "I’ll definitely come back."
    "But, time to finish up here. Lets see about the price tag…"
    "…Shit. I’m definitely gonna starve now."
    lola "…"
    lola "So, that’s it, then?"
    lola "See you again!"
    player "Yeah!"
    hide lola with dissolve
    scene black with fade
    "..."
    "..."
    "After leaving, I reflected a bit. Today was insane. Went on a date with a cute girl, and I met a super cool bartender."
    "I definitely have to see both of them again."
    "…My life is kind of a movie right now."
    jump scene7
    return

label scene7:
    scene bg starryOne with dissolve
    play music "audio/maintheme.mp3"

    "It's been a few weeks. Me and Lilli have been keeping up with each other over calls and texts."
    "We’ve been getting a little serious, so I’m anxious to make this second date go good."
    "I’m here on time, this time around. Even got a star map so we can try to find all the constellations."
    "Guess I’ll just have to wait no-!"
    "Wh-What! Everything’s dark!"
    lillith "Guess whoooo~"
    menu:
        "Jill?":
            show lilli smile with dissolve
            lillith "No silly, its me!"
        "Mom?":
            show lilli smile with dissolve
            lillith " Correct answer, my sweetheart~!"
        "Lilli?":
            show lilli smile with dissolve
            lillith "No silly, its me!"
    lillith "I see you’ve come prepared this time. You’re always so thoughtful!"
    player "Of course. You deserve only the best."
    lillith "Oh, you charmer~"
    lillith "Come on, lets take in the view."
    player "…Right!"
    "We went through all the usual pleasantries and looked at the stars together."
    "I started to feel myself really enjoying this date, laying so close to lillith."
    "I feel like I should make that known."
    player "Hey, lillith…"
    lillith "Yes, my sweetheart?"
    menu:
        "I’ve really enjoyed tonight":
            jump official

        "I think I’ve fallen in love.":
            jump official

        "*Kiss her*":
            player "Lilli…"
            lillith "[name]..."
            "I leaned in, and so did she. My heart was racing, and I felt short of breath."
            "Then… everything vanished."
            "All I could feel… were her lips against mine."
            "An eternity passed before it was over. Our eyes were locked, and neither of us wanted to look away."
    lillith "…[name]..."
    lillith "What we have… is special."
    lillith "Lets make it official."
    "I…"
    "She put her fingers on my lips"
    lillith "You don’t have to say anything yet. But when you’re ready… Come and tell me."
    "She stood and left… Leaving me with that."
    show lilli smile at right with move

    "…Holy fuck…"
    "There’s just no way this girl is real."
    "And, its happening again… I’m getting that feeling… Like I’ve been here before."
    jump scene8

    return

label official:
    lilli "So have I…"
    lilli "I think, maybe, I wanna keep doing this. For years and years."
    lilli "[name]. Lets make it official."
    return
label scene8:
    $drink = ""
    scene bg bar with dissolve
    play music "audio/melancholy.mp3"
    "I’m gonna have to make post-date bar visits a routine."
    "It really eases my mind. Going on dates with Lilli is really fun, but something about the bar is familiar and safe."
    "It lets me relax and unwind. And after tonight, I’ll need that time to think."
    show lola smile with dissolve
    lola "Hey [name]!"
    player "Hey, Lola. How are you"
    lola "Eh, its the same as always. You?"
    player "Great!. Just back from a date."
    lola "Oh right, you told me about that! So, how’d it go?"
    player "It was amazing."
    lola "Getting serious?"
    menu:
        "Yeah I think so":
            lola "That’s cool. What did you do?"

        "Not yet":
            lola "That’s cool. What did you do?"
        "Im open to anything":
            lola "That’s cool. What did you do?"
    player "We went stargazing. It was beautiful."
    lola "Stargazing. Interesting."
    player "Anyways, are you going to order anything?"
    menu:
        "Moscow Mule":
            $drink = "Moscow Mule"
        "Whiskey":
            $drink = "Whiskey"
        "Beer":
            $drink = "Beer"
    lola "One second…"
    lola "Alright, player. Here’s your [drink]."
    lola "Drink up."
    player "Thanks."
    player "If there’s one thing I can rely on in this world, it’s buying a [drink]. for double what it should cost."
    lola "Boo hoo. You're the one that came here."
    player "Fair."
    lola "The girl you’re seeing, what’s she like?"
    player "She’s beautiful. And she’s fun. And exciting. Basically perfect."
    lola "Did you give her 5 stars on yelp?"
    player "Haha. Very funny."
    lola "Seriously though, that’s great."
    player "Are you seeing anyone?"
    lola "Am I seeing anyone?"
    lola "I… I’m not sure…"
    "What’s that supposed to mean?"
    player "I understand."
    hide lola with dissolve
    scene black with fade
    "We continued to talk into the night, and once it got late I headed back home."
    jump scene9
    return
label scene9:
    scene bg nightPark with fade
    "A few days later."
    "Another late night at work… I’m not tired enough to go to bed yet though."
    "I wonder what I should do…"
    "Maybe I should call Lilli… or maybe go to the bar?"
    "I really like Lilli… I feel like she really understands me."
    "But going to the bar can be so… relaxing."
    "Maybe its the drinks, but something about the bartender feels nostalgic."
    menu:
        "Text Lilli":
            jump badending
        "Go to [barName]":
            jump ending
    return
label badending:
    "I pull out my phone and pull up Lilli’s contact. I text her asking her to meet me in the park."
    "I guess I’ll wait for a few minutes to see if she responds…"
    play audio "audio/poof.mp3"
    play music "audio/eckleTheme.mp3"
    show eckle smile with dissolve
    eckle "Looking for your date, eh?"
    player "Not you. I’m looking for Lilli. Hopefully she’ll respond to my text soon."
    eckle "Ah yes. Lilli. How is she doing anyways?"
    player "I’m not dumb. I know you had something to do with this."
    eckle "Oh?"
    player "What did that potion do? Did it make me super attractive? Will it wear off?"
    eckle "Make you super attractive, sport? It didn’t do anything to you at all."
    "What is he talking about? There’s no way I landed a girl like Lilli with dumb luck…"
    eckle "Don’t you get it? Isn’t she perfect?"
    player "I guess..."
    eckle "Maybe too perfect?"
    "What is he getting at…"
    eckle "The only thing the potion changed about you was in your mind."
    player "Oh my god…"
    eckle "Do you understand now? Lilli’s not real, [name]."
    eckle "She’s a fabrication."
    eckle "I created her in your mind."
    eckle "She’s your perfect partner."
    eckle "I saw you in a miserable state and thought I’d give you a second chance."
    eckle "I thought you would easily be able to tell it was a farce, that your true love was near this whole time."
    eckle "Maybe you were lying to yourself about how much you loved her."
    player "No… That isn’t true! I love Selene! I would do anything to get her back."
    eckle "You made your choice."
    outline "BAD ENDING"
    jump credits
label ending:
    hide dayPark with fade
    scene black with fade

    "I guess it is late… I think I’ll just go to the bar. Hopefully bartender is there."
    "A few minutes pass…"
    scene bar with fade
    show lola smile with dissolve
    lola "Hey [name]! How are you?"
    player "I’m alright, just a little tired. Long day."
    lola "I get it. What would you like?"
    menu:
        "Moscow Mule":
            $drink = "Moscow Mule"
        "Whiskey":
            $drink = "Whiskey"
        "Beer":
            $drink = "Frothy Water"
    "ill take a [drink]"
    lola "I'll get that ready for you."
    "I don’t know what it is about her, but she makes me feel so safe."
    lola "Here you are!"
    player "Thanks."
    lola "Any fun stories? Got anything to say or are you going to drink in silence?"
    player "Sorry, I just have a lot on my mind."
    "God, I must look so nervous right now."
    "Going on dates with dream girl is so fun… and yet…"
    "A part of me wants to be with bartender."
    "This shouldn’t even be an issue. I know who I should choose."
    menu:
        "Ask out bartender":
            jump trueending
        "Finish your drink and leave":
            jump alchoholic
    return
label trueending:
    player "You know what, I’m just going to say it. Bartender, I think I-"
    play audio "audio/poof.mp3"
    show eckle smile at left with dissolve
    show lola neutral at right with dissolve
    play music "audio/eckleTheme.mp3"
    eckle "Very good, [name]! Very good."
    eckle "I’m impressed."
    eckle"Looks like you were able to see through the facade."
    eckle"When I saw you looking so incredibly miserable that night I decided to give you a second chance."
    eckle"I decided to give you a second chance at what you thought was true love."
    eckle"It looks like you were right after all."
    lola "[name] do you know him?"
    eckle"Lilli was perfect, wasn’t she?"
    eckle"But there was something off."
    eckle"I’m impressed that you picked up on that. Now for your reward."
    play audio "audio/poof.mp3"
    play music "audio/melancholy.mp3"
    hide lola with dissolve
    show selene sad at right with dissolve

    eckle "I’ve turned her back."
    eckle "You knew Lola was Selene the whole time, didn’t you?"
    eckle "I’ve given you a gold opportunity."
    eckle "You no longer have to be apart."
    selene "What… happened… [name]?"
    eckle "Selene! I’ve made my decision. I’m going to stay with you. No matter what it takes."
    eckle "and scene."
    hide eckle with fade
    selene "Where are we? What happened?"
    selene"I…"
    selene "I missed you."
    play music "audio/melancholy.mp3"
    outline "GOOD ENDING"
    jump credits
    return



label alchoholic:
    show lola neutral with dissolve
    player "Sorry for being so quiet."
    "I takes a large swig of their drink."
    player "Thanks for being a good friend, Lola."
    show lola smile with dissolve
    lola "Hah! I get paid to be here, you know?"
    player "Ouch. That one hurt."
    lola "Just kidding!"
    lola "Would you like another drink?"
    player "No, I should head home now."
    lola"See you around!"
    hide lola with dissolve
    scene bg nightPark with fade
    "What am I thinking? When did I get so greedy?"
    "I can’t believe I considered throwing away what I have with dream girl."
    play music "audio/eckleTheme.mp3" fadeout 1.0
    play sound "audio/poof.mp3" volume 1.0
    show eckle smile with fade
    eckle "Another late night walk in the park, eh?"
    player "I don’t want any of your trouble, Magician."
    eckle "You don’t want any of my trouble, boy?"
    eckle "Really?"
    eckle"Because I can recall that you drank one of my potions."
    player "Looks like I’m regretting it now."
    eckle "How was the bar, player?"
    player "You scare me."
    player "It was fine. I had a drink. I left."
    eckle "Nothing weighing on your mind?"
    eckle "No big decisions made?"
    player "What are you getting at? What do you know?"
    eckle "Do you know what that potion did, player?"
    player "Not really…"
    player "Did it make me super attractive?"
    eckle "Make you super attractive, sport? It didn’t do anything to you at all."
    "What is he talking about? There’s no way I landed a girl like Lilli with dumb luck…"
    eckle "Don’t you get it? Isn’t she perfect?"
    player "I guess…"
    eckle "Maybe too perfect?"
    "What is he getting at…"
    eckle "The only thing the potion changed about you was in your mind."
    player "Oh my god…"
    eckle "Do you understand now? Lilli’s not real, player."
    eckle "She’s a fabrication."
    eckle "I created her in your mind."
    eckle "She’s your perfect partner."
    eckle "I saw you in a miserable state and thought I’d give you a second chance."
    eckle "I thought you would easily be able to tell it was a farce, that your true love was near this whole time."
    eckle "Maybe you were lying to yourself about how much you loved her."
    player "No… That isn’t true! I love Selene! I would do anything to get her back!"
    eckle "You made your choice."
    outline "You went to the bar only to get a drink. Nothing more. Lame."
    outline "ALCOHOLIC ENDING"
    play music "audio/melancholy.mp3" fadeout 1.0
    jump credits
    return









































































label lameEnding:
    eckle "Ho ho ho! I knew you would make the right choice. At the drop of the hat, I will fix your prob-"
    player "I said no."
    show eckle neutral with dissolve
    eckle "You... you said no?"
    player "I’m going to process my emotions in a healthy way. Talking with friends, excercising. I don’t want any shady business. Go away."
    eckle "Well then… I suppose I’ll be off."
    show eckle neutral at right with move
    pause(1)
    hide eckle neutral with dissolve
    player "Good. I’m off then."
    outline "You process your emotions in a healthy way and move on with your life."
    outline "LAME ENDING"
    play music "audio/melancholy.mp3"
    jump credits
    return



label credits:
    #Shoutout to DaFool on lemmasoft for the template credit code
    scene bg starryOne #replace this with a fancy background
    #I have no idea how to make sure it doesnt past the letter count
    show cred at Move((0.5, 2.0), (0.5, 0.0), 25, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    window hide
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
    credits = [["","GAME NAME"],['Art', 'Zach Zhou'], ['Story', 'Ben Brown']]
    credits.append(['Story', 'Kevin Jeudy'])
    credits.append(['Story', 'Jylah Bah'])
    credits.append(['Programming', 'Jylah Bah'])
    credits.append(['Music', 'Ben Brown'])
    credits.append(['Music', 'Sumant Sagar'])
    credits.append(['Special Thanks', 'Aidan Pine'])
    credits.append(['Special Thanks', 'James Wintersteen Arvanitantonis'])
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
    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
