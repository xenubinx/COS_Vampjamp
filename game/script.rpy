# god hep my fukin soul 

define Au = Character("Aurel")
define L = Character("Lark")
define M = Character("Micah")
define I = Character("Isadora")
define MC = Character("[MC_name]")

## Temp chars
define Rl = Character("???")
define Mm = Character("???")
define L2 = Character("???")
define I2 = Character("???")
define A = Character("Andy")

image splash1 = "splash1.png"
image splash2 = "splash2.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash1 
    with dissolve
    with Pause(0.5)

    play sound "honk.ogg" volume 0.5
    show splash2 with vpunch
   
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

#defaulting some variables
default larkintro = False
default micahintro = False
default aurelintro = False

default ferriswheel_fear = False


label start:

    $ aurel_goodend = 0
    $ lark_goodend = 0 
    $ micah_goodend = 0

    # menu:
    #     I "This version allows for there to still be a textbox at the bottom without looking too bad."
    #     "The Tower"(card = "tower"):
    #         pass
    #     "The Fool"(card = "fool"):
    #         pass
    #     "Default Card":
    #         pass
    #     "The Chariot"(card = "chariot"):
    #         pass
    #     "I really want to kiss you right now."(card = "lovers"):
    #         pass
    
    stop music fadeout 9.0
    
    
    scene black with dissolve

python:
    MC_name = renpy.input(_("Please enter your name: "), default = "Alex", length = 10, exclude = '!@ #$%^&*()+={}[]:;|<>?/')

    MC_name = MC_name.strip()

$ MC_name = MC_name.title()

play music "music/music_loop_circus_upbeat.ogg"  fadein 3.0 loop    

#MC "this is a test" just had this for name legnth testing :) 
"You stand for a moment, surveying the area before attempting to go anywhere."
scene carnival with dissolve

pause (1.0)
menu: 
    "Looks Rundown":
        "You can tell this carnival has been around for a while, but this place has seen better days. It’s colorful, but all these colors have faded away due to the elements:  bright reds turning maroon, blues turning gray, yellows practically invisible."
        "If you listen closely enough you can hear the soft whines of the metal on the Ferris wheel, the sad tune of the Merry go round, the games playing broken chipper loops." 
        "You aren’t scared of clowns, but anyone would find this place unsettling. Such is the nature of things aging. It wears people down, worsening them. You suppose the same can be said for man made things."
    "Looks Fun":
        "The place has seen brighter days, but despite the signs of clear aging,  you can't help how your heart begins pattering a little faster."
        "Memories of running around dusty fairgrounds, eating sickeningly sweet fried foods, and bouncing on your top toes in line for the Ferris wheel come soaring back."
    "The atmosphere can’t be beaten, not by time or the elements. Nostalgia is one hell of a drug."

A "It’s so cool!"

"Next to you, Andy takes in the sight themselves. The two of you are here because they invited you. They wouldn’t go to the carnival all by themself, so you tagged along."

"Bending your leg, you’re still stiff from waiting over an hour to get your 'Festum Astrosum' ticket stub. It goes to show that despite what you'd thought of it, the carnival is not as abandoned as you thought it’d be."

A "Where to first?"

#TODO: menu here to choose where to go first
#TODO: create a copy paste to check whether to jump to the choice menu or go to the end of the CR 

label introchoice:

    menu: 
        "The Ferris Wheel" if larkintro == False:
            MC "The Ferris Wheel."
            jump ferriswheel
        "The Circus" if aurelintro == False:
            MC "How about the circus?"
            jump circus
        "The Arcade" if micahintro == False:
            jump arcade


label ferriswheel:
    scene ferriswheel

    #potential whistle SFX
    "Andy follows your line of sight to the giant wheel, towering over the festivities. They whistle."


    A "You sure? That's a long way up."

    menu:
        "Hell yeah!":
            "Raising a hand, Andy answers your high-five with a loud slap and a wide grin."
            A "When you're at the top of the Ferris wheel, everything in sight becomes your kingdom. And I'm ready for my moment to lord over the carnival."
            MC "From that height I think we'll be able to see the roof of my house."
        "Yeah, I think I'll be okay.":
            A "We don't have to."
            MC "I know... but it's a part of the experience. And I want to. I really do."
            A "How about this: you're free to back out up until we're actually on the ride. Deal?"
            "Andy holds their hand out for you to take, and you shake on it. The bonds of friendship couldn't break even if your fear of heights sends you running like the chicken you are."
            MC "Deal!"
        "I wanna get it out of the way as fast as possible.":
            $ ferriswheel_fear = True 
            MC "I'm pretty sure I wanna get it out of the way as fast as possible."
            A "There's no law saying we have to ride the Ferris wheel. We can skip it."
            MC "I know... but it's a part of the experience."
            A "Being scared shitless?"
            MC "Andy."
            A "What? You're scared of heights. We both know it, so there's nothing to prove."
            MC "Who goes to the carnival and doesn't ride the Ferris wheel? Let me have this."
            A "Alright, I surrender. It's your funeral."
            MC "Hey, maybe I'll make it to a higher point this time before I have to close my eyes."
            A "Ha, you never know. Today could be the day it all changes."


    "And on that note, Andy nods their head in the direction of the Ferris wheel."

    MC "Wait, my phone, I’m scared it’ll fall out of my pocket."

    MC "Can I put it in your bag?"

    A "Yeah, just stick it in there."


    "You do just that."


    A "Race ya there?"


    "Before you could answer, Andy scampers off and effortlessly weaves through the crowd of people. You follow after, albeit with less grace. You manage to keep Andy in sight while you attempt to push on ahead."

    "That is, until you try darting around a group of rambunctious kids blocking your way and crash into what feels like a brick wall. You hit the ground, landing directly on your butt, and then something small bounces off your forehead and lands in your lap."


    MC "Ow..."

    show lark neutral at center

    "Rubbing your stinging head, you finally notice the man standing over you. This must be the brick wall, you realize in a wave of embarrassment. A more colorful wall than you expected."

    "His expression doesn't reveal much at all, but he extends a hand. Your lips part and let out a breath of relief. The help up is greatly appreciated."

    "But then, his brow pinches severely and he slaps your hand away."

    show lark annoyed
    L2 "Give it back."

    MC "What?"


    "He points this time and you realize there's a shiny, red ball in your lap. You pick it up."


    MC "This thing?"

    L2 "Yes."

    show lark neutral 
    "He plucks it from your grip and promptly walks away, scanning the ground. The bells attached to his costume jingle with each step. Calling the moment baffling would've been an understatement."

    "You scramble to your feet and brush off any dirt that's stuck to your pants. A thought passes and you consider asking him what his problem is, and maybe slapping that stupid red ball out of his hand..."

    "Sighing, you push that aside and continue towards the Ferris wheel. You don't make it very far before you spot another shiny, red ball. The sight creates a twinge of guilt in your gut."


    "You cut through a group of teenages during their impromptu photoshoot and retrieve the ball before they can kick it aside. Sliding closer to the balloon dart booth, you craned your neck trying to spot any others."

    "There must be at least three of them. So where is it? You peeked in between and around the backsides of the game booths and finally caught the shine of two more red balls."

    "Holding on tightly, you hurry in the direction the strange man went. This time you wouldn't miss him. His ruffles and bright colors should stand out like a beacon in this crowd-- especially if you're looking for them."

    "And luckily, he does indeed stand out. You walk over and stop directly in front of the curled toe of his jester boots."


    MC "I'm sorry."

    show lark shocked
    "He doesn't say anything. Biting down on the inside of your cheek, you lift your gaze to catch something indiscernible clashing in his eyes."


    MC "I... I really didn't mean to crash into you and make your job difficult. Did I find them all?"

    show lark neutral

    "That nudge jolts him out of his shock and he nods. He adds the three you collected to the two in the crook of his arm. Five total."


    MC "My name's [MC_name]."

    L "Lark."

    MC "Well, it's nice to meet you, Lark."

    show lark happy
    "The corner of his mouth tugs impishly in time with a thought. He glances at the balls and then at you."


    L "Is it?"


    "Your lips press together and you try with all your might not to take the bait."


    menu:
        "Sooo, are you any good at juggling?":
            show lark faint smile
            L "I guess so..."
            "Lark picks one up with his free hand and starts tossing it high above his head. It lands perfectly in his palm and he sends it flying again, and again. All without taking his eyes off of you too."

            L "...I just do as I'm told."

            MC "That's... fair. I'd say you're a world class juggler by my standards."

            show lark happy
            "The sharp point of one of his teeth catches your eye as his smile bends. He's about to speak when the whine of the Ferris wheel starting a new rotation steals your attention."


            MC "No, no, no! I gotta go."

            show lark neutral
            "Lark catches the ball and holds it this time. All of his amusement vanishes, and he nods."

            MC "Bye Lark."
            hide lark neutral with dissolve
            "And on that note, you hurry into the moving crowd and run towards the Ferris wheel."
        "So... you work here? That must be fun.":
            show lark neutral
            "Lark's head gradually tilts to the side. You imagine that question is not what he was expecting."

            L "Is this your first carnival?"

            MC "No, but it's my first time at this one. Any recommendations?"

            "He hums and straightens his neck. And finally, Lark points at something behind him."
            show lark faint smile
            L "There's nothing special about this place, but if I had to pick... the view is nice from up there."

            "As if on cue, the metal whines and the Ferris wheel begins a new rotation."

            MC "Oh no. I'm supposed to already be there to meet my friend."
            show lark neutral
            L "..."
            "You hesitate. It's strange... a part of you doesn't want to go. And it must be obvious, because Lark shakes his head."
            MC "Bye Lark."
            L "Shoo. Get."
            "He motions for you to leave, and that feels more fitting than anything else he could have said. You laugh, and then, take off towards the Ferris wheel."
        "You slap those red balls and walk away.":
            "To hell with being the bigger person! You dive forward, but only find open air with your fingertips. Lark easily sidesteps and begins juggling."
            show lark happy
            "He raises an eyebrow, and it goes unsaid that he's daring you to try again."

            "This time your fingers curl into fists, but then the metal whine of the Ferris wheel steals your attention. Andy."
            hide lark happy with dissolve
            "Without a second thought, you run past Lark. Strangely, through all the noise, you hear a laugh. It's genuine and light, and, you're entirely certain somehow, his."

            "It's electric passing through your body, and you almost want to turn back. But what might happen if you do? You don't have an answer, so you try to forget it and move forward."


    "You find Andy near the front of the Ferris wheel line with their hands in their pockets. They turn and spot you just as quickly. Andy lifts the ribbon line marker and waves you over."


    A "There's no way it took that long to get here. What kind of trouble did you cause?"

    MC "More like I ran directly into it."

    A "Oh? Tell me more."


    "The two of you are seated on the Ferris wheel while you recount your bizarre encounter. Andy crosses their arms."


    A "So... what's the verdict? What are we thinking about this Lark and-"


    "The loud whine of the wheel interrupts their thought. Andy excitedly looks side to side, anticipating the view at the top. You two can talk about strange jugglers and your embarrassing moments later. There is plenty of time for that."
    $ larkintro = True
    if micahintro == True and aurelintro == True: 
        jump CRending
    else: 
        jump introchoice

###########################################################
###########################################################

###########################################################
###########################################################
label circus:
    #scene black with dissolve
    #pause (0.5)
    #scene circus with dissolve
    scene carnival #TODO: this needs to be fixed somehow to indicate that they arent inside the big top yet??
    MC "I know we missed the first show, but I want to check when the next one will be before we check out the rest of the place."
    A "You want to go to the circus? I didn’t think you’d be into that."

    menu:
        "Why not?":
            MC "I’ve actually never been to one."
            MC "But it sounds neat! I like magic shows, and animals! Oh! And the acrobats!"
            MC "It sounds fun! So yeah, why not? Unless you don’t want to, of course."
            A "No, no! I don’t mind! It does sound fun. It’s like watching those seal shows at the aquarium!"
        "I thought you'd like it.":
            MC "I thought you’d enjoy it! I know how much you love seals, that’s like 90\% of what you send me."
            A "Can you blame me? The way their little bodies squish into themselves…"
            A "But isn’t it sea lions that are in circuses?"
            MC "Oh yeah…"
            A "Same difference, sea lions are adorable! I’m still down."
            A "Unless you’d rather do something else first?"
            MC "No it’s good for us to check when the next show starts, then while we wait we can explore!" 


    "You grip Andy’s hand so as to not get separated in the crowds, the big top impossible to miss from where you stood."
    "As you both approach you watch as crowds continue to spill out the entrance of the tent, all delighted by the show that had just taken place."
    "As you two get closer, the true magnitude of the big top tent can’t be understated." 
    "Even in the daylight it looks incredible; you could only imagine what it would look like when lit up at night. You both had no real plans to stay that long, but you wouldn’t be mad if you were able to pay witness to it, even if for just a moment."
    A "There’s no posters outside. I guess we gotta go inside."
    A "Might just be quicker to ask someone."
    scene bigtop #actual inside of tent
    "When you both enter it’s significantly dimmer but equally as wondrous. There's so much space. Animals, just what you’d expect to see-- elephants, monkeys, and yes, sea lions-- exited stage left."
    "Even with such a wild sight, the man standing in the center ensnares your attention."
    "He stands with his hands behind his back, leaning onto his cane, andwatches the crowds disperse with a polite smile."
    A "That must be the ringleader!"
    "Andy points to where your eyes have already landed. Their hand drops to their side and they cross their arms, shaking their head."
    A "He's dressed so fancy! Man, I wish I could pull that off."

    menu: 
        "Do it":
            MC "I’m sure you could! Though everyone may think you're cosplaying Dracula or something."
            "You smirk as you say it, you can definitely imagine Andy doing such a thing. He returns your coyness with a playful smile all their own." 
            A "You say that like it’s a bad thing."
            "You can’t imagine anyone looking good in such attire in this day and age, but you can’t help but feel like the ringleader was born to wear it."
        "You'll be teased":
            A "By who?"
            MC "Me."
            A "Well, I say you should care less about what others think, Mc!"
            A "He does look really natural in it though, huh?"
            "You only nod, but you couldn’t agree more."


    "You smile to yourself when you see a child wave to the well dressed man." 
    "He speaks with the boy and his mother for a moment before waving them off. His polite smile is replaced with something much brighter. The child’s eyes brighten at that pointing to the man’s face before the mother drags the boy along."
    "Andy, being ever the opportunist, wastes no time to rush over and speak with the man."
    "You stand next to Andy as you get your first proper look at the man."
    "He's tall even as he leans in his stance. He has dark features and a curtain of black silky hair. Everything about him is sharp- from his dress to his jaw. "
    A "Excuse me! Hate to bother you, but my friend and I wanted to ask a couple of questions."
    show aurel happy with dissolve
    "The ringleader’s eyes shift down to you, and it's clear his smile is for customer service usage only. Even so, he has an undeniable presence, and you feel small beneath his gaze, even when it’s split between you two. You’re thankful for Andy to have led the conversation."
    
    Rl "It’s no bother at all. What can I help you two with?"
    "You speak at the same time as Andy, but they let you take the lead."
    MC "We were wondering when the next show starts?"
    Rl "There’s a new showing every 2 hours."
    MC "Thank you, we’ll be back then."
    show aurel smirk
    Rl "Thank you in advance for coming to the show. I do hope it’ll be to your liking."
    "Despite saying he hopes, even his velvety smile oozes confidence, like he knows you’ll love it once you see it."
    MC "I’m sure it will."

    menu:
        "Ask for his name":
            MC "Ergh… if you don’t mind me asking. What’s your name?"
            show aurel shocked
            Rl "My name?"
            "He appears genuinely surprised you'd ask, and you feel just a tad bit intrusive. Before you can tell him he doesn’t have to answer- he does."
            show aurel neutral
            Au "My name is Aurel." 
            "Aurel. What a beautiful name, much like everything else. It fits him. You wonder if it's  a stage name or the real deal, but you don’t have it in you to ask."
            show aurel happy
            Au "And you both?"
            "That surprises you, but also makes you feel better for having asked."
            MC "This is my best friend, Andy, and I’m [MC_name]."
            show aurel smirk
            Au "Well met, [MC_name] and their best friend Andy."
            "He chuckles to himself." 
        "Compliment the man":
            MC "I love your outfit!"
            show aurel shocked
            "He looks down at himself for a second before a smirk dances across his features."
            show aurel smirk
            Rl "Is that so? Or are you attempting to make fun of me?"
            "Despite what he says, he doesn’t sound offended. He sounds... amused? Like if you did, it would be more fun that way."
            MC "Oh no! Not at all, I really do think it’s neat!"
            Rl "I’m only teasing you."
            "He practically purrs out. Confirming your earlier theory. He’s like a cat playing with its food."
            "But you’ve always liked cats."
            "You exchange looks with Andy, their eyes wide as yours no doubt. A small silence falls over you all before the man breaks the silence. "
            Rl "My name is Aurel, by the way."
            "Aurel- What a beautiful name. Much like everything else, it fits him. You wonder if it's  a stage name or the real deal, but you don't have it in you to ask."
            Au "I am delighted to see childless adults taking interest in the circus."
            Au "What are your names?"
            MC "This is my best friend, Andy, and I’m [MC_name]."
            Au "Well met, [MC_name] and their best friend Andy."
            "He chuckles to himself." 

    hide aurel smirk with dissolve
    "He bows while he says it before turning on his heel. It’s an effective, if not dismissive, way to end the conversation." 
    "A wave of relief washes over you." 
    "There was a tightness growing in your chest as the conversation progressed. You don’t consider yourself an anxious person, nor socially anxious person, but, for the first time in your life you truly understood the feeling."
    "He-- Aurel-- didn’t have much to say, but his voice and demeanor was... enthralling." 
    "You suppose that’s the kind of attribute someone running a show like this would have to have." 
    "Especially, when competing with the likes of acrobats, fire hoops, and of course- sea lions balancing beach balls on their noses."
    "Though you’d also expect him to be more warm and comforting. He's  a circus performer after all. Children seem to like him–"
    "‘Maybe the problem lies with me.’ You catch yourself thinking."
    "Or perhaps, much like clowns, they don’t bring everyone comfort, and have a certain... uncanniness to them."
    "Despite these feelings, much like the thrills that came from a fair ride…"
    "You can’t wait for the next rush."
    $ aurelintro = True
    if micahintro == True and larkintro == True: 
        jump CRending
    else: 
        jump introchoice


###########################################################
###########################################################

###########################################################
###########################################################

## When go to Arcade (MC meets Micah)
label arcade:
    MC "See that game arcade over there?"
    A "Oh, how nostalgic!"
    A "Bet I'll beat you at the crane game!"
        
    "Andy nods towards the flashing neon lights of the arcade, and their grin promises a good challenge."
        
    menu:
        "As if! I'll show you my skills!":
            jump choice_skills
        
        "Aren't those crane games rigged anyway?":
            jump choice_rigged
        
    label choice_skills:
        
        "You wriggle your fingers."
        MC "I may be rusty, but muscle memory has never failed me."
        A "Famous last words!"
        
        jump arcade2

    label choice_rigged:

        "You sigh and shake your head."
        MC "Seriously, what are the chances we're going to win anything?"
        A "You know what the trick is?"
        A "After a few tries, you speak to the staff, and they 'fix' your machine."
        A "All they do is adjust the position of the plushie you want, so you can get it on the next try."
        MC "Really?!"
        

        jump arcade2

label arcade2:

    scene carnival #zoomed from main bg
    "Andy runs ahead, like an excited kid, leaving you trailing behind taking in all the surrounding lights."
    scene arcade #actual inside of arcade if we have it
    "The room is full of different machines, all blinking, beeping, waiting for you to lose your money."
    "It certainly has seen better days, but despite being on the more retro side, they all seem to work properly."
    "A few people are engrossed in the flashing lights, trying their luck at the machines."
    "You finally catch up to Andy,  their excitement spreads across their face making them look instantly younger. It reminds you a lot of your first time going to the arcade with them."
    A "Wow, this really takes me back."
    A "Oh my gosh, is that a 'Vampire Conquest III' pinball machine?!"
    "You follow Andy's eyes to an older looking machine with a vintage illustration of a vampire on the front. The dimly lit display flickers."
    A "I haven't seen one in ages! I was so into it, I ranked 2nd on it!"
    MC "Hehe, nerd."
    
    "Before Andy can gravitate towards childhood memories of beating their highscore, you see someone laying underneath the machine."
    
    MC "Sorry to burst your dreams, Andy, but I think it's being maintained."
    A "Awww.... well, later, then."
    A "I still have to beat you at a crane game!"
    A "How about... this one?"
    
    "The crane game itself seems pretty ordinary. The prizes are bat-plushies with different faces. Cute."
    "Without waiting for your answer, Andy puts a coin into the machine."
    
    A "Hmmmm... Go over there..."
    "You watch as Andy cautiously nudges the joystick on the machine to the back corner, aiming for one of the plushies that seems a little less stuck than the others."
    A "Slowly..."
    A "HA! I caught it!"
    MC "Now you just have to bring it back home!"
    "Andy has the machine's claw grasping onto the wing of a bat with a cute sleepy face on it."
    A "No pressure, it's gonna... be..."
    play sound "audio/sfx/CoS_SFX_14_machine_fail.ogg"
    #fail sound?
    A "Oh no, I dropped it!"
    MC "And so close, too!"
    A "Gimme another try."
    
    "Their second attempt fails, but they succeed at getting the bat closer to the opening. "
    "Their third try doesn't hold much luck either, as the plushie bounces off the edge of the drop box, sending it further away.  " 
    
    MC "Okay, okay, my turn."
    
    "You hip-check Andy's sulking ass to the side and grab the controls."
    "Focused, you slide a coin into the machine, and watch the crane slide to the right side as you push the controls."
    "You want the bat with the angry face near the front glass."
    
    MC "Steady... and..."
    
    "The crane lowers down, and--"
    # get a clunk sound from EJ?
    MC "What?"
    MC "It's stuck?"
    MC "Come on!"
    "You stare helplessly at the angry bat again, frustrated because every try you've both made so far has been a failure."
    
    "Before you can slap the controls out of frustration, someone appears at your side."
    show micah neutral  with dissolve 
    #TODO: Add at right, but set custom position abt 75% across the screen
    Mm "Is it stuck again?"
    "You start to nod, but before you can open your mouth to speak, the man cuts you off."
    Mm "Yeah, that happens sometimes. Lemme see."
    
    "The young man just pushes you away gently, and gets to work at a panel below."
    "Is he...  the maintenance guy?"
    "He mumbles under his breath. You catch a few swear words."
    
    A "So, it's broken?"
    show micah confused
    Mm "No, I think... there's just another problem with connectivity..."
    
    "He answers absentmindedly, still focused on rearranging cables."
    "You glance at his face, looking for any indication as to whether it's a quick fix or not, and can't help but notice that he looks incredibly young."
    Mm "Aha!"
    Mm "Knew this was the problem! So, we can do this..."
    show micah smiling with vpunch
    Mm "Aaaand fixed."
    
    show micah neutral
    "He stands up, and the crane moves back on its own to its starting position."
    
    MC "Wow, cool, thanks!"
    
    "The maintenance man's business-like frown splits into a sunny smile."
    
    Mm "No problem! Just happy to help!"
    Mm "Oh, and, by the way..."
    Mm "'Vampire Conquest III' is working again."
    
    "Andy squeals and skips off immediately. Figures."
    "...Had he heard us talking about that? Where was he?"
    show micah smiling 
    Mm "That enthusiasm... is the best thanks I can get."
    
    MC "So you fix all the machines here?"
    
    Mm "Yeah, these arcades, and some more!"
    show micah neutral 
    Mm "Tinkering with machine's in my blood, y'know?"
    
    "Noticing Andy trying to beat their personal high score on the pinball machine, you see your chance."
    
    MC "Hey, uh..."
    show micah smiling
    M "The name's Micah."
    MC "[MC_name]. So, Micah, you like tinkering, yeah?"
    MC "Can you help me with winning this crane game?"
    
    show micah confused
    "Micah laughs and raises an eyebrow."
   
    M "So you want to play unfair, hm?"
    MC "If it means I'm gonna beat Andy at this crane game, sure!"
    show micah smiling
    "Still chuckling, Micah turns to the control panel and works his magic."
    "You pause for a moment, entranced as his fingers move nimbly across the control panel, tweaking small parts here and there. It barely looks like he's changing anything."
    M "Okay, you can try now."
    
    "You put a coin into the machine and try to grab the angry bat again."
    "The crane moves smoothly, and drops the bat into the hole."
    
    M "You did it!!"
    MC "Awesome! Thank you, Micah!"
    
    "Micah smiles and puts a finger to his lips."
    
    M "It's our secret, 'kay?"
    
    "He grabs his bag of tools from under the pinball machine just as Andy puts in their name into the high score list."
    
    M "See you around, [MC_name]."
    hide micah smiling with dissolve 
    
    "A grinning Andy comes over as Micah leaves and craws about their new highscore."
    "You show them the angry bat you have won. fairly."
    $ micahintro = True
    if larkintro == True and aurelintro == True: 
        jump CRending
    else: 
        jump introchoice

###########################################################
###########################################################

###########################################################
###########################################################

##merge to main route
# if have a love interest you haven’t spoken to yet, loop back to the original parent choice of (where to go) 
#TODO: how???
# ^^^ tief here I will fix dis >:3c 

label CRending: 
    scene carnival
    A "Well that was… interesting, where to next?"
    scene HOM  
    # if you have spoken to all love interests move to the hall of mirrors scene.
    A "Hey do you want to check out the hall of mirrors?"
    MC "Yeah, let's go."


    "It only seems fair since you've been the one making all the decisions up until now."


    A "Awesome! I think it's this way."


    "Andy points in the direction he has in mind and the two of you start walking over. You're about seventy-five percent sure it's the right way."


    A "They used to freak me out so much as a kid! The mirrors."

    MC "They're just warped to make you look like a string bean. What's scary about that?"

    A "I was a kid, [MC_name]. I used to be scared of my own shadow."

    MC "And reflection apparently…"


    "Turning your head away, you fail to stifle a laugh. Andy teasingly bumps their shoulder into yours."


    A "Should we take a second ride on the Ferris wheel then?"


    "You shudder at that thought, remembering the way your stomach dropped at the top of the wheel."


    MC "No."


    "The flat tone in your voice sends Andy's eyes rolling. They playfully slap their hand across their chest like they're about to make a solemn vow."


    A "Don't worry. I won't do that to you, ever."


    "A few minutes later, you and Andy stumble on the large, sun faded sign. The hall of mirrors."


    A "Come on!"


    "Andy motions for you to join them and steps into the dark doorway first. You follow, and pass through several layers of worn fabric draped over the entrance to block out the outside world."

    "On the other side, you enter a dimly lit hallway with mirrors lining each wall. Andy's distorted reflection stares back at you in every mirror. It's eerie."

    "The little hairs on the back of your neck and on your forearms stand straight up. There's something in the air that you can't quite pinpoint a name for."

    "Is it electric? A warning? ...An omen?"


    A "OooOoOoOooh! Spooky right?"


    "Andy's voice slices through your worry, and suddenly, things don't strike you as dire anymore. You take a steady breath. It's just anxiety."

    "Shaking your head, you try to dispel any lingering fears. Mirrors can't do anything. They can't hurt you."


    A "[MC_name]?"

    MC "Your reflection is terrifying."

    A "Hey!"


    "Chuckling, you dash past Andy to the end of the hall and turn into the next room. The space opens up and streaks of blue and green light illuminate the various paths laid out."


    A "Wow."

    MC "You can say that again."


    "Each new area the lights grow more colorful, adding in reds, purples, oranges, and yellows. The mirrors become increasingly more warped, and the reflections absurd."

    "Finally, you and Andy reach a point where the only way forward is through a round doorway illuminated by glow in the dark paint. The swirls and stars lead you in a downward slope as the hallway narrows."

    "The next room is so bright your eyes need time to adjust. And when you look, for a split second, you believe you're outside, but it's a trick. The ceiling is even painted to resemble the sky."


    A "I think it's a maze."


    "Andy walks along the wall of mirrors with their palm pressed against the glass. When they hit the open air, they stop."


    A "Stay close."


    "Nodding, you walk beside them for a minute, and then, behind them when the path narrows. Each step is carefully taken with your fingertips touching the mirrors on either side."

    "You've seen so much of your own reflection today that it almost doesn't look right anymore."

    "Glancing up, you notice there are fluffy, white clouds adorning the painted sky. It's beautiful, and further in the room you think there's a sun there too."

    #TODO: Hpunch potential below

    "And then, you walk into a mirror. The sudden impact sends a shock of pain rippling through your nose and to the back of your skull. Your eyes water instantly, and you bury your face in your hands."


    MC "Ow! Ugh... That was so stupid. Did you see that?"


    "Oddly, Andy doesn't answer. Not even to tease you. You lift your head."


    MC "Andy?"


    "There's a path on either side and you check both turns, but there's only your own reflection waiting."


    MC "{i}Hey!{/i} Come back!"


    "You hear nothing. Not even footsteps."

    menu:
        "Go right":
            "The path quickly leads to another dead end. No matter where you go, it's glass."
            "Your heart races, and you spin on your heel. Nothing looks familiar. Everything's the same. Have you actually gone anywhere?"

            "It's like you're back at the start, but you're not. You can't be."
        "Go left":
            "The maze goes on for a while. Some directions lead to dead ends, but most give you a sense of progression. The end must be here somewhere..."
            "{i}Another dead end{/i}. You search for an opening, but find none. This time it sends your heart racing."

            "You find a path further down and stop dead in your tracks. The sight is reminiscent of the start. That doesn't make any sense. There's no way you circled back..."



    #Converge
    "You look up and recognize that you're almost under the long, wavy rays of the sun. It's a crumb of hope, but at least it's something."

    "You move forward, and the mirrors appear closer. Is the path narrowing again?"

    "Dead end."

    "Dead end."

    "Another dead end."

    "Panic sets in this time as you pick up speed and run. It's all glass in every direction you go. And your hands, nose, and shoulders ache from bumping into wall after wall."


    MC "{i}Andy{/i}! This isn't funny."


    "The only thing you hear next is the blood pounding in your ears."

    "Finally, the maze appears to open up ahead, but that doesn't make sense. It can't be the exit. You're directly under the sun."

    "Something different moves in your peripheral vision. A flash of gold."

    "{i}Eyes?{/i}"

    "Your body freezes mid step. It's only you in the mirror. That can't be right. You touch the glass."

    "You remember blond hair and gold eyes. A shiver races down your spine."


    MC "Hello?"


    "Still, there's no answer. You reach the opening and your heart sinks. This has to be the center of the maze."

    "There's several paths and it's not long before you're confused. Which way?"

    "You hear a footstep."


    MC "Andy?"


    "There's another, and then it's just your heart."

    "You need out. Now."

    "You pick a direction at random and your feet bring you to a three way split in the maze. It's strange. There's noise coming from each one."


    "To the left you swear there's a faint call of an elephant. It reminds you of the main tent and the dashing, charismatic ring leader you met there... Aurel."

    "The center beckons with the familiar music chimes and metal gears of arcade cabinets and pinball machines. You remember Micah's sunny smile."

    "To the right you hear the faint jingle of bells and the clatter of several things hitting the floor and rolling away. Those small, red balls come to mind and... the mischievous curve of Lark's mouth."


    "Are you losing your mind? This doesn't make any sense. Your head turns and you notice there's something behind you."

    "The lights go out."

    "And something sharp curls around your throat. You scream."


    #TODO: add choice in correct place   

    menu:
        "Micah":
            jump micah

        "Aurel":
            jump aurel

        "Lark":
            jump lark


label game_end:
    return
