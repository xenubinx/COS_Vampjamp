label micah:
###MICAHS ROUTE STARTOOOOOOO
    scene carnival
    "Your piercing scream echoes in your ears, in the maze."
    "Your footsteps are frantic, a staccato on the ground."
    
    M "[MC]?!"
    M "Watch out!"
    
    "A worried voice cuts through your panic."
    "Before you can open your eyes, a strong hand grabs your shoulder, stopping you."
    "Opening your eyes, you find yourself looking directly into Micah's worried blue ones."

    show micah confused
    
    M "Woah there, slow down!"
    M "Where are you going, little one?"
    
    MC "Where I am... going?"
    
    "Taking in your surroundings, you realize that you are already outside."
    "Wait. Outside?"
    "The big tent is not far away, the cool night air on your face. A shudder rolls down your back."
    
    MC "Wh-what?"
    
    "You were just in the mirror maze, with those creepy eyes watching you, so how--"
    
    M "You're shaking."
    
    "His hand is still on your shoulder, and its warmth may be the only thing grounding you right now."
    "Your pulse is still racing, the adrenaline high; nothing makes sense at this moment."
    
    MC "Sorry, I really don't know what just happened..."
    MC "I was in the mirror maze, and there was no way out, and..."
    
    "Micah retracts his hand, and you kind of wish he didn't."

    show micah neutral
    
    M "But the Maze of Mirrors is down there, behind the main tent."
    M "That's not where you came from."

    show micah smiling

    M "Although, you {i}did{/i} come running through and then just stand here next to the hot dog stand and start to scream like your life depended on it... No judgement."

menu:

    "Ha {i}fucking{/i} ha.":
        M "I mean, I get like this sometimes too, y'know?"
    
        jump oddball

    "Forget about it.":
        show micah neutral

        M "You think? Okay, I trust you."
        
        jump oddball




    
label oddball:

    "You sigh. Now Micah thinks you're an oddball. Could be worse, though."
    "But you have a feeling that there's something more to it."
    "How could you have made it halfway across the carnival?"
    "Were you running {i}that{/i} fast?"
    "... Without seeing where you were going?"

    show micah sad
    
    M "[MC], you're really pale."

    show micah smiling

    M "C'mon. We'll warm you up."
    


    scene dressing room
    "Still deep in thought, you trail behind Micah through the carnival streets."
    "Both of you arrive at a side entrance to the main tent."
    "Micah ushers you in, and you enter a kind of dressing room."

    show micah neutral
    
    M "Come on in and take a seat. Anywhere, really."
    M "Sorry it's so messy, but you know how it is with busy working people..."
    
    "You look around for a seat and find a sofa with lots of costumes and clothing on it. Pushing some stuff aside, you sit down."
    "Now you realize how much you've been shaking; your legs are happy to rest."
    "With all these personal things squeezed into every corner, it seems like you're intruding into their private lives."
    
    MC "Is this... where you live?"
    
    M "Oh, no, it's where Isadora, Lark and Aurel change their costumes for the shows."
    M"I help out sometimes, as an extra. I think I have a costume... somewhere..."
    M "But it's warm here. You need to rest a bit."
    M "Let me find you something to drink."

    "Filing through different items from a locker with his name on it, Micah takes out several red bottles, but puts them back quickly."
    "Maybe they were already empty?"
    "He looks around the makeup table as the door opens and Aurel steps in."
    "Raising an eyebrow, he looks at you."

    show aurel neutral at left
    
    Au "What's this?"
    Au "Micah, how come [MC_name] is still here at this hour? The carnival's closed."

    show micah confused at right
    
    M "Well--"
    
    MC "'At this hour'? How late is it?"
    MC "Wait, where is Andy?!"
    
    "Anxiety flares in your gut and you rush out of the room."
    hide aurel neutral with dissolve
    hide micah confused with dissolve

    
###OUTSIDE
    scene carnival
   
    "Oh no, oh no, oh no!"
    "Frantically looking around, you can't see Andy anywhere."
    "You reach the main gate."
    "Actually, you don't see anyone, anywhere."
    "Not a single soul in sight."
    
    MC "Right... Aurel said the carnival's closed."
    
    "The looming gate in front of you is closed, too."
    
    MC "I... shouldn't be here anymore."
    
    M "[MC_name]!" ##no sprite
    
    "Stepping towards the gate to see if you can open it, you stop."
    "{b}Involuntarily.{/b}"
    "Your feet are rooted to the ground by an invisible force."
    
    MC "What?"
    
    "You take a step back."
    "Your feet are working."
    "You step forward."
    "And can't take another step further."

    show micah neutral with dissolve
    
    M "...Ah."

    "Micah watches your desperate attempt to go past the invisible barrier and nods."
    show micah sad

    M "So you're bound now too, huh?"
    
    "His tone is worried, and his eyes search for something. Or someone."
    
    M "I don't know what happened, but..."
    M"You're gonna stay here, little one. With us."
    
    MC "What?!"
    MC "Are you for real? Is this for real?"

    show micah shocked

    M "Relax, Isadora will explain it to you--"


    MC "I can't stay here, Micah, I have to go home!"
    
    "Panic claws at your throat, and this is just too much to process--"
    hide micah shocked with dissolve
    
    I "At ease." ##no sprite
    
    "You whip around to the newcomer."

    show isa smiling
    
    I "No need to panic, now."
    
    "She smiles at you, and her soothing voice is somehow calming you down way more than expected. It feels like a cold blanket settling on your panic, smothering  it."

    I "Good. Deep breaths."
    I "In, and out."
    I "Good, very good. One more time."

    show isa smirk at left
    
    "Her eyes are staring at you intently, like a teacher waiting for you to do as you are told. Unblinking."
    "You take a few more deep breaths. It's getting colder."

    show micah neutral at right
    
    M "Isadora."
    
    "Her gaze doesn't waver. She's still focused on you, tilting her head, not giving Micah any kind of attention."
    "Micah doesn't say anything until she deliberately turns around to face him. The icy feeling lets up and leaves goosebumps in its wake."

    show isa neutral at left
    
    I "Yes?"
    
    M "They're stuck here."
    M "Just like us."

    show isa sad at left
    
    I "...Is that so?"
    I "Poor thing."
    
    "Your pulse is steadying, and you step back from the invisible glue trap."
    
    MC "Like you?"
    
    I "Sadly, yes."
    I "When all the lights and glamor fade, we're still stuck at this carnival."
    I "It's not just our home in a familial sense."
    I "We are not able to leave."
    
    "This should be way more alarming in a rational sense than it feels right now."
    "You're still oddly calm. Micah, too."

    show isa neutral at left
    
    I "I will consult with Aurel about this matter."
    
    "She steps up to Micah, gently cupping his face."

    show isa smiling
    
    I "You will take care of them, all right?"

    show micah empty at right
    
    M "...Sure."

    show isa smirk
    
    I "Good! I'll call for you when you're needed."

    hide isa smirk with dissolve
    hide micah empty with dissolve
    
    "Without a word, she leaves with unhurried steps."
    "What was that about? {i}You're stuck here, too{/i}?"
    "But what about your family? What about Andy, your friends?"
    "An unsettling feeling blooms in your chest."

    MC "Micah...?"

    show micah empty

    "You turn towards your only apparent ally in this mess - but he's staring into the distance, eerily still. It's an odd look on him-- every time you've seen him so far, he's been thrumming with energy."

    MC "Hey, are you all right?"
    
    M "....."
    M "...Hm?"
    M "I'm fine. Yeah."
    
    "He frowns, his eyes still distant. It seems like he has a headache, like he's trying to get himself together."
    "Shaking his head like a big dog, he snaps out of his reverie."

    show micah confused
    
    M "Brr! Man, it's cold."
    M "[MC_name], let's go over there. The Arcade is warmer, and has food."
    
###ARCADE
    
    "You let him guide you along to the Arcade, where you and Andy first met Micah."
    "The stupid bet with Andy, Micah's secret smile when he rigged the claw machine... Everything seems so far away now. Like a distant memory, although it's barely nighttime."

    show micah neutral
    
    M "How did you get lost in the first place?"
    
    "Micah hops over the counter where, when you'd seen it that day, an employee had been redeeming hard-earned tickets from the machines."
    "He skips all the prizes and goes right for the popcorn machine."
    
    MC "I... can't really remember."
    MC "Andy and I wanted to try the mirror maze, and... Suddenly, there was no exit anywhere."

    show micah smiling
    
    M "So... you got lost." #teasing
    M "Good thing that I found you, then, hm?"
    M "I know this place like the back of my hand. Seen every nook and cranny."
    M "Probably fixed all of the nooks, too."

    show micah neutral
    
    "He fills up a small bag with popcorn and hands it to you before getting himself something to drink from a small fridge."
    "It's a red bottle and looks like one of those syrup-y drinks you're not too keen about. Way too much artificial flavor."
    "He doesn't offer you a bottle. Micah pops the lid and sits on the counter."
    
menu:
    "Thank you, my magnanimous hero.":
        jump hero
    
    "Thanks, Micah.":
        jump thanks_mic
    
label hero:

    "You even bow to show your gratitude in jest."

    show micah smiling
    
    M "Hahaha!"
    M "You may rise."
    
    jump popcorn

label thanks_mic:

    "You hope to express your gratitude with a genuine smile."

    show micah smiling
    
    M "No problem, really!"
    
    jump popcorn
    
label popcorn:

    "The buttery popcorn crunching between your teeth melts your anxiety somewhat."
    "It might be the best popcorn you've ever eaten."

    show micah neutral
    
    M "Come, sit with me."
    
    "He pats next to him on the counter. His feet are dangling in the air, dipping restlessly, while he's nursing his drink."
    "You hop on and munch another handful of popcorn."
    "Everything around you is so... silent-- even though the lights of the arcade are still on, and the electronics are running."
    "There's not a soul in sight."
    
    MC "So... I guess I have to be here... forever... then?"
    MC "Seems difficult to believe."

    show micah shocked
    
    M "Forever?"

    show micah neutral

    M "That's a... really long time."
    
    MC "C'mon, you know what I mean."
    MC "How long have you been here? Working or living or whatever."
    
    "Micah tilts his head downwards and seems lost in thought for a moment."

    show micah confused

    
    M "A few years, I guess."
    M "Since my teenage years?"
    
    MC "Oh god. Please don't tell me this carnival is condoning child labor."

    show micah shocked
    
    "Micah is surprised for a second before starting to laugh loudly."

    show micah smiling

    "In the neon light, his smile is radiant, almost sharp--"
    "No, it must've been a trick of the light. Micah couldn't have teeth that sharp. Maybe they're fake. Part of the carnival mystique."

    M "I've been working for a long time here, yes, but I've never seen children working here."

    "He scoots a bit closer, tilting his head."
    "Although he's so close to you, directly in your personal space, you feel no body heat coming from him."
    "The neon light above your flickers and casts a dangerous shadow on Micah's wide grin."
    
    ### CG Micah smiling widely
    
    M "But back in my day, nobody was batting an eye at that."
    M "Wanna take a guess when that was?"
    
menu:
    "I do?":
        jump question

    "I might have a hunch...":
        jump hunch

label question:

    M "Come now, little one."
    M "You probably learned in history class that there was a time when child labor was not frowned upon."

    show micah neutral
    
    "His tone is playfully disappointed, but his mouth is trying to fight an amused smile."
    "Taking a big sip of his drink, he theatrically sighs afterwards, like he's a thirsty man in the desert finally getting relief."

    show micah smiling
    
    M "That's the stuff."
    M "You know, this drink's for employee's only."
    
    "You can see a drop of it on his lower lip. It's familiar."
    "It's not syrup."
    
    jump vampire_guess

label hunch:
    
    M "Oh, really now?"
    
    "Taking a big sip of his drink, he theatrically sighs afterwards like he's a thirsty man in the desert, finally getting relief."
    
    M "That's the stuff."
    M "You know, this drink's for employee's only."
    
    "You can see a drop of it on his lower lip. It's familiar."
    "It's not syrup."
    "His sharp teeth gleam in the neon lights, and no, those are definitely not fake."
    "His eyes are fixed on you. Predatory. Waiting playfully for you to make the next move."
    "Your pulse quickens and your stomach squirms."
    
    jump vampire_guess

label vampire_guess:
    
    "The teeth. The syrup-y drink that is very possibly blood."
    "He knows the carnival like the back of his hand after \'all these years.\'"
    "No body heat."
    "It takes a bit of courage and a whole lot of daredevilry to say the next words out loud."
    
    MC "Are you... a vampire?"

    show micah neutral

    "Silence."
    "Micah doesn't say anything, but his amused smile quivers."
    "Before you can feel silly about saying something like this, he claps his hands."

    show micah smiling
    
    M "Ding, ding, ding!"
    M "The contestant gets 1000 points!"
    
    MC "W-wait a second."    
    MC "Just how old are you?"
    
    "Kicking his feet in the air, Micah just smiles wistfully."

    show micah neutral
    
    M "Around 200 years."
    M "I've been living my whole life here as a vampire. With Isadora and the others."
    
    "That is something you have to process for a moment."
    
    MC "So..."
    MC "Isadora and... Aurel and Lark are vampires, too?"
    
    M "Yup. We're like... a family. Or something."

    show micah confused

    M "...Yeah, more 'something' than family. But then again what do I know about family?"

    show micah neutral

    M "My biological family abandoned me because of who I am, so..."
    M "I came here. And stayed."
    
    "Another sip from his drink. Another popcorn kernel between your teeth."
    "You let  that sink in, your thoughts swirling."
    
menu:

    "That's... a lot to take in.":
        jump blow_mind

    "...Cool.":
        jump i_know

label blow_mind:

    show micah smiling
    
    M "Did I blow your mind?"
    
    MC "Ha ha."
    
    jump snag_popcorn

label i_know:

    show micah smiling

    M "I know, right?"
    
    MC "Not what I meant, but, yeah."
    
    jump snag_popcorn

label snag_popcorn:

    "Without further ado, Micah snags a popcorn from your half-empty bag."

    show micah neutral
    
    M "But I get it."
    M "It also took me quite a while to get used to all of this."
    
    MC "You mean, drinking blood?"
    
    M "And living under Isadora's protection, out-living co-workers and such."
    M "Living at a place that sells happiness and a fun, fleeting time while we are stuck here forever, making the most of it."

    show micah sad

    M "But..."
    
    "He takes a deep breath and seems to be talking to himself."
    
    M "It's the best alternative.."
    
    "A thoughtful silence settles comfortably around you."
    "Stuck here forever, huh? Maybe that's the fate you're sharing now, too."
    "Your stomach grows heavy at the thought of never seeing your friends, your family, ever again."
    "You didn't even say goodbye to them properly. The rushed 'I'll be home late!' you told your mom doesn't count."
    
    MC "So..."
    MC "How do you live here? Pass the time? Besides fixing the arcade machines; that's just your job."
    
    "Dragging himself out of his own reverie, he looks at you."

    show micah confused
    
    M "But my job {i}is{/i} my hobby."
    
    MC "Huh?"
    MC "Really?!"

    show micah neutral
    
    "A sheepish look crosses over his face."
    
    M "...I've always liked to work on machines. Fix them, improve them."
    M "I don't have  formal training, but it's... fun. Relaxing, even."
    
    MC "You are a rare breed of 'making-their-hobby-their-livelyhood'. I tip my hat."
    
    "You tip your imaginary hat and smile."

    show micah smiling
    
    M "Thank you, my liege."
    
    "He bows his head and plays along."

    show micah neutral
    
    M "Don't you have a hobby? Something that really drives you?"
    
    MC "Not... really."
    MC "Don't misunderstand! I really enjoy many things, but probably not as... focused and intensely as you do."
    MC "So, yeah, I might be a bit envious, haha!"
    
    M "Don't be-- it can also be very frustrating at times."
    M "I have this... project. Quite literally a 'pet project'."
    
menu:

    "Ooh, tell me more!":
        $ micah_goodend += 1
        jump lightup

    "Hm, okay?":
        jump scratch_cheek

label lightup:

    "Micah's eyes start to light up."

    show micah smiling
    
    M "Be warned, I won't stop if you're willing to listen!"
    
    jump tell_me
    
label scratch_cheek:

    "Micah scratches his cheek."

    show micah sad
    
    M "It may seem... childish."
    
    jump tell_me
    
label tell_me:

    MC "C'mon, just tell me about it!"

    show micah neutral
    
    M "Okay, okay."
    M "I'm working on an autonomous pet. A dog, to be precise."
    
    "His hands are moving, almost talking along."

    show micah smiling
    
    M "It's been a work in progress for many years by now..."
    M  "Faraday's prototype is built with spare parts and scrap, but she's beautiful."
    M "The tricky part is to make her move on her own."
    M "I got my hands on portable batteries, but..."
    
    MC "Don't you have a computer?"

    show micah confused
    
    M "A... what now?"
    
    MC "Computer. Maybe a small one you can build into your dog?"
    
    M "I have no idea what you are talking about."
    
    "Stunned, you remember that Micah's a very old vampire, who probably hasn't interacted with the outside world since the dark ages or so."
    
    MC "Oh, okay, so... A computer is an electronic device with a screen."

    show micah shocked
    
    M "You mean a TV? I know those."
    
    MC "It looks like one, but you can put data on it! Program it to work just the way you want it to!"
    MC "Like a.. smart TV that can do math or whatever you want it to do."

    "It's hard explaining it, since you aren't a specialist yourself, and never looked too deeply into it. It never interested you to build your own computer or learn programming."

    show micah neutral
    
    M "....."

    show micah shocked

    M "That sounds... too fantastic to be true."
    
    MC "I know, right?"
    MC "I'll show you one, next time we--"

    "\'Next time,\' hah. You realize there might not be a next time."
    "Because you're still stuck."

    show micah neutral

    MC "If we..."
    MC "... can leave this place."
    
    "If you can leave this place. Big if."

    show micah sad
    
    M "Thanks for the offer, but..."
    M "I don't wanna go outside."
    
    MC "...What? Why?"
    
    M "....."
    
    "Micah fiddles with one of his necklaces, deep in thought."

menu:
    "Are you okay?":
        jump deep_breath

    "(Wait for Micah to speak.)":
        $ micah_goodend += 1
        jump this_is_home

label deep_breath:

    "Micah takes a deep breath, and it seems like he's struggling to tell you something."
    
    M "...Yeah. I guess."
    M "It's just..."
    
    jump this_is_home

label this_is_home:

    "He licks his teeth, and you realize he's anxious about something."

    show micah confused

    M "This is my home now."
    M "And after so many years... living with the others, living the carnival life..."
    M "I don't know if I can face the outside world."

    show micah sad
    
    "He turns to you, his eyes unsure."

    show micah confused
    
    M "Does that make sense?"
    M "It feels like... I won't belong with your kind."
    
    MC "My kind? You mean humans?"
    
    M "Yeah, humans who have built a modern, fast-paced world."
    M "I hear about it from suppliers and co-workers who come and go."

    "A fast-paced world... Huh. As someone who was born into it, and picked up the internet and everything else with a toddler's unstoppable curiosity, you never thought about it that way."
    
    MC "Well, that's one way to describe it. You're not wrong."
    MC "This world has evolved rapidly in the technological department..."
    MC "I'm no expert, but I think I know where you're coming from."
    MC "If you don't keep up, you'll be lost, like some old people who can't handle any electronic devices."
    MC "But it has its upsides, too!"
    MC "I think there's a way to fulfill your dream of building Faraday to be walking and acting on her own."

    "Your little speech apparently strikes a chord in Micah."

    show micah shocked
    
    M "...You think?"
    M "That would be... amazing."
    
    MC "Why \'Faraday,\' anyway?"

    show micah smiling
    
    "A big, happy smile stretches across Micah's face. It irons out the thinking lines between his brows."
    
    M "Faraday invented the first electric motor with electromagnetic fields!"
    M "Not the kind we know today, but he worked it out with research by Orsted and Ampère and--"
    M "He was a self-taught scientist, just like me!"
    M "Faraday had this idea that electricity might not be a material, fluid like water that goes through a pipe or something."
    M "He thought it might be a force or vibration--"

    show micah shocked

    M "Oh, sorry, I know this must be boring to you."
    
    "Catching himself mid-rant, Micah's shoulders sag."
    
menu:

    "No, no! Talk nerdy to me, please!":
        jump too_highly

    "Haha, you're a geek!":
        jump massive

label too_highly:

    show micah smiling

    M "Oh, so that's what you're into, huh?"
    M "I'm not smart like Aurel, though, and I'm hardly a scholar."
    M "All I do is fix some machines and light bulbs around here."
    
    jump casually
    
label massive:

    show micah smiling

    M "Haha, yeah, a massive one! Maybe I should get some thick glasses."
    M "But really, all I do is fix some machines and light bulbs around here."
    
    jump casually
    
label casually:

    show micah neutral
    
    MC "And you CASUALLY build a robot dog!"
    MC "Who knows what else you can build - the sky's the limit!"
    MC "Maybe you want to CASUALLY build a self-driving car? We don't have those yet!"

    show micah smiling
    
    "Your joined laughter echoes through the arcade."
    "Your pinky touches Micah's gloved hand by accident and you can feel him shaking from laughter."
    "Putting your hand into the popcorn bag, you notice it's empty."
    "Before you can mourn the last piece of perfect popcorn, a hurried movement catches your attention."

    show micah shocked
    
    MC "Is that... a bat?"
    
    "A small creature the size of your hand darts directly for Micah."
    
    M "Oh, it's a summoner."
    M "I gotta go."
    
    "He jumps from the counter in a swift motion but before following the little bat, he stops and turns to you."
    
    show micah neutral
    M "You wanna come with?"
    M "It's either a fixing job, or Isadora has some update on your situation."
    M "Wish those little guys could talk. Or are they girls? Bats are not my specialty."
    
    hide micah neutral with dissolve
    "He nods at you to come along, and sure, why not?"
    "It's not like you got something better to do. Or somewhere to be."
    "Maybe you will gain more insight into your situation, being stuck here."
    "A flicker of hope rises in your chest as you run after Micah."    
    
###OUTSIDE
    scene carnival
    "The carnival is still silent and still. Frozen in time."
    "Will you be frozen in time as well?"
    "Though... time will move on for you, since you're human..."
    
    MC "Micah?"
    
    "As you walk side by side, guided through the paths of the carnival by the summoner bat, Micah turns to you."
    show micah confused with dissolve
    M "Hm?"
    
    "Looking at you, an eyebrow raised, Micah really looks... normal."
    "Not like a vampire at all. With his outfit and undercut, he'd look like any other human out there."
    "But he's way older than he looks. He really seems frozen in time."
    
    MC "I was thinking..."
    MC "If I'm really going to be stuck here..."
    MC "Will I become a vampire?"
    
    M "'Become'?"
    M "Oh, you mean, being bitten?"
    
    MC "Otherwise, I'll die way before you guys."
    MC "A human life expectancy is around 80 years old, so, in vampire time, it's probably something akin to a month."
    MC "Maybe I'll die next month!"
    
    "Micah thinks for a second about what you just said and laughs quietly."
    show micah neutral 
    M "For some vampires, 80 years might seem like a month or so, I guess."
    M "Can't say so for myself, though."
    M "But... as far as you being turned into a vampire in the future..."
    
    "He seems to contemplate the thought as he takes a turn. The main tent is coming into view."
    "Maybe Isadora really summoned you?"
    
    M "Well..."
    
    "He parts the flap of the tent entrance to the side, stepping aside to leave an opening for you."
    "The warm light is spilling out into the dark and onto your feet, inviting you in."
    show micah smiling
    M "We'll find out." #grinning
    hide micah smiling with dissolve
    
###CIRCUS TENT INSIDE
    scene circus
    "You step inside the warm tent and are blinded by the lights."
    "Adjusting, you realize you came through a side entrance this time; earlier-- which feels like forever ago-- you came through the main entrance."
    "Isadora and Lark  swing on a trapeze, concentration lining their faces."
    "They flip easily back and forth, and then back again. Isadora leaps, and catches Lark's  outstretched hand in the last possible second."
    "They move with the momentum until Isadora is thrusted up, twirls, and catches her own bar again, swinging effortlessly."
    "Aurel is standing below, reading something in the first row."
    "Micah announces himself with a big wave and a cheer."
    
    show micah smiling at left
    with dissolve 
    
    M "I'm here!"
    M "Whatcha need fixing?"
    
    "Aurel carefully puts a bookmark into the pages he's currently in, and turns towards you."
    show aurel neutral at right
    Au "Oh, it's you."
    Au "Thanks for coming over so quickly, Micah."
    Au "And hello [MC_name] as well. I heard of your... situation."
    
    "Gentlemanly as ever, Aurel's perfect posture is highlighted standing next to Micah, whose pose is relaxed, but ready to spring into action."
    
    M "Yeah, we wanted to ask about that."
    M "But, before that: is something broken?"
    
    Au "Yes. The spotlight over there flickered out about half an hour ago."
    Au "It’s driving me mad…"
    
    M "Hm, maybe it's just the bulb."
    M "I'll take a look at it."
    
    hide micah smiling with dissolve
    "Conjuring a screwdriver from god-knows-where, Micah skips off, leaving you with Aurel, who has an indiscernible look."
    show aurel neutral at center
    with move 

    MC "So..."
    MC "You heard from Isadora? About me being stuck here?"
    
    Au "Yes, she mentioned it."
    Au "It's curious - you, in particular, have nothing to do with Festum Astrosum, nor with any of us."
    Au "...As far as I know, at the least."

    MC "That doesn't sound really reassuring..."
    MC "I mean, all I did was have a good time and then get lost in the mirror maze."
    MC "Maybe... It has something to do with those eyes I saw?"

    "That seems to garner his full attention."
    show aurel shocked
    Au "Eyes, you say?"

    "You try to remember what happened when you realized you were stuck in the maze, but all you remember is the rising panic and those piercing eyes that made you scream."

    MC "They were... gazing into my soul."
    MC "I dunno, they just seemed to... {i}devour{/i} me."
    MC "But only for a split second? Sorry, that doesn't make any sense..."
    show aurel neutral 
    "Aurel seems to ponder this, watching Micah in the distance."

    Au "And you say Micah got you out of there? Were they his eyes you saw?"

    "He doesn’t even seem to be all that convinced by what he’s saying."

    MC "I'm not sure. I'm also not sure how I got out, because I was running, and then Micah stopped me."
    MC "I was half across the carnival by then."

    Au "Hm..."
    Au "That is {i}certainly{/i} odd. I'll talk to Isadora about this as soon as possible."
    show aurel neutral at left
    with move
    "Just in time, Micah comes back, a satisfied smile on his face."
    show micah smiling at right
    with dissolve

    
    M "It was just the bulb, no biggie."
    M "Good thing we have a good stockpile of those."
    M "Sooooooo, [MC_name]..."
    
    "His leering face is exaggerated by his wagging eyebrows."
    
    M "Did you ask Aurel about being turned into a vampire?"
    M "Since he turned me, maybe you have a shot, too!"
    
    "You know he's ribbing, but--"
    
menu:

    "Please make me into a vampire!!":
        jump please_vampire

    "No, I didn't mean it like that!":
        jump not_like_that

label please_vampire:
    show aurel shocked

    Au "Excuse me?!"

    "\'Aghast\' is a light word for the look on Aurel's face."

    Au "This isn’t something to be joked about."

    "Despite Aurel's apparent horror, you can’t help but juggle the idea around in your mind."

    MC "Oh, you know, the whole vampirism thing is pretty big in the media right now, and it seems..."
    MC "Hot, I guess?"

    "Micah cackles in the background while Aurel flounders for words."
    
    jump lets_drop

label not_like_that:
    
    M "Oh, come on, don't be shy!"
    show aurel angry
    Au "Micah, please. Being turned into a vampire isn't something to be taken lightly."
    Au "It's not something you can undo. It's your life."

    M "Yeah, yeah."
    
    jump lets_drop

label lets_drop:
    show aurel neutral
    M "Okay, okay, maybe we should drop this for now."
    M "Look, Isadora and Lark are done with their routine training."

    "Still flustered from the conversation, you look over to Isadora and Lark approaching."
    show aurel neutral at fourd
    with move
    show micah smiling at fourd
    with move
    show lark neutral at fourb
    show isa smiling at foura
    "They are walking close to each other, with Isadora having Lark's hand in a tight vice grip, pulling him after her."
    "Lark's gaze is passive, not meeting yours, and is just trailing after her as if he has no choice. Poor Lark."
    "When Isadora notices you, her face brightens up. Why is she so happy to see you?"
    "She lets go of Lark's hand and skips over."
    
    I "Oh, hello, [MC_name]!"
    I "Did you accustom yourself to your new surroundings?"
    
    "She cards a hand through one of her voluminous ponytails."
    
    MC "Ah, yes, Micah's shown me around and explained to me what's going on."
    
    I "Is that so?"
    
    "Switching her focus over to Micah, she eyes him like a hawk, her smile gone. She's really good at switching moods; it's spooky."
    "He's not phased by her, but doesn't speak up."
    "In fact, all three of them become as motionless as possible. As if they're afraid of triggering a bomb."
    
    I "How much did he tell you?"
    
    "Her smile is directed at you again."
    
menu:

    "Well, I know that you're all vampires?":
        jump hums_thought
    
    "Oh, this and that...":
        jump what_exactly

label what_exactly:
    show isa neutral
    I "And what exactly does \'this and that\' entail?"
    
    MC "Well..."
    show isa smirk
    "She doesn't take your humming and hawing well. Her smile gains an edge."    
    I "Let me guess. You already know what we are."
    
    "You feel like you ratted Micah out. Like you told her something that you shouldn't have."
    
    jump hums_thought
    
label hums_thought:
    show isa neutral
    "She hums in thought and nods."
    
    I "It's not something we broadcast, but..."
    I "It's a shared fate, I'd say."
    show isa sad
    I "Are you afraid, [MC_name]? Of us?"
    
    "Looking over to your left, where Aurel is looking deep in thought, and Micah next to him smiling, and Lark next to Isadora glaring at you..."
    "You can't help but feel that these different personalities are being held together by something deeper, something you cannot grasp yet."
    "They certainly seem familiar with each other, but not loving."
    "Micah said that they are 'something'. Not family."
    
    MC "No, I don't think so."
    MC "I'm feeling... sad. For you all being trapped here for such a long time."
    
    "It certainly causes a stunned reaction-- until Isadora laughs."
    show isa smiling
    I "How sweet!"
    I "You're pretty empathetic, aren't you?"
    I "That's very nice of you to say."

    "Her warm smile makes you smile in return."
    
    I "Considering you are also trapped here now, I do hope you don't lose that shiny optimism just yet."
    I "That's what I summoned Aurel for-- but we haven't had the chance to look into that matter."
    
    Au "Isadora, do you think this has anything to do with the pact?"
    
    I "Hm... it's possible, but it could also be unrelated."
    I "Maybe their problem is only temporary?"
    
    MC "About that..."
    
    I "Hm?"
    
    MC "If I really have to stay here forever..."
    MC "{i}Will{/i} you make me into a vampire?"
    
    show lark angry 
    #TODO: potential vpunch?
    "Before Isadora can answer, Lark steps up, his gaze stormy."
    
    L "No."
    L "Don't even think about that."
    
    "His tone leaves no room for argument, but Micah doesn't seem to catch it or simply ignores it when he stands in front of you protectively."
    show micah shocked 
    M "Why not?"
    M "If they want to become a vampire, that's their choice!"
    
    L "You {i}know{i} what it means to be a vampire, Micah. The burden that comes with it."
    
    show micah angry 
    M "Is it a {i}burden{/i} for you, Lark?"
    
    L "It's a sacrifice! You know how much we've suffered--"
    
    M "Speak for yourself! You think being a vampire is only suffering?"
    M "Because I definitely don't think so!"
    M "You know how this is the only way I can {i}truly{/i} be myself!"
    M "And I never regretted a {i}single{/i} moment being who I am!!"
    
    L "Your experience is not universal, Micah, stop being so self-centered--"
    
    M "Self-centered? That's rich, coming from you, Mister Brooding-over-Everything--"
    show isa angry
    I "Stop it, you two."
    show isa angry with vpunch
    I "NOW."
    show micah shocked
    show lark shocked
    "Her tone cuts the tension like a knife through butter."
    "Both squabblers back off immediately, taking a step back."
    show micah neutral 
    show lark neutral
    
    I "Lark, you know that I do not condone this type of behavior."
    I "And Micah, I understand that this topic is important to you, but [MC_name] can still decide for themself."
    
    "Micah mumbles to himself, pouting like a scolded child. It's kinda cute."
    
    M "Sorry..."
    
    "Like a switch, her stern face slips into an amused one - she claps her hands and you try to keep up with the mood swing."
    show isa smiling 
    I "Good!"
    I "Now. Micah, you fixed the spotlight, I see?"
    
    M "Yes, I did."
    
    I "Very good!"
    I "Well done, Micah."
    
    "She cradles his cheek in her palm, stroking her thumb over his skin softly. It's so intimate and off-putting, you feel the need to look away."
    
    I "You're always so reliable and efficient... What would I do without you?"
    
    "When you look over to Micah again, Isadora has taken her place at Lark's side again."
    show micah empty
    "Micah's gaze is distant."
    
    I "Now, then!"
    I "It's getting late, and we're rapidly approaching dinner time."
    I "I have to freshen up first."
    I "[MC_name], have you already eaten? There's plenty of food at the food court-- maybe Micah can serve you something more nutritious than popcorn."
    
    MC "Oh, uhh, that'd be nice. Thanks!"
    
    I "All right. Micah, please accompany them to the food court."
    
    "Micah nods absent-mindedly and is ushering you toward the exit when Isadora calls out to him again."
    
    I "Oh, and, Micah?"
    
    "You both turn around and you see that intense gaze directed at you again. Goosebumps prickle down your spine."
    
    I "Dinner will be in..."
    I "One hour. Be punctual."
    
    M "...Yes."
    
    "His response is flat, devoid of any emotion. Micah doesn't look too good." 
    "This happened earlier, too, didn't it?"
    "You see Isadora and Lark leave with Aurel in the opposite direction."
    "Something seems... wrong."
    "You turn to catch up to Micah, who doesn't seem to notice you, as you two leave the main tent and step back into the night."
    "Wait a second. How did she know about the popcorn?"
    hide micah empty with dissolve
    hide isa happy with dissolve
    hide lark neutral with dissolve
    hide aurel neutral with dissolve
    scene black with dissolve
###FOOD COURT
    scene foodcourt with dissolve
    "This night certainly is getting weirder and weirder."
    "Sure, it's nice that Isadora and Aurel are looking into the reason why you might be stuck here, but..."
    "Something about them is rubbing you the wrong way."
    "Especially..."

menu:

    "Isadora":
        "Isadora really is a moody one."
        "The way her mood changes within the bat of an eye, it almost seems like she's... acting."
        "And she's intense, too."
        "You don't really know how to handle her. And when she interacts with Micah..."
        
    "Aurel":
        "Aurel seems interested in you and invested in your predicament. And yet, he seems passive."
        "Like he is waiting for permission or a sign or something."
        "Regarding Micah, he's the friendly type, but when Micah gets like this..."
    
    "Lark":
        "Lark is a closed off person, and you respect that."
        "But his outburst earlier raises some questions."
        "Why was he so agitated about Micah? Is it just a difference in perspective and opinion?"


show micah empty with dissolve
"Looking over to Micah, who is robotically making you something to eat just by muscle memory, your heart drops."
"Seeing him so devoid of his usual energy, of his cheery personality, doesn't seem right."
"There must be some way to cheer him up."

MC "Hey, Micah."

"He doesn't seem to notice that you've said anything to him, and continues picking ingredients from the cart."

menu:

    "Go over and touch his arm.":
        $ micah_goodend -= 1
        "He doesn't realize you're next to him until you touch his forearm lightly."
        show micah empty with vpunch
        "Suddenly, Micah flinches like he's being electrocuted and jerks away from you."
        
        MC "O-oh, sorry, I didn't mean to--"
        
        M "....."
        M "Please leave me be for a moment."
        jump prepared_food
    
    "Wait until he is done preparing food.":
        $ micah_goodend += 1
        jump prepared_food

    
label prepared_food:

    "Maybe he needs some space for his thoughts. You shouldn't intrude and wait until he's ready."
    "He finishes his task behind the counter and comes over to you with a steamy hotdog in a bun."
    
    M "Hm?"
    
    MC "Oh, thanks!"
    MC "That's nice of you."
    
    M "....."
    M "Isadora told me to give you something to eat."
    
    MC "Oh? So you didn't really want to give this poor human a hearty meal?"
    MC "Do you have no soul, oh big, bad vampire?"
    
    "Your tone is teasing, and hopefully, he'll respond to it in turn."
    
    M "I, uh-- I didn't mean to make you starve, I mean..."
    
    "He looks like he's trying to fight a headache, shaking his head again, Micah blinks. He seems confused."
    
    MC "Hey, I'm just teasing you."
    
    M "Oh. Sorry, I didn't... catch on. Weird."
    
    MC "Absolutely weird!"
    MC "Maybe you also need some food, huh?"
    MC "Or your 'special blood juice'? To get those engines running again!"
    
    "Micah snorts at your bad attempt to make a joke."
    "Satisfied, you bite into your warm hot dog. It's delicious."
    
    MC "I mean, I get lethargic, too, when I'm not eating, so..."
    
    M "Hm... Yeah. Maybe I'm just hungry."
    show micah confused
    M "It's weird, I haven't had these mood swings in quite a while."
    
    MC "'Mood swings,' huh?"
    
    M "I suppose? But at the moment, it feels more like a cold fog that engulfs my thoughts."
    M "I don't like it."
    
    MC "How do you get fed, anyway? Isadora said dinner will be in a short while, so you just... drink blood from someone?"
    MC "Is it better than drinking from those bottles?"
    show micah neutral
    M "Dinner is provided by Isadora, and no, we're not drinking from humans or animals directly."
    M "She is working with donor centers for our main meals."
    M "Those bottles are filled with animal blood. Tastes different and is less nutritious than human blood."
    
    "Just as he stops talking, as on cue, his stomach starts rumbling loudly."
    
    MC "Here."
    
    "You hold out the remaining half of your hot dog."
    "Micah looks at you, surprised."
    
    MC "Or don't you eat normal food?"
    MC "You ate some popcorn earlier, so I thought you might need some carbs."
    MC "Carbs are the best."
    show micah smiling with vpunch
    M "Hahaha!"
    M "I agree, carbs are the best."
    
    "Without hesitation, he bites into the hot dog, and his teeth are dangerously close to your fingers holding it."
    "Just the approving expression as he's chewing makes the earlier anxiety fly out the window."
    
    M "Mmmmh, thish 'sh good!"
    
    MC "Please don't talk with your mouth full."
    MC "And, you made it yourself."
    MC "Not that making a hot dog is considered 'cooking'."
    
    M "Hey, it's just quick and easy! Especially if you're busy all the time!"
    
    MC "Is someone speaking from experience?"
    
    M "...Oh, absolutely."
    M "When I'm neck deep in remodeling Faraday, I tend to forget to sustain my body."
    
    "His admission is kinda cute - you can't help but smile."
    
    MC "That's the downside to being a genius, I guess."
    
    M "Genius? Aw, come on!"
    
    "Micah playfully bumps your shoulder with his own and laughs."
    M "Wanna do something fun until dinner time?"
    M "Race you to the ferris wheel!"
    
    hide micah smiling with dissolve
    "And without hearing your reply, Micah sprints off. Fortunately, competitiveness is engraved in your DNA."
    
    MC "Oh, it is on!!"
    
###FERRIS WHEEL
    scene ferriswheel

    "Your legs are burning by the time you reach the ferris wheel."
    "Micah's grinning as you try not to cough your lungs out."
    show micah smiling with dissolve
    M "Endurance might not be your strong point, but you're fast!"
    
    MC "You were at an advantage, taking off out of the blue like that!"
    
    M "Haha, yeah, that was not totally fair, I apologize."
    
    MC "Apology accepted."
    
    "Goofing around and poking fun-- Micah seems back to his usual self. You're relieved."
    "Micah skips over to a control station of the ferris wheel and tinkers with it."
    "The wheel starts humming with electricity, and the door of the cabin at the ground opens."    
    
    if ferriswheel_fear == True:

        "Wait. Does Micah really want to get in this death trap? {i}With you?{/i}"
        "Your pulse, still going strong from the sprint, is a jackhammer within seconds."
    
        MC "W-wait, do you really want to go in there?"
    
        M "On the ferris wheel, yeah!"
    
        "A carefree smile meets a terrified gaze. Thankfully, Micah catches on quickly."
        show micah confused
        M "Are you afraid, little one?"
    
        "The nickname catches you off guard, you were transfixed by the sheer height of the ferris wheel."
    
        MC "Yes, very much so-- please don't think I'm weird--"
        show micah neutral
        M "Shh, it's okay."
        M "You're okay, [MC_name]. Look, I thought it'd be nice to go on this ride with you."
        M "I'm not going to leave your side, yeah?"
        M "This ride is Super Safe Certified! I check it every week, and it runs smoothly."
    
        MC "Mh-hm."
    
        M "And it's a slow ride! No fast movements, just a slow, safe ascent."
        M "We're safe in the cabin with the door closed."
    
        MC "...Okay."
    
        "As you slowly warm up to the idea, Micah holds out his hand to you."
    
        M "I'll hold your hand, okay?"
    
        "He has valid points. And since Micah's doing the maintenance, it's must be a reliable, safe ride... right?"
        "And you'll probably enjoy it - with him."
        "Swallowing down your fear, you take his outstretched hand and join him in the cabin."

        jump wooden_seat
    
    else:

        MC "Did you hijack this ride just now?"
    
        M "Nah, I do maintenance on it every week, so I've got permission."
        M "Actually, I've got permission to use all rides, whenever!"
    
        "The perk of being the fix-it guy, huh?"
        "Micah probably rode all of them before, until he was tired of them. That's what you would do if you'd live as long as he does."
    
        M "Come on!"
    
        "He offers you his hand, and with the blinking lights illuminating his warm smile, he's {i}dazzling.{/i}"
        "Your heart, still going strong from the sprint, skips a beat."
        "You take his hand with a sure grip and join him in the cabin of the ferris wheel."

        jump wooden_seat
    
label wooden_seat:
    show micah neutral
    "The wooden seat you pick opposite Micah is well-worn, but still hard. The doors close and the wheel starts turning."
    
    M "Sorry to drag you out here all of a sudden."
    M "I... wanted to tell you something."
    
    "You study the thinking crease between his brows. It seems to be important."

menu:

    "I'm all ears":
        M "Haha, thanks. Sorry, that came off more grim than I wanted."
        jump say_sorry
    
    "Do you want to propose?":
        show micah shocked
        M "Wait, what?"
        M "Oh, because of the ferris wheel and... Ah."
        M "Sorry to burst your dreams."
        
        MC "It was a JOKE, Micah!"
        show micah neutral
        M "All right, all right! Maybe my opening line came off more intense than I wanted."
        jump say_sorry


label say_sorry:
    show micah sad
    M "I wanna apologize for the scene earlier in the tent. With Lark."
    M "Sometimes, we just butt heads over fundamental things."
    
    MC "Yeah... I was wondering about that."
    
    M "Even though we've lived together for so long, it's still a rocky relationship."
    M "Don't get me wrong, I love all of them, but..."
    M "Hm."
    
    "The hand holding yours squeezes a little."
    
    M "Y'know, my birth family was not really wealthy. My parents were simple farm workers, working the land for the owners."
    M "Paying loans, working from dawn till dusk, paying for the kids, for food..."
    M "I was one of those kids. \'Ungrateful,\' my father always said. Well."
    M "You had to eat whatever mom cooked, regardless of our own predilections."
    M "My older siblings helping out on the farm, my younger siblings raising themselves until they would become farmers."
    M "And I... just... wanted to do something else."
    
    "You can picture it: Micah collecting spare parts he found, tinkering with them, making scrap work again."
    
    MC "Lemme guess. Your hobby?"
    show micah smiling 
    M "Haha! I'm pretty obvious, yeah?"
    M "But it was more than wanting to become an engineer."
    show micah sad
    M "I wanted to be myself. Not the version my parents saw in me."
    
    "He squeezes harder."
    
    M "When you're a kid, it's easy getting away with wearing pants, y'know."
    M "It isn't once you start to go to school."
    M "I got beaten daily by my father, and after a while by my older brother."
    M "They just didn't understand."
    show micah neutral 
    M "Aurel did, though."
    
    MC "Aurel? How does he come into play?"
    
    M "I met him by pure chance at a bookstore."
    M "Picture it: My scrawny teenage self, bruises everywhere, torn clothes, because I had just run away from home."
    M "Me, this dirty urchin, trying to shoplift a book on mechanical engineering, being approached by a gentleman in fine clothing."
    
    show micah smiling
    "He laughs at the nostalgic memory."
    
    M "I probably peed my pants a little."
    M "But he didn't rat me out-- instead, he offered to buy me that book, can you believe it?"
    
    MC "Somehow, I can, yeah. It fits."
    
    M "Yeah, you're right!"
    M "And he left an impression on me, y'know? Him, standing tall, broad shoulders, fine clothing, being able to buy any book you ever want?"
    M "I really wanted to be like him. ...Please don't tell him this."
    
    MC "I will use this as leverage at a certain point in time, thank you."
    
    "He laughs."

    M "I will deny everything and plead the fifth."
    
    MC "Hehe, we will see!"
    MC "Really, though. I get what you saw in him. Aurel has this... air around him, this charm."
    
    M "Indeed. And I'm grateful he took me under his wing."
    M "...Well, actually, I annoyed the living hell outta him and never left his side, but that's the details."
    M "He got me like no one before. And gave me the blessing of eternal life."
    
    MC "In exchange for drinking blood on the regular."
    
    M "That's a small price to pay. And you always have to pay something in return for favors."
    M "And here at Festum Atrosum, under Isadora's protection, we have a stable food supply. A place to stay. We don't have to hide."
    
    show micah empty
    "His smile turns sad, and his reasoning sounds like a re-affirming mantra he has to tell himself to cover up... what?"
    
    MC "That's true, but... are you still happy?"
    
    M "....."
    M "Aurel would probably say something like: \'Happiness is a fleeting concept.\' Pfft. Yeah."
    M "I dunno If I'm happy. I tend not to dwell on it too much."
    show micah smiling
    M "I am happy now, though! Tonight was fun."
    
    "Your cabin of the ferris wheel approaches the top of its rotation. The vast space of the carnival and the unattainable land behind it is glimmering in the dark below."
    
    MC "And leaving this place?"
    MC "If we somehow break this weird curse that traps us here, we could leave and... find happiness."

    M "...Hm. Maybe..."
    M "The outside couldn't be so bad, if everyone is like you."
    M "And, I think, with you by my side... With you, I'd feel... safe."
    
    "Micah's sad smile evolves - like a cocoon to a butterfly - into a genuine, happy smile."
    
menu:

    "This smile really suits you." :
        $ micah_goodend += 1
        "Even in the dark you notice a blush creep into Micah's cheeks."
        
        M "Thank you."
        M "I haven't... felt like this before, you know."
        M "And I, uh, kind of don't know what to say to that?"
        
        jump breakdown
    
    "Sorry, was this too corny?":
        M "I don't think so?"
        M "It's really sweet of you to say that."
        
        jump breakdown



    

    
    
label breakdown:
    
    "Without hesitation, he turns your hand and supports it with his own."
    "Before you can say anything or crack a joke to break the tension, he lifts your hand and plants a feather-light kiss to your ring finger."
    "The world is still for a long moment, frozen in time."
    "Only you and Micah in this small cabin on the highest point above the carnival, overseeing a sea of lights."
    
    MC "...Wait."
    MC "Is the ferris wheel not moving?"

    "Micah looks through the window and frowns."
    show micah confused
    M "You're right. It stops at the top, but it should've moved on by now."
    M "Hm, I don't hear the flow of electricity... Has it broken down?"
    
    MC "...You mean the power's out?"
    
    M "Could be, it's hard to tell."
    
    "The ferris wheel still isn't moving. You try to stifle the panic rising in your gut."
    
    M "But it's no biggie, I'll just climb down and put it back on!"
    
    "Without further ado, he stands up, and the cabin starts swinging lightly."
    
    MC "{i}Climb down?{/i} You want to climb down this metal contraption and leave me in this cabin?!"
    
    "Micah moves to open the emergency hatch on the door, and speaks over his shoulder."
    show micah smiling 
    
    M "Do you want to climb along? I mean, if you're up for it, why not!"
    
    "The door opens and cold air sweeps in. Goodness, you are high up. You can't look outside."
    
    MC "T-that's not what I meant! Just don't leave me here, please!"
    
    M "Hm, guess we'll have to improvise, then!"
    
    "Micah's thought process takes a split second before he grabs you under your arms and hauls you over his shoulder like you weigh nothing to him."
    "You can't process what's happening, and instinctively hold onto him."
    
    M "Okay, little one, hold on tight!"
    hide micah happy with dissolve
    
    "Before you can veto Micah's impromptu plan, he grabs the column overhead and swings you two outside the cabin."
    "Someone is screaming in the distance. It might be you."
    "As you try not to let go, Micah's amused laughter mixes with your high-pitched shrieking, and he slides down the ferris wheel frame like a firefighter on a mission."
    "A spare thought, somehow not occupied with screaming for your life, notices how agile Micah is, and how easily he's zipping down the metal beams."
    "The ground is coming closer {i}way{/i} faster than you like--"
    "Micah's feet land safely on the ground, and he puts you down with care."
    "Maybe you're still whistling like a teapot, but it could be the shock playing tricks on your ears."
    
    show micah smiling with dissolve 
    M "Screaming is {i}your{/i} hobby, huh?"
    
    "His laughter pulls you out of your panic spiral, and you try to take deep breaths."
    
    MC "This is the worst day of my life. It must be."
    
    "Micah doesn't seem to hear you, because he's already over at the main console."
    "No lights are blinking and you don't need to be a technician to know that the power is out, like he suspected."
    show micah confused
    M "This is bad. This has never happened before."
    
    "He tries a few things as you try to calm your shaking hands, but nothing seems to be working."
    show micah sad
    M "This is really bad."
    
    MC "It's not fixable?"
    
    M "I'm not sure. I haven't had this specific problem before."
    M "There cables are in, nothing is broken or cut..."
    M "It must be a problem with the generator itself."
    M "I should go take a look at it. There's more things running on that generator than this ferris wheel."

    MC "Okay, where to?"
    show micah neutral 
    M "There's an underground tunnel where the generator is kept. Come with me."
    hide micah neutral with dissolve
    "You understand how important fixing the generator is, but at this moment, you'd rather sit down and cozy up in a blanket."
    "Everything that has happened today was just a lot."
    "But when Micah takes your hand ever so gently in his to pull you along, you know you can pull through just a bit more."
    
###CATACOMBS
    scene black with dissolve 
    #catacombs is just black on purpose i sw ear
    "The entrance is an old mossy door with a long staircase behind it. It looks right out of a castle, with big, uneven stones."
    "Micah has procured a flashlight from one of his many, many pockets to light the way down."
    "As you two descend, the stairs become more slippery from the damp air. Good thing Micah is still holding your hand in his strong grip."
    "It makes you feel safe, and you remember Micah's confession that he feels safe with you. You squeeze his hand."
    
    show micah neutral with dissolve
    M "I haven't been here in ages."
    M "And that means something."
    M "Never liked coming here. Too spooky."
    
    MC "\'Spooky\' is underselling it..."
    MC "There is no lightsource whatsoever. Who built this tunnel?"
    
    M "I really have no idea."
    M "And the air's so sticky, ugh. When was the last time {i}anyone{/i} was down here?"
    
    "He's right, the air is getting warm, and damp-- sticky. It's gross on your skin, and you really want to leave as soon as possible."
    "And it smells pretty bad. You identify mold, but there is a sweet undertone. Gross."
    
    M "That's one of the downsides of being the handyman. Sorry to drag you into this."
    
    MC "Nah, it's fine. Could be worse, like jumping down from a 200 feet high ferris wheel."
    
    "With your last word, you reach the bottom of the stairs. How far below underground are you? Good thing you're not claustrophobic, because the ceiling is pretty low."
    "Panning the flashlight around, you see a dark tunnel ahead with stone arches on the walls and--"
    
    M "The generator!"
    
    "Luckily, it's close to you, so Micah goes right to work. He puts down the flashlight so it illuminates the ceiling in order to free up his hands."
    "Keeping close to him and letting him do his magic, you look down the pitch-black tunnel. You really need to leave sooner than later."
    "Also, the smell is giving you a headache."
    "In a split second, as you turn around to Micah again, you see something moving."
    "A flash of gold."
    "Your blood freezes, and the déjà vu makes your stomach drop."
    "Were those the same eyes you saw earlier in the maze? Although it feels like aeons ago, you know that they are the same eyes."
    "You take a few steps down the tunnel, but not too far from the light source. Before you is a stone arch, like a doorway to a bigger room behind it."
    "The smell-- no-- the {i}stench{/i} is overwhelming. You can't see much, but you don't need to: there is an arm on the ground right before your feet."
    
    MC "Eek!" #with hpunch?
    
    "You almost jump away from it, but your eyes are glued to the severed arm laying on the ground before you."
    "You dare not look further, but you can't help yourself."
    "In the dark, you can only see shadows of a grotesque pile. The metallic smell of blood is thick on your tongue, and your knees are on the verge of giving out."
    "Bodies. Piles and piles of them, blood-drained with the limbs severed away."
    "You try to swallow with a dry throat."
    
    MC "T-this can't be..."
    
    "You take a step back and flinch as you see the same golden eyes down the tunnel again."
    "This time, you--"
    
menu:

    "Go and see for yourself.":
        hide micah neutral with dissolve
        "You take your adrenaline-fueled legs down the tunnel until you hear a light chuckle."
        I "You're a brave little human."
        
        "The owner of the golden eyes materializes in front of you."
        MC "I knew it."
        MC "You have been watching me this whole time, didn't you?"
        
        I "Well, I have to know what's going on, don't I?"
        I "With you snooping around."
        
        "She gives you a disapproving look."
        
        I "I don't like you intruding , and taking Micah away from me."
        I "He's mine, you know?"
        I "And none of your sweet little promises of a {i}life outside the carnival{/i} will change that."
        
        MC "Micah can decide on his own what he wants!"
        
        I "No, he won't. Because he doesn't know what's good for him."
        I "All he has to do is keep the carnival running and be happy."
        
        "Isadora touches your chin with a finger and lifts it."
        "An ice-cold shiver slides down your throat and takes hold of your heart."
        
        I "And all I have to do is to keep him fed."
        
        "You want to give a witty retort, but your strength has left you, and you feel cold and numb all over."
        "All you can do is glare at Isadora's smiling face and with great effort, you grab her wrist."
        "You are too weak to move her away from you. Your senses are failing you."
        
        I "You will make a good meal, little human."
        I "Just like your useless friend."
        scene badend with dissolve
        
        "You can hardly hear her anymore. It's like a blanket covering you, and your sight is dimming. Isadora is taking every ounce of energy from you."
        "The last thing you hear is breaking your heart."
        
        I "Oh, Micah!"
        I "Come over here, it's dinner time!" 
        pause (1.0)
        jump game_end
    
    "Stay with Micah.": 
        $ micah_goodend += 1
        jump staywith_micah


label staywith_micah:

    "You need to get out, NOW."
    "Running back to Micah, you clumsily bump into him."
    show micah shocked
    M "Hey, little one, you okay? You're as white as a sheet!"
    M "I'm almost done here, just fixing this cable, and..."
    
    "A deep electrical hum emerges from the generator and Micah pats away the sweat from his forehead."
    show micah neutral 
    M "This should do it."
    
    "Conflicted, you bite your lip. Should you tell Micah what you've found and tear down the illusion that Isadora has conjured?"
    "Or is ignorance really bliss, as they say?"
    "No. Micah needs to know the truth. That the blood he's drinking isn't donated voluntarily."
    
    MC "Micah, I..."
    MC "I might know where your food supply comes from."
    
    M "What do you mean?"
    
    MC "T-there's bodies down the tunnel. Lots of them."
    
    "The truth hangs between you like a ticking time bomb."
    show micah shocked
    M "You mean that..."
    M "The donor centers are a lie, aren't they?"
    
    "There's terror in his voice and in your heart. You don't know what to say, how to console him."
    show micah neutral 
    M "....."
    M "We have to go and tell Aurel and Lark."
    
    "He takes your shaking hand in his."
    
    M "Let's scram."
    
    "A last look into the tunnel, where you saw those golden eyes. They're gone now, but you know that they are still watching."
    
    MC "Gladly!"
    
    "You take his hand and try not to look back, but you just know that Isadora has been and still is watching your every step around this carnival."
    hide micah neutral with dissolve
    scene black with dissolve 
###MAIN TENT
    scene bigtop with dissolve 
    
    "You two make your way over to the main tent as quickly as possible."
    "As you reach the main tent, you see Aurel and Lark talking. They notice you and Micah, and mirror your worried faces."
    show aurel shocked at left
    with dissolve
    Au "Has something happened?"
    Au "You look terrified. Both of you."
    show micah neutral at right
    with dissolve 

    "Understatement of the year. But the words are stuck in your throat."
    
    M "Aurel, we..."
    
    "Even Micah doesn't know how to put what you've just seen and realized into words."
    show aurel neutral 
    Au "Take a deep breath, Micah."
    Au "In your absence, I've revisited the pact we made years ago, and it might be a clue to what happened to [MC_name]."
    
    "He flips open a notebook and skims the text for the right passage."

    Au "All right. When Isadora and I made the pact, we bound it in Latin."
    Au "{i}Omnes manere in Festo Astroso debent, adhuc tres avent simul relinquere{/i}."
    Au "My Latin is rusty; give me a moment, and I'll translate."
    
    "You give Aurel time to translate the pact and look over to Micah to see how he is doing."
    "He notices you and gives you a reassuring smile."
    show aurel neutral at fourc 
    with move
    show micah neutral at fourd 
    with move
    show isa angry at fourb
    with dissolve
    show lark neutral at foura
    with dissolve
    #god help me w t hese fucking sprite call 
    
    I "And what do you think you are doing?"
    
    "Her voice is like cold steel, cutting through the agitated conversation."
    show micah shocked
    show lark empty 
    "Micah goes rigid beside you, and Aurel stops breathing for a second."
    "Lark flinches visibly, ducking his head."
    

    I "Conspiring? Or just talking?"
    I "Aurel, tell me."
    
    show micah neutral
    show lark neutral 
    "Aurel composes himself pretty quickly and stands straight - maybe to brace himself for what's coming."
    
    Au "We are not conspiring against you, Isadora."
    Au "All we were doing was talking about the pact we once made. So we can help [MC_name]."
    show isa neutral 
    "Isadora's face shows clear as day that she doesn't buy his deflection."
    
    I "And apparently, you have found something?"
    I "Something helpful?"
    
    Au "We revisited the pact, and it says that..."
    Au "All must remain at Festum Astrosum until three simultaneously desire to leave."
    
    show isa angry
    I "So..."
    I "You {i}are{/i} conspiring against me."
    
    "A condescending tone, a neutral, unaffected face. The other side of her coin of emotions."
    "Micah steps up and holds out his hand, palms open, as if he's talking down a dangerous creature."
    show micah angry
    M "No, we are not. Please, listen, Isadora."
    
    "She bares her fangs, snarling at Micah."
    show micah shocked
    I "I can't believe this."
    I "....."
    I "I can't accept this!"
    
    "Her roar makes you flinch."
    
    show micah neutral
    M "Isa--"
    show isa angry with vpunch
    I "You ungrateful imbeciles!"
    I "You want to leave this place? You want to leave ME?"
    
    "She takes a step towards Micah."
    
    I "You can't. I give you everything you need to live your life to the fullest."
    I "I'm giving you a family."
    I "I'm giving you a job. A purpose."
    
    "Another step. Micah drops his hands."
    show micah empty
    M "That's true, but..."
    
    "Isadora doesn't listen and takes another step."
    
    I "I feed you and give you a home."
    I "And just because someone new shows up and promises you the stars, you want to throw all of this away?"
    
    "Her voice is dangerously low as she steps right into Micah's personal space."
    
    I "I give you... happiness."
    
    "The tension between them raises your hackles and you feel the urge to intervene."
    
    MC "And at what cost?"
    
    "Her head whips around to face you, a jagged mask of ire."
    
    MC "So you can feed off them forever?"
    
    I "[MC_name]..."
    I "You think you're oh so smart, don't you?"
    show isa smiling
    "Ire is switched for another manic smile, like mixing a deck of cards and picking a new one."
    show micah sad
    M "Isadora, please--"
    
    I "Shut up."
    show micah empty
    "Micah closes his mouth so fast his teeth clack loudly in the silence."
    
    show isa smirk 
    I "So you think you have it all figured out, hm?"
    
    MC "Don't play games, Isadora, I know you're using these three to feed yourself."
    MC "You don't need to drink blood, do you?"
    MC "Every time you do this thing to Micah... You drain him of his happiness. His energy."
    
    "In answer, Isadora giggles."
    
    I "That's right. But aren't I allowed to?"
    I "I provide food for him and the others, after all. It's give and take. Don't tell me this has changed after all these years."
    
    MC "By luring carnival guests in and killing them?"
    MC "That's disgusting!"

    show aurel shocked
    show lark shocked 
    "Aurel flinches at the truth, gasping. Lark's horrified gaze tells you he didn't know the truth, either."
    show lark neutral
    show aurel neutral 

    I "Hm. You might think so, as you are human, but humans are nothing more than livestock."
    I "Livestock with free will, yes, but there are so many of them! Nobody will miss any of these humans."
    
    MC "Of course they will be missed, they might have had family, friends--"
    
    I "Like you do, I suppose?"
    show isa smiling
    "Her grin resembles a grotesque cut."
    
    I "Good that you are one friend less, then."
    I "And your family won't miss you."
    
    "Before any of these words can sink in and utterly destroy you,  Micah moves to stand in front of you."
    "His broad back shelters  you from Isadora and her admission."
    "She... {i}She killed and drained Andy in cold blood{/i}."
    show micah angry 
    M "Don't you dare hurt them."
    M "Or I will take you on."
    
    "Micah doesn't wait for Isadora's reply and turns around to you, taking you by your shoulders."
    show micah sad
    M "Are you all right, little one?"
    M "We have to go."
    M "This place... can't be my home anymore."
    
    "Looking over to Aurel and Lark, Micah fights to retain his composure. A plea in his eyes toward the others - the closest thing he has to a family."
    "Aurel's eyes are stormy, trying to keep it together, and nods."
    M "Lark... please."
    
    "There is no time for Lark to answer as Isadora stomps her foot and the ground starts shaking."
    
    I "You don't get to take my pet away, don't you dare, Micah!"
    I "And [MC_name] will stay!"
    
    "Over Micah's shoulder you see her launching at you, and act on instinct; you grab Micah's hand and start to run."
    
    MC "We have to go, now!!"
    hide micah sad with dissolve
    hide isa smiling with dissolve
    hide lark neutral with dissolve
    hide aurel neutral with dissolve 
    
###ENTRANCE GATE
    scene carnival with dissolve
    #TODO: replace or smthn, this is a placeholder
    "You're running again, with fear powering your legs and making your heart beat faster, Micah's hand in yours."
    "Hopefully, Aurel and Lark are right behind you, but you have no time to look back."
    "Your rushed escape ends abruptly in front of the entrance gate."
    "As before, your feet won't budge another inch. Stupid curse."
    
    MC "Oh no..."
    
    show micah shocked at fourb
    with dissolve
    M "Aurel! Lark!"
    M "We have to leave this place!"
    show aurel shocked at fourc
    with dissolve
    show lark shocked at fourd
    with dissolve
    Au "Yes, we do. But... as the pact says, we will remain until all three of us desire to leave."
    show aurel neutral 
    show lark empty
    "The three of you turn around to Lark, who has followed you, surprisingly."
    "He looks conflicted, licking his lips."
    
    M "All three of us, Lark."
    M "We have to want this together."
    
    L "I know."
    L "I KNOW, but--"
    
    show isa smiling at foura
    I "You won't leave me, my beloved Lark."
    
    "Of course she's caught up, and didn't even break a sweat. Her saccharine voice is getting on your nerves."
    
    I "I give you everything you need."
    I "And Micah. You are happy here, repairing facilities, having time to be creative, no?"
    show micah empty
    "Before you can stop her, she touches Micah's arm and in slow-motion you see Micah's face crumble like a dune under the sea."
    "It breaks your heart."
    
    MC "NO!!!"
    
    "You push Isadora away with a rough shove, turn towards Micah and try to make him snap out of it."


########################
    if micah_goodend >= 2:
        jump micah_goodend
    else:
        jump micah_badend
    
label micah_goodend:
    MC "Micah, please! Look at me!"
    
    "You take him by his hands and rub a thumb over it soothingly."
    "Out of the corner of your eye, you see Lark, shock streaking his face."
    show lark shocked 
    L "...Micah?"
    
    "Micah groans, squeezing his eyes shut. You know hes fighting, and all you can do is be there for him."
    show isa neutral 
    I "Hmmm...."
    I "Negative emotions are just not the same as positive ones."
    I "They still suffice, though."
    
    "With tears welling up in your eyes, you turn to Isadora."
    
    MC "When will you stop this? When will you have enough?"
    
    I "Is that a rhetorical question? It must be."
    show lark angry
    L "Isadora. What have you done?"
    
    I "Another dumb, rhetorical question? This time from you?"
    
    L "You drained way too much!"   
    L "You drain him way more often than Aurel or me, but this time... Micah won\'t..."
    
    "You don\'t quite understand what Lark is getting at, but filling in the gaps, it doesn\'t look good."
    "Isadora has drained Micah more often than the others? Probably because of his sunny character. But what about repercussions?"
    
    I "Psh, he\'ll live. He always does."
    I "And I can do whatever, whenever I want to him. To any of you!"
    
    "The finality of her words seem to change something within Lark. He growls."
    
    L "No, you can\'t."
    show isa shocked
    I "...What?"
    
    "Micah slowly blinks and seems to gain back his senses. You give him an encouraging smile."
    show aurel angry
    Au "Lark is right. You can\'t do whatever you want with us."
    Au "If we three want to leave, from the bottom of our hearts, we will."
    
    "He turns on his heel and lifts his cane to press the button next to the gate."
    "The old gate opens slowly with a groaning, iron sound."
    show isa smirk 
    I "And you really want this? \'From the bottom of your hearts?\'"
    I "Don\'t make me laugh!"
    
    "Still creaking, the gate continues to open, and Isadora hisses."
    
    I "Just because this human came along, you want to throw away everything we\'ve built together?"
    
    "Without deeming her worthy of an answer, Aurel turns around and steps over the barrier like it never existed."
    
    Au "Farewell."
    show isa shocked
    "With wide, panicked eyes, Isadora is speechless for a moment. She never expected this to happen."
    
    I "T-this is ridiculous!"
    I "This is not how it\'s supposed to be! How can you leave me like this?"
    
    L "Because you are cruel, Isadora."
    show isa sad
    I "But-- I love you, Lark!"
    I "We\'ve always been together! I\'ve always done what\'s best for you!"
    
    "But her pleas fall on deaf ears. Lark still looks shaken."
    "He looks over to Micah. A tentative smile settles on his face when he sees that his brother seems to be getting better."
    "A resolute strength shines through as he speaks."
    show lark annoyed
    L "You have always done what\'s best for {i}YOU{/i}, Isadora. Goodbye."
    
    "Lark turns around and passes the threshold to join Aurel."
    
    I "I- I..."
    
    "Micah watches the scene with bewilderment. You guess he never would\'ve thought it possible to leave."
    "You look at each other and there is understanding and unwavering trust."
    
    MC "You\'re back. I\'m glad."
    
    show micah neutral 
    M "I guess? Still got a headache, though."
    
    MC "Do you want to go after them?"
    
    M "Only if you come with. And hold my hand."
    
    I "N-no, you can\'t go, Micah!"
    I "What about everything you\'ll leave behind? What about your pet project?"
    
    M "I\'m leaving Faraday behind with a teary eye."
    M "But I\'ll go forward and gain something else."
    
    I "No, please, don't leave me, too!"
    
    M "....."
    M "You know that I will. Because you just used me for your own gain."
    M "And you will never again."
    show micah smiling
    "He takes your hand and grins."
    
    M "You ready?"
    
    MC "Whenever you are!"
    
    hide isa sad with dissolve 
    show micah smiling at center
    hide lark annoyed with dissolve
    hide aurel angry with dissolve
    "Both of you start sprinting towards the gate, no hesitation or what-ifs holding you back."
    "As you pass the barrier, you can see the morning sun painting the sky in beautiful pastel colors and a beautiful turquoise."
    "Just like Micah's eyes."
    
    M "Hey guys, we made it!"
    
    "Micah's cheerful announcement overshadows Isadora's painful scream. You turn around, looking back to the carnival and see a cloud of dust falling to the ground."
    "You feel no remorse, just relief and... Sadness. You think of your best friend, who you will never see again."
    
    M "Hey, [MC_name], you okay?"
    M "You're crying."
    
    "And yes, there may be tears sneaking up on you and rolling down your cheeks, but you smile at him."
    
    MC "I'm okay. It was just a long... night.."
    hide micah happy with dissolve
    scene black with dissolve
    pause (1.0)
    
    ###END

###FARADAY SCENE

    "The day is a sunny one and a light breeze is playing with your hair."
    "You take a deep breath and think back to a year ago - when your life had changed."
    "It's kinda spooky how the flow of time makes those memories less hurtful, less intense. It's not rose-colored glasses."
    "The loss of Andy and the existential fear have left invisible scars."
    "But life just continued on."
    
    ##CG
    scene micahgood
    $ persistent.unlock_Micah = True
    MC "Hey, Micah!"
    
    "You stroll over to Micah, who is holding a stick to throw for his canine companion."
    "Faraday is waiting in anticipation - or an order, since she can't exactly feel anticipation like a real dog."
    "But this new, updated model of Faraday can even move on her own and execute different orders."
    
    M "Oh, hey, [MC_name]!"
    M "Faraday, say 'Hi'."
    
    "Faraday barks. It's a sound file you two have chosen for her from the internet, and it sounds pretty realistic."
    "And Micah couldn't look any more like a proud dad. He is kind of a perfectionist when it comes to programming and refining Faraday."
    
    MC "Hi, Fara!"
    MC "So, how's it going?"
    
    M "She executes all of her programmed orders perfectly!"
    M "Because she is a good girl, right? Aren't you a good girl!"
    
    "Cooing over her, he pets her, although it's not really necessary. But it doesn't matter if it's necessary. He treats her like a real dog."
    "Faraday wags her tail and barks at him."
    
    M "Okay, here you go!"
    
    "He stands up, throws the stick and Faraday leaps after it. No difference from a real dog. Well, maybe less panting. And no poop."
    "You two stand side by side, watching her retrieve the stick."
    
    MC "You did a fantastic job with her."
    
    M "Thanks! You may call me 'the Dog Father' from now on."
    
    MC "...Oh my god, was that a pop culture reference?"
    MC "I'm so proud... My little Micah has grown so much..."
    MC "But, please don't let Faraday join the mafia."
    
    "Micah laughs and takes the stick from Faraday only to throw it again. You two stand so close, your shoulders touch."
    
    M "I'm still catching up on a lot. Aurel wants me to watch this show with him... I think it was called 'Drag'?"
    
    MC "You mean a drag show?"
    
    M "Yeah, that's it! We're gonna meet up tonight. Wanna come with?"
    
    MC "Sure thing! Should we get some blood bags from the donor center tonight beforehand?"
    
    M "Yeah, let's. And I need to put Faraday on her charger."
    M "This rechargeable battery isn't the best. I have to look for a new one."
    
    "Faraday comes back to you, and her pace is slower than before. She uses up a lot of energy, but Micah hasn't found a way to reduce her output yet."
    "The afternoon sun warms your back and lets her copper coat shine."
    "Wait a second. It gives you an idea."
    
    MC "Hm."
    
    "You turn your head and put on your best Italian accent."
    
    MC "How about I make you an offer you cannot refuse?"
    
    "Micah picks up on the joke and grins at you. His teeth are not something he has to hide from you."
    
    M "Care to enlighten me?"
    
    MC "Have you heard of solar power?"
    jump game_end

label micah_badend:
    show aurel neutral at fourc
    with dissolve
    show lark empty at fourd
    with dissolve
    show micah empty at fourb
    "Micah sways where he stands, eyes hollow and devoid of any emotion."
    
    MC "Micah? Micah!"
    MC "Please, say something!"
    
    "This time, he doesn't even respond to you. He just stands there, like a lifeless puppet."
    show isa smirk at foura

    I "Hmmm...."
    I "Negative emotions are just not the same as positive ones."
    I "They still suffice, though."
    
    "With tears welling up in your eyes, you turn to Isadora."
    
    MC "When will you stop this? When will you have enough?"
    
    I "Is that a rhetorical question? It must be."
    
    "She taps a finger against her cheek and turns to Lark. His eyes tell you that Isadora has drained him as well."
    
    I "Come now, pet. This was enough trouble for one evening."
    
    L "Yes, Isadora."
    
    I "Oh, and, Aurel?"
    I "I hope you will get your act together and remember your place."
    hide isa smirk with dissolve
    hide aurel neutral with dissolve
    hide lark empty with dissolve
    hide micah empty with dissolve
    ## hide all sprites u put into this scene
    scene badend
    "Her tone leaves no room for arguments."
    "Within seconds, she has all three of them wrapped around her finger, just like before."
    "The sight of them ignites a flame of despair in your heart. But you can't fight anymore."
    "You have run, screamed, and fought from the second you entered the damned Mirror Maze."
    "It's enough, now."
    "Hopelessness is spreading like poison in your gut. Isadora has won."
    "Isadora's piercing eyes - the same eyes that have watched your every step on these carnival grounds - lay upon you for the last time."
    
    I "[MC_name], why don't you come here?"
    I "If you say you're sorry, you might be forgiven. It all starts with an outstretched hand."
    
    "With a smile that could fool you, she offers you her hand."
    
    I "I will give you everything you need - a family, food, happiness."
    
    "And you take her hand in yours. Forever."
    scene black with dissolve 
    pause (1.0)
    jump game_end
