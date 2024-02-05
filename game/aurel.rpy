label aurel:

    #Written by: FlowersforJoy (Joy)

# Black screen background
scene black

" ‘Aurel!’ slips from your lips before you can catch them."
"Reality snaps back into place, your senses along with it; you feel something hard and…wooden? Beneath your chin."
scene carnival 
#TODO: note more than anything, carnival outside, circus inside
"As your eyes peel open, you see the man you called out for. His sharp eyes bring a relief you can't explain, considering he wasn't much comfort during your brief interaction before."
"He's no Andy, but he'll do."
show aurel neutral

Au "Are you alright?"
"He doesn’t sound especially concerned.  If anything,  he sounds... confused?"
"He’s not the only one. One moment you were unamused by the simplistic nature of this maze of mirrors, the next-- Andy was gone, and everything spiraled. You were running but going nowhere, with only glimpses of images along with an unmistakable sense of dread."
MC "Andy? Where’s Andy? Have you seen them?"
Au "Everyone’s gone home, the carnival has closed."
MC "No way! How is that possible? It hasn’t been that long…"
MC "…Has it?"
show auren angry

"Something shifts in his expression. What was just annoyance is now replaced with an expression that you assume closely mirrors your own.."
"He sneers, and you catch a glimpse of sharp teeth... unnaturally sharp teeth."
"Something is wrong."
show aurel empty
Au "Come with me, quickly."
"Despite your growing unease, you don’t hesitate for long."
"You feel sick at how easily you leave this place, as if you hadn’t just been fighting for your life to do so before."
"Was it a dream? ...No. Andy was still gone."
"Whatever just happened was real…"
"You follow Aurel’s march towards the entrance."
MC "But what about Andy?"
"You're practically jog to keep up with him."
# Carnival Entrance/Exit (night variant)
scene entrance 
#TODO make sure this bg is defined as entrance, i WILL f orget
show aurel neutral at right
Au "They’ve more than likely gone. You’ll probably find them wherever home is for them.."
"He looks to you, stopping at the entrance of the carnival, the name 'Festum Astrosum' across the banner."
Au "I’m usually the one to greet guests, but you must leave."
show aurel angry at right
Au "Now."
#Route Choice #1
menu:
    "title test" #TODO max ping 
    "Ask more questions":
        $ aurel_goodend -= 1
        MC "How is it nighttime? How has it been hours?"
        show aurel neutral at right
        Au "I’ll answer any questions you have, {i}after{/i} you leave these grounds."
        MC "Why not now? I don’t understand."
        show aurel empty at right
        Au "…"
        "He opts for silence; there’s no negotiating with him. His face has darkened, and the longer you linger, the worse he looks."
    "Do as he says":
        $ aurel_goodend += 1
        #TODO Pass here??

#Aurel  not on screen right now/no Aurel 
"Despite your doubts, the night sky overhead and the vacancy of what was just moments ago a bustling carnival, you do as you’re told and walk out."
"You’ve had enough of this place for a lifetime."
"Except-"
"You’re stopped. You feel like there’s something holding you, but as you turn to look, Aurel is still standing by himself- not another soul in sight."
"You instinctively fight back and try to press onward, but despite your efforts, nothing changes. You don't move."
"Panic begins to settle in."
"You throw yourself out of the entrance, but the laws of nature no longer apply- you are drawn back each and every time, never able to set a single toe to the other side."
MC "W-what’s going on?! Aurel, why can’t I leave?"
"His hand is on your shoulder now, pulling you back."
show aurel sad  at center
Au "This isn't supposed to happen…"
"He doesn’t continue, but his anguish mirrors your own."
"He turns away from you and paces the grounds for a moment, cursing to himself."
MC "What is this place?"
MC "What are you?"
MC "You’ve got to tell me what’s going on!"
show aurel angry  at center
"Aurel stops in place and whips his head to you. He can only hold your gaze for a moment before he breaks contact, his eyes favoring his boots."
"He begins to trace his cane in the dirt. There are no discernible shapes, just erratic scribbles."
"His shoulders raise and his eyes shut, you hear no breath despite the visual of a rather large sigh."
show aurel neutral  at center
Au "Fine. You, however, cannot panic. At all. It'll make things worse."
"You nod, against your better judgment. It’s better to know than to not."
"You maintain your composure as you feel reality losing its meaning,your fear bubbling in your gut."
show aurel sad  at center
Au "You’re stuck here, in Festum Astrosum."
Au "Just like us."
show isadora mischief smile  at center
show micah smile  at left
show lark empty  at right 
show aurel shocked  at center
I2 "And so are we." #TODO: review if ?? is okay in script it is "feminine voice"
Mc "..?"
"You turn in the direction of the voice and you spot a woman with golden locks of hair in an equally eye catching outfit. It’s familiar-- you’ve seen one like it before. The woman herself,  however,  you don't recognize. . The men lagging behind her though, you do: Lark and Micah."
"Still no Andy…did they just go home like Aurel said? Was it that simple?"
"You hope so: you wouldn’t wish this fate on anyone else. Least of all Andy."
show aurel shocked  #- wherever he fits lol
Au "Isadora, they’re trapped here. How did this happen?"
"She gives him a passing glance before focusing on you."
show isadora sad   
I "I’m just as confused as you both."
show isadora smiling   
I  "What’s your name, darling?"
MC "...[MC_name]."
I  "I’m Isadora; this is Micah, and Lark."
I  "And I see you’ve already met our Aurel."
show isadora neutral   
I  "We're also trapped here."
MC "You are?"
show lark neutral  at right
L "Yes."
show micah happy  at right
M "It’s not as bad as it sounds, trust me."
show aurel sad  at left
Au "...Nor is it a fate we would wish upon you."
show isadora neutral   
I  "You may have guessed already, [MC_name]-."
M  "But we are all also vampires."
"You absolutely had not."
"Aurel nearly jumps out of his skin when she says it."
show aurel shocked  at left
Au "Isadora! What are you-?!"
show isadora smiling   
I  "Shush, it’s no good to keep secrets from them now."
"A part of you believed her, but you’d also believed you were trapped in a mirror maze, and only minutes had passed since you entered."
"You couldn’t outright deny this claim, nor could you make comfort with the fact."
MC "A-are you serious?"
show isadora mischief smile   
I  "Deadly."
show aurel angry  at left
"Aurel grits his teeth."
"His {i}vampire{/i} teeth."
"Stranger things must have happened... right?  Either way, you’re surprisingly inclined to believe her."
MC "Why are you telling me this?"
show isadora neutral   
"Isadora shrugs, of all things."
I  "You’d figure it out eventually, right?"
"As absurd as it seems, it makes perfect sense."
"Now you can’t unsee it. Everytime you catch a glimpse of their eyes, something otherworldly takes its place. Not foreign, but not familiar. Uncanny."
show isadora smiling   
I  "Please don’t let that fact frighten you. We haven’t feasted on humans in {i}centuries{/i}. Some of us haven’t ever."
"Micah impishly raises his hand."
show lark empty  at right
L "If we wanted to, we’d have already done so."
"Something about that puts you somewhat at ease. If they wanted to feed off of humans, they would. They wouldn’t have to use smoke and…mirrors."
show aurel sad  at left
Au "We are above such…outdated methodologies."
show aurel neutral  at left
Au "And we aren’t hard up for human company."
show isadora angry   
"Isadora gasps frantically at his bitter words."
I  "Now where is your hospitality, Aurel?"
show isadora neutral   
I  "[MC_name] is a {i}guest{/i} now. We should treat them as such."
"She reaches for your hands as she speaks, squeezing them once they're in her grasp."
"They’re like ice cubes, the longer you hold them the more the cold burns your flesh. If you didn’t believe before she was undead, you do now."
I "You’ll be here for a while as we get this sorted out, but we’ve plenty of food for you." 
show isadora smiling   
I  "You’ll be safe here, I promise."
"Despite what she says, you can’t feel happy with the phrasing, implication, or the {i}touching{/i}…"
"{i} /'A while./'{/i} You can’t be here for {i}a while{/i}. You need to leave now. You’ve already been here far too long."
"As if she can hear your thoughts, Isadora speaks up suddenly."
I "It’ll be okay."
"She's attempting to soothe you, but the effect is less comfort and more maddening."
show isadora sad   
I  "Poor thing, you look pale."
"She’s one to talk."
show isadora neutral   
I  "Here, you should come back with us."
show isadora mischief smile   
I  "We have food." 
"She sing-songs, practically lulling you into following her. Like a siren coaxing sailors into the water."
"You resist the urge to cover your ears."
show aurel sad  at left
"You feel Aurel’s gaze fixated on you, waiting for your response. He looks like he wants to say something, but stops himself."
"You have to speak with him, he seems like the only one willing to help you {i}actually{/i} leave this place."
#Route Choice #2
#shake your head] $ aurel_goodend += 1 #(add point)
MC "Thank you, but I need to keep trying. I'm not ready to give up just yet. I need to get home."
MC "I appreciate your honesty, and willingness to make me feel welcome. But I need to get home as soon as possible."
show isadora sad   
I  "If you insist!, our kitchen is always open and you can reach out to me if you need anything!"
show isadora mischief smile   
I  "...I think we’re going to become great friends."
"You nod absentmindedly, and she{i}finally{/i} releases your hands."
"Warmth reluctantly returns, spreading to your palms and fingertips, but it doesn’t fully chase away the ache. The sensation of Isadora’s touch lingers." 
#tell her you need to leave] $ aurel_goodend -= 1 #(take away)
MC "I can’t even think about food right now."
show isadora shocked   
I  "But you must eat…"
MC "No, I can eat when I’m home. I don’t know where Andy is, I need to leave and know for myself if they’re okay."
"Isadora drops your hands from hers. The suddenness startles you."
show isadora neutral   
I  "That’s fine."
I  "In the event you {i}aren’t{/i} able to leave, don’t hesitate to ask me for anything."
show isadora mischief smile   
I  "We’re friends now, after all."
"You nod as the blood returns, painfully slowly, to your hands."
#converge
#TODO: Everyone but Aurel leaves, he moves to the center
"The others simply wave you off as they follow back from which they came closely behind Isadora..."
"Leaving just you and Aurel. He seems determined to get you to leave. He may be harsh about it, but you both want the same thing at least."
"His company is ever so slightly preferable to Isadora’s, who nearly suffocated you in her overwhelming presence."
show aurel neutral  
"You turn to Aurel, his eyes watching the others create more distance before he speaks."
Au "Why didn’t you accept her offer?"
Route Choice #3
#I want to go home] $ aurel_goodend += 1 #(add point)
MC "I want to go home."
show aurel smiling   
Au "...Of course you do. It was a foolish question to ask."
show aurel neutral   
Au "I understand you shouldn’t be here, but I {i}unfortunately{/i} don’t have a way to get you out just yet."
Au "So I do believe it’s in your best interest to eat first."
MC "…Then we can come back here and keep looking for answers?"
show aurel smirk   
Au "Better than that, we can discuss our options over food, and return here after."
show aurel neutral   
Au "Trust me when I say I won’t rest until we can get you home."
show aurel   
Au "Not that I do sleep, but you understand."
"Knowing he’s dedicated to getting you home brings you some semblance of comfort."
"You giggle despite yourself."
MC "Were you all invited here and just couldn’t leave? Is that it?"
"What started out as a joke soon became a genuine question."
show aurel smiling   
"Aurel cracks a small smile at that."
Au "If only it were so simple…"
#[Isadora is a lot]  $ aurel_goodend -= 1 #(take away)
MC "Isadora is just {i}a lot{/i} for me."
show aurel neutral   
Au "She {i}can{/i} be quite…eccentric. It’s not just a performance she puts on for the show."
show aurel sad   
Au "I’m no better company, truthfully. But if things go as planned, you won’t be here long enough for it to matter."
"It sounds dismissive, but knowing he’s dedicated to getting you home is why you chose to stay with him to begin with."
show aurel neutral   
Au "Truth is, Isadora may have a better idea on how to get you out of here than I."
Au "Nonetheless,  I’ll stop at nothing to make sure you can leave before the next Carnival season begins."
MC "...Today was the last day wasn't it?"
Au "Indeed."
Au "It’s best we discuss more as you eat, then we can return here soon after."
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
#converge 
#Part 2
"You followed Aurel, the carnival grounds are much easier to navigate when devoid of visitors. Almost ghostly by comparison."
# Foodcourt
#(We in the food court now, I’ll transition into it smoother when my brain decides to work)
"A rat scurries by your foot."
#Personality Choice #1
#freak out] (Personality choice no points)
"You let out a yelp stepping back." 
show aurel neutral   
Au "It’s okay, no need to panic. It’s a harmless rodent."
show aurel angry   
Au "You’re just like the elephants…"
"Did he just compare you to an elephant?"
Au "Filthy things, they’re covered in fleas no doubt."
"{i}Well that’s rude!{/i}"
Au "Those traps are pointless…"
"{i}Oh, he meant the rats…{/i}"
show aurel sad   
Au "If only Charlotte were here."
MC "Charlotte? Is that another one of your {i}buddies?{/i}"
show aurel neutral   
Au "A cat I once had, actually."
show aurel smiling   
Au "Beautiful thing, pitch black, eyes like two full moons."
show aurel smirk   
Au "She was very vampire-like- she’d bleed these rats dry, that’s for sure."
"You can’t help but feel a bit uneasy at how happily he says things like that."
"However, if it kept you from encountering another rat, that was a plus." 
MC "Andy wants to have one for a pet… I’ll never understand that."
Au "That’s a fascinating concept, keeping a rat for a pet."
MC "According to them they’re very smart, and cuddly."
"You shudder at the thought."
Au "Is that so?"
"You could be imagining it, but he seems genuinely curious."
"But he doesn’t say anything more about it."
#what a cutie] (Personality choice no points)
MC "Awww, did you see that little guy?"
show aurel neutral   
"Aurel simply blinks at you."
Au "It’s a rat."
MC "I think they’re cute! I want one as a pet."
show aurel shocked 
Au "Your people keep them as pets?"
MC "My people? ...Humans?"
show aurel neutral   
Au "{i}Modern{/i} humans."
MC "I suppose; there are plenty of people that see them as pests."
Au "I don’t actively hunt them or anything. That was Charlotte’s job."
MC "Charlotte? Have I not met her?"
Au "A cat I once had, actually."
show aurel smiling   
Au "Beautiful thing, pitch black, eyes like two full moons."
show aurel smirk   
Au "She was very vampire-like- she’d bleed these rats dry, that’s for sure."
"You can’t help but feel a bit uneasy at how happily he says something like that."
"Perhaps though it was simply a fact of life. You just hope you aren’t a rat in this den of cats."
show aurel smiling   
Au "That’s a fascinating concept, keeping a rat for a pet."
MC "They’re very smart actually, soft and loveable too."
Au "Is that so?"
"You could be imagining it, but he seems genuinely curious."
Au "That says a lot about you, that you could be fond of such a creature."
MC "...Thanks?"
"You tend to think it says more about those who don't."
#Converge
show aurel neutral   

"Aurel points his cane, as if you can’t see the line of food carts set up yourself."
Au "It’s all yours for the taking. Help yourself."
MC "Weren’t we supposed to all eat together?"
MC "Wait…do vampires not eat regular food?"
Au "Of course we can. Humans have an incredibly skewed idea of what vampires can and can’t do."
Au "No reflections, can’t be in sunlight, turning into {i}bats{/i}?"
show aurel smiling   
Au "How do they come up with all of this?"
"He laughs heartily at the absurdity. You feel a bit foolish for assuming what you saw on television made sense in reality."
"Then again, vampires existing at all seemed impossible, as well as being stuck in a carnival, so…"
MC "So the only thing we got right was drinking blood, then?"
show aurel neutral   
Au "Yes, but even that-- we aren’t mindless creatures, we don’t feed upon the innocent."
Au "All of our blood is ethically sourced, thanks to our {i}dearest{/i} Isadora."
"The sarcasm oozes from his lips."
"‘What’s that about?’ You can’t help but ponder."
"Now that you think back on it, he and Isadora didn’t seem all that friendly. At least, not by your standards."
"He stops for a moment, contemplating something, before pivoting to look at you."
show aurel smirk   
"The air nearly stills; your breath catches in your throat."
"There’s something in his eyes you can’t quite make out."
"You feel as if you’re under a spotlight."
Au "Tell me, [MC_Name]."
"The way he says your name in {i}that voice{/i} makes your head spin."
Au "Do you believe we're truly vampires?"
"You swallow."
MC "Yes?"
show aurel neutral   
"There’s a beat of silence. That answer didn’t seem to satisfy him."
MC "Is this a trick question?"
"The question takes more courage than you care to admit. "
"If you didn’t believe it before, you do now. He looks otherworldly, with his eyes and those teeth-- unmistakable."
"He takes a step towards you, and despite all the exits available, you feel cornered where you stand."
"Still, your feet remain planted in place. Much like when you stood at the entrance, your body seems unable to obey your commands."
show aurel smirk   
Au "Your {i}media{/i} tells you we are monsters. You should be fleeing from me, not seeking my help. Right?"
"His eyes! Is compelling something  true to vampires then?"
"You curse yourself for not asking about that."
"You twist your wrists and shuffle your feet. No, you can clearly still move."
"Your mouth even opens, and words you didn’t think of before drop from your lips and fill the silence."
MC "Maybe it’s just what Lark said: if you wanted to harm me, you could’ve already."
Au "How do you know we aren’t fattening you up for the kill?"
"That would just be them playing with you…"
"{i}Oh.{/i}"
"You get it."
"You frown.."
MC "I guess I don’t, Aurel."
"You counter, the sweat pooling in your palms."
"Even when you’re aware of the game he’s playing, you can’t help but feel adrenaline coursing through your veins."
show aurel neutral   
"He squints at your expression for a moment before his face breaks, and he cracks a smile."
show aurel smiling   
Au "Interesting. You’re clearly terrified, and yet you didn’t run."
"Now he’s analyzing you, like he put you through some sort of test."
MC "I’m trapped here, my fate is in your hands already."
MC "What is this?"
MC "I don’t appreciate being played with."
show aurel neutral   

"The smile melts from his features. You’ve spoiled his fun.{i} Good{/i}."
Au "Even if I meant to lighten the mood?"
MC "How would teasing me at a time like this lighten the mood?"
"Aurel furrows his brow."
show aurel neutral   
Au "I only meant to pick your brain. Most would have run; they wouldn’t have questioned me."
Au "Most would have accepted Isadora’s offer."
Au "I keep wondering {i}why{/i} it is that you decided to stay with me?"
MC "You seemed like you wanted to help me leave this place."
MC "I guess I was wrong."
"Your answer comes out harsh, but you aren’t mad at the bite- nor the expression it draws from Aurel."
show aurel sad   
Au "I see."
"He shuffles uncomfortably."
Au "You should eat."
show aurel neutral   
Au "Come, let’s sit together."
"Aurel starts to walk in one direction, but stops, his shoulders sinking."
"You don’t move."
show aurel sad   
Au "[MC_Name], I’m sorry."
Au "It’s…{i}evident{/i} I haven’t had much company in this time."
"His apology comes out slowly, held back."
"You watch him falter under your gaze."
"You hate yourself a bit for enjoying it. You sort of understand why he was having fun before."
Au "I got carried away."
Au "I hoped to understand your reasoning for choosing me, and also tried to ease some of this unbearable tension."
Au "I {i}do{/i} want to help you leave this place. Will you allow me?"
"He extends a hand out in your direction. For a moment, he resembles a prince."
Personality Choice #2
#Tease Him (Personality choice no points)
"A smirk spreads across your face."
MC "If you wanted to flirt with me, you can just say that, Aurel."
show aurel blush   
Au "Huh?!"
"That seems to dissipate the tension immediately."
(Note to self: Add expressions Joy)
"You laugh. Not even attempting to explain yourself."
"It’s far more fun this way."
"Perhaps it was a harmless joke. It's kind of him to even try to begin with. Even if he is pretty shit at it."
"All those years of performing couldn’t substitute for basic human interaction; you’d have to keep that in mind."
MC "Where’s the kitchen again?"
"Aurel shakes his head trying to regain his composure."
"Flustered, he answers."
Au "...Follow me."
Au "I’ll eat with you."
#Accept His Apology (Personality choice no points)
MC "We’re okay."
"His posture instantly relaxes."
Au "Thank you."
"It comes out strangled."
"You aren’t exactly sure what to make of him, but he seems well-meaning."
"Perhaps it was a harmless joke. It's kind of him to even try to begin with... Even if it came out a tad cruel."
"All those years of performing couldn’t substitute for basic human interaction; you’d have to keep that in mind."
MC "I'm starving…"
Au "Follow me, I’ll eat with you."
# Converge 
Au "I-if you’ll have me, that is..."
"His face has the most color you’ve seen so far."
"You’re not cruel enough to further embarrass him."
MC "I’ll have you."
"You both freeze."
"{i}Okay- weird way to say that{/i}."
"Before you can flub your way out of it, Aurel speaks."
Au "Then I’ll happily be had."
"He bows, but it doesn’t seem like he’s mocking you."
"You exchange a smile before proceeding to your destination."
"Aurel leads you into the kitchen. It’s somehow nicer than you expected a carnival kitchen to be."
"Not that you’d ever put much thought into how a carnival kitchen looked, of course."
"He practically glides across the floor as he speaks, rummaging through the cabinets overhead."
Au "Can I interest you in some duck soup?"
"What you thought was a joke crumples to nothing when he holds out a can with a cartoony picture of a duck, and the words "duck soup" across it."
MC "Duck soup?"
Au "It’s a gag prop."
"You smile. What a funny thing to have in the {i}actual{/ kitchen."
Au "How about some decade old clam chowder perhaps?"
"He presents the can as if it were a fancy new invention."
"You giggle, shaking your head."
Au "I’ve never been much of a fan, myself."
"He turns his attention away from the cabinets and leans on the counter."
Au "Well, it looks like you’ll be having popcorn for supper."
"{i}‘That actually sounds pretty good{/i}’."
"The interest must show on your face."
Au "I was joking. Popcorn isn’t much of a meal."
MC "I don’t plan on being here long, I just need something to tide me over."
"He shrugs."
Au "A fair point."
Au "Popped corn it is."
Au "Wait here just a moment."
"You do as he says. Aurel exits the way you came and a minute or so later he comes back with huge tub of popcorn, and a few drinks in hand."
MC "Don't I have to pay for this?"
Au "Nonsense, there’s always free cheese inside a rat trap afterall."
"You don’t respond, mulling it over."
Au "I’m kidding, though of course it may feel like that for you right now."
Au "It’s okay, you’ll be in no danger with me."
"Despite everything, you believe him."
"He’s capable of landing a joke and lightening the mood. Just not all seem to hit their target." 
"Every reminder, big or small, is hammering it in that you are stuck here- a constant press on a bruise: insistent and too much."
Au "I didn’t know what drink you’d like so I brought you some options."
"That brings a smile to your face."
"How thoughtful of him."
Au "Which one would you like first?"
MC "Whichever one you don’t want, I guess."
Au "They’re all yours."
Au "So, which one first?"
Personality Choice #3
# water](Personality choice no points)
"You can’t go wrong with a water."
Au "A fine choice."
"He hands you the water, setting the other two into the fridge."
"He then places the bucket of popcorn on the table, and takes the seat opposite you."
# orange soda](Personality choice no points)
Au "I always wonder how anyone can drink such a thing. It’s like melted, bubbly candy."
MC "I haven’t had one in awhile. I always used to drink them as a kid."
Au "Giving a child limitless access to these is a recipe for certain disaster, surely?"
MC "I think I turned out alright."
"He hands you the /'bubbly melted candy/' drink, setting the other two into the fridge."
"He then places the bucket of popcorn on the table, and takes the seat opposite you."
# lemonade](Personality choice no points)
Au "You’ve got great taste-- even better, it’s freshly squeezed."
"That excites you."
Au "It’s quite tart, just a warning."
MC "Thank you."
"He hands you a plastic cup filled with ice, pulpy lemonade, and slices of whole lemon. Then sets the other two drinks in the fridge."
"Then he places the bucket of popcorn on the table, and takes the seat opposite you."
# converge
"You take a handful of the popcorn, surprisingly hot to the touch, and gesture to offer some of the popcorn to him, but stop yourself."
MC "So, I know vampires {i}can{/i} eat regular food, but do you?"
MC "Or is that a dumb question?"
Au "No such thing as a dumb question here."
Au "We do eat food sometimes, but there is no real sense. Nothing compares to blood."
Au "We eat mostly to play the role of being human, even if just for a moment."
Au "It’s just empty calories, and nostalgia."
"Even saying so he takes a couple pieces and pops them into his mouth."
"The popcorn is even better than what they serve in the movie theaters." 
Au "I’m going to make some tea, would you like some?"
MC "I’m good with this, thank you."
"He moves over the stove filling an old style kettle full of water before returning to his seat. With him is a gorgeous tea cup decorated with a hand painted roses and vines."
"He sets a tea bag inside and sets a- seasoning shaker?- beside it. Is paprika a common additive to tea? And does it normally look that dark? Or is it just old?"
MC "What’s that?"
"He looks down at his arrangement and cocks an eyebrow, before realizing what you were asking."
Au "This?"
"He points to the out of place jar."
Au "Blood powder."
Au "It’s commonly used to feed canines to provide them with extra iron."
"You laugh, but he doesn’t join you."
MC "You’re serious?"
Au "It helps the taste of the tea."
Au "I wouldn’t have put any in yours. Don’t worry."
"If only the inventors of dehydrated blood knew it would one day be used as a flavoring packet for tea for vampires."
"Truth was truly stranger than fiction."
"Before you can say anything in response the tea kettle screams. You steady your heart at the sound."
"Aurel brings the kettle over, delicately pouring it into his cup."
MC "What kind of tea is it?"
Au "Darjeeling Black Tea."
Au "It tastes fruity this time of year."
MC "The taste changes?"
Au "Depending on the season the tea leaves grow, it can taste more earthy or when it’s ripened it can be more fruity."
MC "Interesting, I should try it sometime."
"Aurel smiles at you before lightly shaking the powder into the steaming hot liquid."
"Before bringing the cup under his nose and taking a huge whiff."
Au "{i}Delightful{/i}."
"He practically moans it."
"Everything he does is so ...{i}theatrical{/i}."
"He looks like he’s ripped right out of an old time-y movie. You can’t bring yourself to take your eyes off of him."
"You reach your popcorn and continue to watch him."
Au "This is what I needed."
"He taps the side of his teacup with his nails, the soft clink sends a wonderful sensation through your head."
Au "If you don’t mind me asking, what is your relationship with Andy? Are you just friends?"
"He smirks as he says it."
Personality Choice #4
# Just friends](Personality choice no points)
MC "Oh no! Andy's like family to me. There’s never been anything romantic between us."
Au "Are you interested in that sort of thing?"
MC "Being in love? Yeah. Just, hasn’t really happened for me, yet."
MC "You?"
Au "I have, but like so many things, it was a lifetime ago." 
Au "I didn’t mean to pry, just making small talk."
Au "Andy seemed lovely."
MC "They are, I miss them."
#And if we are together](Personality choice no points)
MC "And if we {i}are{/i} together?"
Au "Then that’s wonderful, Andy seemed lovely."
MC "They are, but there’s never been any romantic feelings there. I love them, but only platonically."
MC "What about you? Any special someone?"
Au "No. Not in a long time."
Au "I didn’t mean to pry, just making small talk."
MC "It’s okay, I just miss them."
#Converge
Au "Let’s forget the small talk and start to discuss your options…"
Au "Hmmm."
"He seems immediately stumped, his relaxed demeanor is replaced with frustration. He sets down his tea cup only after a sip."
MC "How are you all stuck here in the first place? Did someone put you all here?"
Au "Yes."
Au "I did."
"You nearly choke on a popcorn kernel."
MC "You?"
"He doesn’t appear to be joking."
MC "Why?"
Au "For Micah… he wanted to become the man he is, physically-- it was a different time."
"Aurel makes a circling motion with his hand." 
Au "It wasn’t safe for him to live as he wanted, to look how he wanted. I wanted to keep him safe."
"He wanted to protect him… Aurel looks pained as he speaks."
MC "I see."
MC "Honestly it’s not very safe {i}now{/i} to be- well, who Micah wants to be. I can’t imagine how much worse it was in {i}your time{/i}."
"He nods, offering you the smallest hint of a smile."
Au "At the time, it seemed like the perfect idea. We could all live as we wanted without fear of being ostracized for being who we were, or worse."
Au "Isadora and I made a pact to keep us safe, here."
MC "A pact?"
Au "Yes. There was, of course, a probleM after some time we realized we couldn’t leave."
"A terrible sadness takes over his expression."
Au "It’s been decades since I’ve even tried."
"He closes his eyes."
Au "This may not inspire any hope for you, but this is the first time anyone else has been trapped with us."
"What? It made sense, you'd suspected as much, but it only brings more questions: why {i}you{/i}?"
MC "Are you serious? The first time?"
Au "Yes. However, I believe you could be the key to changing these circumstances."
MC "But that’s just a theory, you don’t {i}know{o} if that’ll actually work."
Au "That’s also true."
"Your stomach sinks, dread washing over you. The quiet realization that you may never see your home, your family, or Andy ever again tugs at your mind, your heart."
Au "But, [MC_Name], listen to me…"
"You continue to spiral."
"It isn’t until Aurel reaches for your hand that you are ripped from your thoughts."
"His hands aren’t frigidly cold like Isadora’s."
Au "I can’t promise that things {i}will{/i} go back to normal."
Au "But I promise to try. I will spend every waking moment searching for a way for you to go home."
Au "Do you understand?"
"You nod."
"You feel yourself calming down; if anyone can help you out of here, it’s him."
"It’s not hopeless yet."
Au "I’ve thought for a while that there must be some loophole, some other means to escape."
Au "The other 3 show no desire to leave, so for a while I also made peace with the idea of living here forever." 
Au "Perhaps I am foolish for thinking so, but I believe there {i}is{/i} a way. We just have to find it."
MC "I’ll help find it. If you could end up here, if vampires exist, if what happened to me in that mirror maze is real, then anything is possible."
"He smiles gently at you."
Au "Your optimism is refreshing."
Au "Micah is much the same way, however he likes it here. I don’t want to bring him down, but I’ve wanted to leave this place for far too long."
MC "Really?"
"He only nods."
MC "Well I guess it could be worse…"
MC "At least I have good company."
"His eyes widen, and he avoids yours, but reaches for his cup."
Au "I’ll cheers to that."
Au "And to getting you out of here, as soon as possible."
"You reach for your own drink and tap it against his own before taking a sip."
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
"After you put a slight dent in your popcorn and sipped at your drink you couldn’t sit still any longer."
"You walk alongside Aurel as he leads you through the circus tent, into the dressing rooms."
# Dressing Room BG
Au "I hope I wrote down the contents of the pact in my journal."
MC "When was the last time you wrote in that?"
Au "I don’t know... far too long ago. I filled it and moved to another journal."
Au "I hope I wasn’t foolish enough to throw it away…"
"You hope so as well."
"You're led into a dressing room, far more cluttered than the kitchen before, andfar more welcoming."
"There’s a vanity for everyone. Mirrors decorated with lights. (description goes here)"
"Aurel moves to the corner where his vanity is, your attention is drawn in favor of the stacks of vinyls, books, and movies lie. There isn’t enough to fill a bookcase, more than could fit in a drawer."
"The vanity is bare except for a single picture of a man that isn’t Aurel, Lark, or Micah."
Route Choice #4
#Ask about the picture] $ aurel_goodend -= 1 #(take away)
MC "Who’s that?"
"His eyes follow your finger and he recoils."
"You instantly regret asking."
Au "What does that have to do with finding a way to get you out of here?"
MC "I’m sorry."
"Obviously that touched a sore spot."
"You want to know even more now, but you know better than to ask about it."
"An awkward silence settles between you."
"Aurel begins sifting through the pile in search of his journal, and it isn’t long before he retrieves it."
#Ask about the stuff on the floor] $ aurel_goodend += 1 #(add point)
MC "What is all that stuff on the floor?"
Au "This?"
"He seems pleased you asked-- a very different reaction than your question minutes before."
Au "It’s just as you see, movies, books, music-"
MC "Obviously-- I meant more like, is it your personal collection?"
Au "{i}Personal{/i}?"
Au "You make it sound dirty."
"Your face burns. You hadn’t considered that there may be… {i}adult{/i} contents intermixed."
Au "No,there's nothing of that sort, but these are all my favorite pieces of media I’ve obtained over my time here."
Au "I can’t rent a movie or the like,of course, so what I have is what visitors or employees leave behind."
MC "You stole these?"
Au "I suppose I did. It gets terribly boring here, you understand."
MC "I guess they can easily replace it. It’s weird to bring a movie or a record here anyway."
Au "I truly treasure these. I’ve obtained more, but many of them were pure drivel."
#converge
"Aurel reaches into the pile."
"He starts to hand things to you to hold."
"First is a book, "The Color Purple;" next a movie: "The Bird Cage"; and next is a vinyl, "Purple Rain" by Prince and the Revolution."
"He hands you many more: some familiar, some completely foreign."
Au "Here it is!"
"He pulls out a leather bound journal-- it looks older than you."
"Aurel flips through the pages, chuckling to himself."
Au "This was my first journal written with an ink pen."
Au "I remember thinking how unbelievable such a thing was."
Au "I had no idea what was ahead of me."
"You can’t even imagine living through so much history, where something as simple as a ballpoint pen was innovative."
"He’s lived through the first light bulb being invented to touchscreen devices."
"You miss your phone more than ever at this moment, and you wonder- if you had it on you, could you contact Andy? Would they believe what has transpired?"
"You’ve truly been severed from reality."
Au "Here it is! Written right here, I speak about the pact I made with Isadora."
"You stand beside him reading the yellowed pages. They are filled with beautiful cursive handwriting, decorative to nearly a calligraphy level."
Au "The pact we made, I wrote it down..."
Au "{i}Omnes manere in Festo Astroso debent, adhuc tres avent simul relinquere{/i}."
Au "It’s written in Latin. I haven’t practiced Latin… give me a moment, I think I can translate."
"He mouths the words to himself a couple times over, closing his eyes to focus."
Au "I-I think the exact words were-"
Au "{i}All must remain at Festum Astrosum until three simultaneously desire to leave{/i}. "
MC "Is that it?"
MC "That’s all it says?"
Au "Yes, it seems quite simple…"
MC "So until three decide to leave…the carnival?"
Au "Simultaneously. I noted that specifically."
MC "But..?"
Au "I believe you and I are the only ones who desire to leave."
MC "You mean the others don’t want to leave? Have never wanted to leave?"
MC "And the pact wasn’t made with me in mind-- do I don’t even count?"
MC "But you all have been here forever, surely they’d want to go home by now?"
Au "Go home to what?"
"That trips you up."
MC "I-I don’t know?"
Au "The world has changed {i}drastically{/i} from when we were living out there."
MC "That’s true, but-"
"You're left speechless, but the more you think about it, the more it makes sense."
"There wasn’t anything for them out there…only you and Aurel- wait."
MC "Why do you want to leave then?"
MC "Or do you also not want to?"
Au "I {i}do{/i}!"
Au "Want to leave, that is..."
MC "But why?"
Au "I have my reasons."
"He’s being secretive, what’s the point?"
MC "Look."
MC "I understand you don’t know me that well, but keeping secrets from each other isn’t helpful when there’s a good chance I’ll be here for the rest of my life."
"He sighs deeply."
Au "You’re right, I’m sorry."
Au "I-- there is much of the world I want to see."
Au "I’ve seen snippets of the world via this media and…I know there are mountains, trenches that are filled with wonderful stories I have yet to experience."
Au "I have all this time, and it’s spent just scrounging by, living the same day over and over."
Au "Now that the season is over, I’m left with the same stories again and again… it’s been so long since I’ve experienced something new."
"When he says it, you can only imagine how maddening it must be."
"You may not even have to imagine; it may just become your new reality."
"He can’t even die."
Au "I don’t understand how you fit into this pact at all, it shouldn’t affect you. You shouldn’t be here, and yet…"
MC "Here I am..."
"You search for an answer in Aurel’s eyes, and you feel tears welling in your eyes, defeat threatening to overtake you."
MC "I won’t ever leave this place? Will I?"
Au "No, that’s not true--"
Au "I believe something must have changed."
Au "It’s far more impossible that there is {i}no{/i} way for you to leave."
Au "We can always ask the others for ideas if need be."
"Something occurs to you in this moment."
"As he says those words, just a flash, a flash of gold…a pair of eyes enters your mind."
Route Choice #5
# Speak your suspicions]$ aurel_goodend += 1 #(add point)
MC "Aurel."
"He cocks an eyebrow at you."
Au "Yes?"
MC "When I was in the hall of mirrors, before you found me…"
MC "I think I saw Isadora."
Au "Are you serious?"
MC "I’m not you, I wouldn’t joke at a time like this."
"He drops his head, wearing a defeated smile."
Au "I suppose I deserve that…"
Au "But you truly saw her? Was she there with you?"
MC "No, I thought I saw her eyes, I could {i}feel{/i} her presence."
Au "If that’s true, then…"
Au "No, I shouldn’t say."
"If he wouldn’t say it, you would."
MC "I think she may be behind why I’m here to begin with."
"He closes his eyes, flashing his teeth."
"You hit the nail on the head, it seems."
Au "It does appear that way."
Au "I’ve had my suspicions regarding her for awhile, but I worried it may just be {i}me{/i}."
MC "What do you mean?"
Au "It’s quite {i}personal{/i}... I promise it isn’t relevant to your escape."
# Keep your feelings to yourself] $ aurel_goodend -= 1 #(take away)
"{i}It isn’t helpful to take any of what I saw in that maze seriously.{/i}"
"I’ll just make this harder and more complicated for the both of us."
#converge 
Au "I need some fresh air, would you like to join me for a walk?"
Au "Moving helps me think."
MC "Sure thing."
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# Carnival Grounds
"The night air does help ease some of the stress building in your chest."
"You both walk aimlessly. The silence is comfortable. You can tell how deeply Aurel is thinking."
MC "Do you write a lot?"
Au "I do."
MC "Okay. What about?"
"You stop walking to check his expression."
MC "Or is that too personal?"
Au "No, it’s just a hobby of mine."
Au "I write critiques."
MC "Critiques? About the movies and books you have?"
Au "Yes."
MC "What do you like about it? I only thought of critiquing as a job, not a hobby."
Au "It’s both; many see criticism as pretentious, mean spirited... pointless, even."
Au "But I couldn’t disagree more. Criticism is a necessary tool for the growth of creatives."
Au "Stop me now if you’d rather not hear my feelings about this."
MC "I’m all ears."
"His smile widens for a moment before he suppresses it, clearing his throat."
Au "Well, criticism isn't /‘hate,/’ it’s the greatest form of loving something: loving it despite its flaws, and working to improve what holds it back from being truly masterful!"
Au "Also, it’s beneficial for the critic! I understand myself more, what I truly value, what grates on me, what holds me back."
Au "It’s as David Foster Wallace once said, /‘Good fiction's job is to comfort the disturbed and disturb the comfortable./’ "
"His words come out faster, and he motions with his hands as he speaks."
Au "Augh, what was that one quote?...Never the matter, the point is, proper critique holds the creator accountable and ensures growth-- or if the creator chooses to ignore it, their own demise."
"You smile and listen attentively. You hadn’t ever thought of criticism as a passion, but after seeing Aurel enthuse for the last half hour about it, you know just how wrong you were."
Au "I’m sorry, that went on longer than I intended it to."
MC "Don’t apologize, I loved hearing about it."
Au "Truly? That’s…you wouldn’t mind if I shared one of my critiques with you, do you?"
"You shake your head."
MC "Go right ahead."
"He laughs."
Au "I have one back at the dressing rooms I could grab."
MC "I’ll wait here."
I "Before you go, can {i}I{/i} have a word?"
"In an instant the light atmosphere is washed out in favor of something else- you catch a glimpse of Isadora’s eyes. They don’t match her smile."
"Aurel looks like an entirely different person."
"She taps her foot as you and Aurel approach her."
I "I don’t know what’s so funny about [MC_name] being stuck here."
I "How inappropriate can you be? They aren’t going to replace Cedric if that’s what you’re {i}trying{/i} to do."
I "I see right through you, this is {i}so{/i} unfair to [MC_name]!"
Au "I’m not listening to you attempting to slander me. Isadora! I’ve been trying to help!"
"She bares her teeth at him. Your blood runs cold."
I "I don’t believe that. Shame on you!"
Au "This is getting us nowhere."
"His voice is losing its composure."
"Aurel storms off. Surprised, you attempt to follow him when a familiar icy grip takes hold, dragging you back."
Route Choice #6
# shake her off] $ aurel_goodend -= 1 #(take away)
"Before she can get a proper grip, you jerk your shoulder."
"Leaving her behind."
"She attempts to call out for you, but you don’t listen."
"You focus on following the path you watched Aurel go."
# listen to what she has to say]$ aurel_goodend += 1 #(add point)
"Isadora shakes her head."
I "I’m sorry I didn’t warn you before, [MC_name]."
MC "Warn me of what?"
I "Aurel."
I "He’s lonely, I know that, but I didn’t want to think he’d try to flirt with someone stuck here."
MC "But Aurel {i}has{/i} been helping me."
I "Are you sure? Or is he just doing that so you’d stick with him?"
I "He knows you’re desperate to leave." 
I "But we made the pact together and {i}I’m{/i} telling you, you cannot leave this place."
"{i}No{/i}!"
MC "I can’t leave?"
I "Lark and Micah know it too."
I "I wanted to make you comfortable here. I wanted to break the news in a better way than this."
I "But when I saw him getting all {i}close{/i} to you… I knew I had to step in."
I "You must understand."
I "I don’t want to hurt Aurel, but he can’t get away with this."
I "We’ve all had to sacrifice so much. He can’t just make a lover out of you because he misses Cedric."
"What she says makes sense, but for some reason you just can’t believe it- something is off."
"But you know better than to tip Isadora off. You have to speak to Aurel, you have to hear {i}his{/i} side."
MC "Thank you, Isadora."
"The words taste sickening as they exit your mouth."
MC "I understand what you’re saying. I had my own suspicions."
MC "It’s going to be a huge adjustment living here... forever."
"You know something is missing, that everything isn’t as it appears. Isadora most certainly has something to do with it- but you hope-- {i}pray{/i} that what she says about the pact isn’t true."
"That there {i}is{/i} a way you can leave."
I "You did?"
I "You’re always so incredibly perceptive [MC_name], I’m impressed!"
"Her friendliness is overwhelming…"
MC "Thank you. Before I go with you, I need to get my bracelet. I left it with Aurel." 
"She gives you a look, a look that may suggest she’s not entirely buying what you’re selling her."
MC "It’s really important to me, it was a birthday gift from my friend Andy."
I "I could get it for you."
"{i}No{/i}! It has to be you, you have to speak to Aurel first."
MC "I appreciate your offer, but I want to diffuse this tension."
MC "I mean, since we’re going to be living together, I don’t want to be on bad terms."
I "You’re right, he’d most surely refuse to give me the time of day."
I "Alright. When you’ve retrieved it, come find me and the others in the circus; Lark and I need to practice anyway."
MC "I’ll be there."
I "Don't keep me waiting too long, dear."
"She giggles, but it doesn’t feel any less threatening."
#converge
# Dressing Rooms BG
"It doesn’t take you long to locate Aurel. He sits at his vanity, sulking, looking at the singular object on it: a photo of a young man."
"As you approach, you study the picture closer."
"It’s what you’d expect from an old time-y photograph: grainy coloring, light leaks, and stiff posing. Even so, the man in the photo is handsome."
"Without asking, you know who this man is-- or rather, his name."
Au "You’re {i}not{/i} a replacement for Cedric."  
"Aurel pivots from the photo to you."
"He looks as if he was just mourning at a tombstone."
"You dare not even ask what became of Cedric, or who he was. It’s written all over Aurel’s very being." 
Au "You’re not a replacement for {i}anyone{/i}."
MC "I {i}know{/i}."
"You whisper, reaching for his hands."
"You’re filled with sunshine when he lets you take them. You squeeze them encouragingly." 
"He lets out a shaky breath at that. He gives you a small smile."
MC "What she said to you was so…"
"You take out your mental thesaurus."
MC "Uncharitable."
"He breathes out a laugh, amused by how strange it sounds coming from you."
Au "It’s alright. We’ve not gotten along for decades."
Au "Everytime I try to speak with Micah, and especially Lark, she hovers over me-- like I mean to lure them to hell’s gates."
Au "I’ve only ever wanted what I thought was best for them."
Au "I know I’ve been wrong before, but she won’t give me the chance to be right."
"Your heart aches at that. How long has Aurel been alone here, isolated from the others?"
"Then another, even more horrible thought occurs to you. Are you the first person to speak with Aurel like this in... who knows how long? Possibly a lifetime? {i} More?{/i}"
Au "I feared she’d do the same with you."
MC "I don’t believe her."
MC "You’re not a monster, not to me."
MC "You saved me. You’ve helped me stay sane during all of this. And you’re trying to help me leave."
MC "You’re a good man, Aurel. Don’t let anyone tell you otherwise."
Au "Thank you, {i}truly{/i}."
Au "I’ve more than prepared for the reality that I’ll always be here."
Au "I can indulge myself until the sun blacks out."
Au "But... Micah and Lark deserve to experience the outside world. They were so young when I turned them."
MC "You made them vampires, too?"
"He bows his head in shame."
Au "Another foolish attempt to protect them."
"He sighs deeply."
Au "I’d lived a full life before I became a vampire."
Au "I had a career, a home to call my own, a man I loved more than anything."
Au "I don’t believe Micah or Lark ever got that chance, and I hate myself more everytime I think about that."
MC "You didn’t know, Aurel. And I’m sure you  {i}did{/i} protect them, but things have changed."
MC "We can still change things, remember?"
Au "I want to believe that, but I fear I’m just getting your hopes up."
Au "I fear... that all my nightmares will come true."
Au "Before you came, I was stuck in a perpetual motion, a state of being without living, and endless, soulless merry go round."
Au "I had no goals, no wishes, no dreams. Only now do I realize how truly undead I’ve become."
Au "Even with all the lights, festivities, and grandeur of a circus- I still felt empty. But the show must go on, as they say."
Au "The truth is, I haven’t written a critique in at least 20 years. I’d lost interest and become completely numb to all of it."
"He confirms your fears, he’d been truly alone. Even when standing at the center of a bustling circus, he was disconnected from it all."
"You knew the feeling. Even when you knew what it was, you couldn’t escape it."
"Aurel’s eyes meet yours, and you still under his gaze."
Au "That was until I found you."
Au "In that mirror maze, it was as if my old self came flooding back into me."
Au "I had a goal, finally. To get you out of here."
Au "I have this dream, of discovering the world outside with the others."
Au "But Isadora- for some ungodly reason, she won’t even try to work with me, she won’t let me atone for my sins. She keeps us trapped here, by merely standing by."
Au "Perhaps I myself am being uncharitable, but I believe her to be at the root of this, and I want to put it to an end."
MC "I want to help you."
MC "The world isn’t perfect, it never was, and it never will be-- but, it’s better than here."
MC "I want you all to see that world. I want to show you."
Au "[MC_name], please stop me if I say too much."
"You simply nod, you’ll listen to anything he wants to tell you."
Au "It may seem wrong to say, but Isadora wasn’t entirely incorrect."
MC "What do you mean?"
Au "I am... fond of you. Not in the way you’re fond of Andy, but... how I was once fond of Cedric."
Au "You remind me of a happier time. You fill me with the enjoyment of a masterful winding tale."
Au "I want to learn everything there is about you. I want to explore you."
Au "Are my feelings just my own?"
"You can only shake your head. Your words catch in your throat."
"He watches you, waiting for you to respond."
MC "Aurel I- I like you too, b-but…"
Au "If you’re worried, don’t be. This doesn’t change anything."
Au "It’s wonderful to have you here for the time, but this isn’t where you should be."
Au "No matter my feelings, your return home remains my top priority."
MC "Aurel."
"His eyes trail from your eyes to your lips. You bite them in response."
Personality Choice #5
# Kiss Him](Personality choice no points)
"You don’t miss your chance to collide your lips with his."
"It starts stiff, letting the shock of it run through you both, before you soften against him."
"A tingle runs up your spine as you grip his face, properly kissing him."
"It’s clumsy. It’s been awhile since you’ve been kissed, and you suspect it’s been even longer since he has."
"Even so, it’s wonderful. You forget about everything that isn’t him."
"Your conjoined lips work away at one another’s, discovering the taste, the feeling, making this sensation familiar."
"You keep being distracted by the reality that you’re kissing Aurel, but even so, it feels so natural, as if it were always meant to be this way."
"Your head fills with stars at the tenderness with which he kisses you back. His hands hold your waist."
"He’s even gentleman enough to not run his hands along your body. You do wish he would be less gentlemanly, however."
"He pulls you against his large frame, hugging you before releasing your lips, ending the kiss."
"Even still, he holds you."
"You flutter your eyes open, falling back down to reality. You’re met with Aurel’s handsome face smiling down at you, he’s flushed, and his eyes are ever so slightly glazed."
Au "That was wonderful."
Au "I’d wanted to kiss you, but it felt like asking for too much."
"You smile at him, enjoying being in his embrace, happily having all his attention."
Au "Would it be too much to ask to kiss you again?"
# Let Him Kiss You](Personality choice no points)
"You shut your eyes as Aurel leans into you, and you only have a moment to prepare yourself for his kiss."
"It starts stiff, the shock of it running through you both, before you soften against him."
"A tingle runs up your spine as he grips your face, properly kissing you."
"It’s clumsy. It’s been awhile since you’ve been kissed, and you suspect it’s been even longer since he has."
"Even so, it’s wonderful. You forget about everything that isn’t him."
"Your conjoined lips work away at one another’s, discovering the taste, the sensation; making this feel familiar."
"You keep being distracted by the reality that you’re kissing Aurel, but even so, it feels so naturaL as if it were always meant to be this way."
"Your head fills with stars at the tenderness with which he kisses you back. His hands hold your waist."
"He’s even gentleman enough to not run his hands along your body. You do wish he would be less gentlemanly, however."
"He pulls you against his large frame, hugging you before releasing your lips and ending the kiss."
"Even still, he holds you."
"Your eyes flutter open, falling back down to reality. You’re met with Aurel’s handsome face smiling down at you He’s flushed, and his eyes are ever so slightly glazed."
Au "That was wonderful."
Au "I’d wanted to kiss you, but it felt like asking for too much."
"You smile at him, enjoying being in his embrace, happily having all his attention."
Au "Would it be too much to ask to kiss you again?"
#converge
Part 3
"You smile, closing your eyes, waiting for him to kiss you yet again."
"Except this time reality came crashing in."
I "See! I knew it!"
"When you open your eyes you see Isadora with Micah and Lark in tow, as they all stare at you in horror. You’ve been caught red handed."
I "I told you he was trying to seduce [MC_name]!"
I "You’re only out for yourself, it’s as I always suspected!"
#Bad End] (If Good End Points Not high enough it goes straight into the bad end here)
Bad End
MC "That’s enough!"
"Your words lash out like a whip."
"The room falls silent."
MC "Why were you in the hall of mirrors, Isadora? Why did I see you there before I got trapped?"
"You don’t let her answer."
MC "Why is it you don’t want to leave this place?"
MC "Why do you keep Aurel from Lark and Micah?"
MC "Just what are {i}you{/i} hiding?"
I "How dare you accuse me!"
MC "{i}You’re{/i} why we’re trapped here."
MC "The pact said that three must desire to leave Festum Astrosum."
M  "That’s what the pact says?"
MC "It does. I’m guessing Isadora never told you that. How convenient."
MC "Aurel has only worked with me to find a way for all of us to escape--"
I "You can’t leave."
MC "Why? Because it’s impossible, or because you don’t want us to?"
I "No, it’s a {i}fact{/i}. I’m not trying to keep anyone here. They can leave if they so choose."
M "But we don’t want to leave."
"Micah's rebuttal throws a wrench in your momentum and jams it. Panic takes it’s place."
M "It’s unfair for you to accuse Isadora of all this, [MC_name]."
MC "Micah, she’s {i}lying{/i}."
L "Is she?"
L "Weren’t you just getting cuddled up with Aurel?"
M "Isadora tried to tell us that he was only thinking of himself, and I didn’t want to believe it, but-"
A: "It makes no difference, we're speaking the truth."
"You can’t even feel comforted by Aurel’s defense. It’s clear-"
"They don’t believe a word of what you have to say."
"Tears burn in your eyes, your heart clenches, and you claw for a way out of this hole you’ve dug for yourself."
MC "I need to leave here, you have to help me!"
"Your calls continually fall on deaf ears."
MC "Please, I’m {i}desperate{/i}!"
L "Clearly."
"Whatever chance you had to leave this place is squashed in that instant."
"As if Isadora can read your thoughts,she forces back her grin."
"She takes your hands again. The cold of her grip goes straight to your bones, as if it had never left."
"You shut your eyes, unable to pull away, to resist.."
"You’re overcome with despair. The fact you’ll be here forever is a thought you can’t escape… you’ll remain here just as Aurel has."
"You were a fool to think you could fight that fact."
"Isadora won."
I "I think they need some water-- Micah, would you be a dear?"
"Micah does as she says, like some sort of robot. He doesn’t even speak."
"Aurel isn’t even saying anything anymore, either."
"When you look for him, he avoids your eyes."
"Lark continues to stare at you and Isadora. Watching, you can’t read his expression. It’s almost easier to look at Isadora."
"You’re drained, you can’t fight-- You’ve been fighting from the moment you got stuck in that godforsaken mirror maze."
"You give up. It’s simply easier to swim down than it is to attempt to reach the surface."
"Home feels so far away now, a galaxy away."
"You suppose it’s time to make this house a home."
"Shaking, you hug Isadora."
"She’s stills, but returns it with careful, deliberate strokes to the back of your head."
"You always remembered hugs as warm comforting things, but this is far from that."
"It’s like hugging a corpse in a meat freezer."
"It’s then she whispers, when she’s got you well in her grasp, nearly constricting."
"Just not enough to kill."
I "Don’t think about ever doing {i}that{/i} again."
"And this time, you listen."
Bad Ending
#Good End] (If Good End Points are high enough it goes straight to the good end from here)
Good End
Au "That’s enough!"
"You stop Aurel with your hand."
"He looks down at you, confused."
MC "Let her speak."
"Isadora's eyes widen, she looks around as if the answer to your actions will be written on the dressing room walls."
"Under the spotlight you provide her, she fumbles."
I "I-I’ve already told you all, so many times. Aurel is no good!"
MC "How so?"
I "He’s trying to seduce you!"
I "Turn you against {i}us{/i}."
MC "Aurel has done no such thing. He’s never spoken ill of Lark or Micah, not once."
I "But he {i}has{/i} of me."
MC "Only of your actions-- like how you want to keep everyone here. Despite the pact stating that three who want to leave, can leave Festum Astrosum."
"Lark and Micah exchange a look."
MC "You didn’t tell them?"
MC "You didn’t even let {i}Aurel{/i} tell them?"
MC "He kept you here to protect you."
"You say to Micah and Lark, the two watching you speak. You do everything in your power to get the sentiment across."
MC "What do you stand to lose, Isadora, if we all leave? What harm does it do?"
I "It’s dangerous."
MC "It isn’t. If it were, you wouldn’t let the outside here into the circus to begin with."
I "I-"
"Before she can scrape together another lie, the unthinkable happens."
L "Enough, Isadora."
I "Excuse me?!"
"All the composure she originally had drops. "
I "{i}No{/i}-- not you!"
I "You’re {i}my{/i} pet!"
"Isadora reaches a claiming hand for Lark's face, moving with such speed and confidence that she stumbles slightly when it doesn't make contact."
"Lark steps away, out of her grasp, and narrows his eyes."
L "It’s more than time that we leave this place."
L "If you know how, tell us."
M  "Please. I want to see what’s on the outside."
I "No!"
"The two only watch her in silence. Something resembling fear takes over them."
I "No, no, no, {b}no!{/b}"
"Before she can do anything else, you reach for Aurel’s hand, dragging him behind you. As you pass, you usher Lark and Micah to follow. Aurel looks to you in shock."
Au "Where are we going?"
MC "We’re leaving, all of us."
# Carnival Entrance/Exit 
"Lark and Micah follow behind, but so does Isadora."
I "Stop! You can’t! It’s a waste of time!"
MC "Don’t listen to her, I want to see for myself."
I "Please! Listen to me! Lark!"
I "Micah!"
I " [MC_name]!"
MC "She can come with us."
MC "I’m not listening to her lies anymore, and neither should any of you."
"You reach the entrance and a hand grips your wrist, her nails digging into your skin."
I "Listen! I’ll make you a deal!"
MC "Let go of me, Isadora."
I "Don’t leave, and I’ll tell you- I’ll tell you all!"
"That stops you."
Au "Tell us... what?"
I "I’ll tell you, you just have to promise you won’t leave."
"As Aurel closes his eyes, preparing, a thought occurs to you, and a fear seizes you."
"He can’t-"
Au "If you tell us the truth, I’ll stay behind."
"Your fear is confirmed."
MC "Aurel, no!"
Au "Only three need to leave. I’ll stay here. As she says."
Au "Does that work, Isadora?"
"It seems the beggar has become the chooser as she sneers at the idea."
I "Instead of you, Lark-- He stays."
"Lark looks ill; he closes his eyes, gritting his teeth, fists clenched."
"Even so, he answers."
L "Of course…"
"She smiles unsettlingly."
I "I did trap [MC_name] here. I feed off of the psyche. I only need one person to keep me alive."
I "I can’t help that I am this way. I’m sorry I didn’t tell you all before."
"It twists your stomach."
"She’s truly sick."
MC "You should be sorry."
"Isadora’s eyes go wide, but you don’t give her time to say another word before you reach for all the men as you step over the entrance, you feel a- pop as if you stepped outside of a bubble." 
"You all fall to the ground, looking at the circus from the outside, you turn your head and see the parking lot, the street just behind it, the morning sun peeking over the trees."
"You’re free."
I "{i}{b}NOOOOOOOOOOOOOOOO!{/i}{/b}"
"Turning your attention toward the source of the wailing, you watch as Isadora disintegrates right before your eyes, falling to ashes where she once stood."
M  "!!"
Lark: "!!"
Au "!!"
"There’s a long silence, taking in all that had just happened over the course of mere minutes."
"The first sound you hear is the wonderful sound of Aurel’s voice."
"It slows your pounding heart."
Au "[MC_name]..."
Au "We’ve escaped…"
"Lark puts up a hand to stop him."
L "Let me check first."
Au "Lark, don’t--!"
"Before the words even leave his mouth, Lark is already inside the carnival entrance again."
"He stands studying what remains of Isadora before poking the dusty pile with the tip of his shoe." 
"He turns to you all and as easily as blinking, crosses the entrance."
"Aurel clutches his chest and breathes a sigh of relief."
"Micah joins him pacing over the entrance a couple times before it settles in."
Au "It’s over, it’s truly over…"
Au "I can’t believe it…"
"You stand up, offering your hand to help him up."
"He smiles as he takes his place by your side."
Au "I don’t know how you did it."
MC "I think you all could have done this a while ago, but you believed you couldn’t."
Au "We made our own cage?"
"He seems almost amused by that."
Au "How dreadfully ironic…"
MC "No, you were trapped. What she said, it just didn’t add up."
MC "I sensed that Lark and Micah wanted to try to leave, so it was now or never."
MC "I didn’t know she was feeding off of all of you, or that she’d die."
L "It’s not your fault. She could have released us at any time. She brought this onto herself."
"You nod."
M  "Aurel, Lark, you would’ve been stuck here, just so [MC_name] and I could leave?"
"Aurel turns to Micah, wearing a soft expression."
Au "Of course."
"Lark shrugs."
L "I thought there was no other way."
M  "Thank you, that was really brave of you guys. And you [MC_Name]."
MC "I’m sorry to have pulled you all out, but I couldn’t risk one of you being stuck behind for her to feed off of ."
Au "Don’t apologize, your quick thinking saved the day."
Au "Isadora feeding off all of us though, that is truly putrid."
MC "I need to leave this place."
MC "I know you all don’t know what to do, but we’ll figure it out. You can stay with me for now."
MC "The world is scary, but it’s better than it was. And I think, with time, it’ll be better than it is."
"Micah and Lark looked a bit unsure, but they seem to warm up to the idea."
Au "It’s good you invited us; we are vampires, afterall."
"You chuckle, leading the group away from their once permanent home. With every step you feel better."
"Even if you have to walk all the way home, it’s still better than walking those carnival grounds, like an endless merry go round."
A: "[MC_name]? Is that you?"
"You know that voice, your heart leaps."
MC "Andy!"
MC "What are you doing here?"
A: "I came here looking for {i}you{/i}. I lost you, and I had to go home. I said I’d come back and look for you in the morning-- where the hell have you been?!"
MC "It’s... a long story."
"Andy looks past you, to the boys."
A: "You brought these guys with you? What’s going on?"
MC "This... really isn’t the place to talk about all this."
A: "...Okay?"
MC "But I will tell you, I just want to get home and take a shower first."
MC "I’m sorry for worrying you."
A: "It’s okay, just don’t do that again."
MC "I won’t."
Au "Nice to see you again, Andy."
A: "And you… Aurel, was it?"
"Aurel nods, smiling."
A: "Well, hello again [MC_name], and Mc’s friend Aurel."
MC "I think we may be more than friends."
A: "!!"
"Aurel grins, grabbing your hand. You can feel the excitement resonating between you both."
"You don’t know what was to come, but you couldn’t wait to find out."
Epilogue
"One Year Later"

"The microwave beeps as you set the facemasks on the coffee table, lighting the candles."

MC "Babe! Are you out of the shower?"

Au "I am; here."


"He hands you a bowl filled with popcorn."

MC "Were you watching the microwave again?"

Au "I can’t wrap my head around how it works, and so quickly!"

"You go to place the bowl onto the coffee table as well."

MC "Honestly I don’t understand how it works either."

Au "You can look it up, can’t you?"

"You nod."

MC "I’ll send you the wiki link, but I’m not reading it all tonight. I’ve been waiting all day to watch the season finale with you."

Au "Yes, of course, I’m simply curious."

"So you do, you look up how the miracle of microwavable popcorn is even possible."

Au "Heat forms steam inside the kernel! That makes sense…"

Au "Ah! Fascinating...."

Au "Thank you, [MC_Name] for indulging me."

MC "Of course, my love."

"You say mimicking his speech before puckering your lips."

"He kisses you before pulling you onto the couch."

MC "So who do you think is going to win? Luscious Vivica or Bach’d Macon Chic?"

Au "Luscious Vivica, if the judges have {i}any{/i} taste."

MC "You’re kidding? Bach is hilarious!"

Au "Do you want to make a wager?"

"You eye him playfully."

MC "Wager?"

Au "Yes, if Vivica wins you have to do what I say. If Bach wins, I have to do what you say."

"He’s got a {i}vampish{/i} look in his eyes."

MC "Alright, I hope you enjoy doing the dishes when Bach wins."

Au "Oh, you’ll love what's in store if Vivica wins."

MC "What are you going to have me do?"

"He leans back into the couch, closing his eyes."

Au "I guess you’ll just have to wait and see."

"You squint at your boyfriend."

"Now you almost want Vivica to win, but you won’t say so."

"You lean into him, while grabbing the bowl off the table."

"The smell of citrus candles, buttery popcorn, and Aurel’s body wash fills your senses while you sink into him and the couch."

"He rests his head on yours."

#TODO: somethin to indicate a time skip

"An hour or so later."

MC "Told you she’d win!"

Au "Very well…dish duty for me then."

MC "You can do them tomorrow, it’s already pretty late."

Au "How virtuous of you."

"The two of you chuckle."

MC "Are you gonna tell me what you were going to have me do?"

Au "Hmmm…"

MC "Aurel! Tell me!"

Au "I was going to have you listen to one of my critiques."

MC "You don’t have to make a bet for that."

Au "Truthfully, I didn’t know what to wager; I just wanted to make you squirm."

"Your face flushes at that."

MC "I thought you were going to ask for a massage or something."

Au "That would have been a good idea…"

MC "Maybe you could give {i}me{/i} a massage?"

"He pokes your nose."

Au "You’re already making me do the dishes, you can’t have both."

MC "I can’t?"

"You give him your best puppy eyes."

"He sighs-- it seems to have an effect."

Au "Only if I can get one in return."

"You pretend to think."

Au "You little devil, you."

MC "I’m just joking, I swear! Don’t tickle me! I’m sorry!"

Au "Next time we make a bet, I’m going to tickle you relentlessly when I win."

"You gasp, sitting up on the couch to face him."

MC "You wouldn’t! That’s basically torture!"

Au "So is dish duty."

MC "Don’t be dramatic."

"He leans in with a smirk."

Au "You’re the one being coy."

"You can only bring yourself to kiss him, setting the now empty popcorn bowl onto the coffee table, while he ravishes you all night long."


Good Ending
























    if aurel_goodend >= 4:
        jump aurel_goodend
    else:
        jump aurel_badend
    
label aurel_goodend:
    "good end 4 aurel!"
    jump end

label aurel_badend:
    "bad end frowny face"
    jump end

