### hep


## Defining all sprites here to save my mind

###########################

image isa angry:
    "images/sprites/Isadora/Isadora_Angry.png"
    zoom 0.75
image isa neutral:
    "images/sprites/Isadora/Isadora_Neutral.png"
    zoom 0.75
image isa sad:
    "images/sprites/Isadora/Isadora_Sad.png"
    zoom 0.75
image isa shocked:
    "images/sprites/Isadora/Isadora_Shocked.png"
    zoom 0.75
image isa shadow:
    "images/sprites/Isadora/Isadora_Silhouette.png"
    zoom 0.75
image isa smiling:
    "images/sprites/Isadora/Isadora_Smiling.png"
    zoom 0.75
image isa smirk:
    "images/sprites/Isadora/Isadora_Smirk.png"
    zoom 0.75
image isa mask:
    "images/sprites/Isadora/Isadora_Masked.png"
    zoom 0.75
###########################

image lark annoyed:
    "images/sprites/Lark/Lark_Annoyed.png"
    zoom 0.75
image lark angry:
    "images/sprites/Lark/Lark_Enraged.png"
    zoom 0.75
image lark empty:
    "images/sprites/Lark/Lark_Eyes_Empty.png"
    zoom 0.75
image lark faint smile:
    "images/sprites/Lark/Lark_Faint_Smile.png"
    zoom 0.75
image lark happy:
    "images/sprites/Lark/Lark_Grin.png"
    zoom 0.75
image lark neutral:
    "images/sprites/Lark/Lark_Neutral.png"
    zoom 0.75
image lark sad:
    "images/sprites/Lark/Lark_Sad.png"
    zoom 0.75
image lark shocked:
    "images/sprites/Lark/Lark_Shocked.png"
    zoom 0.75
image lark mask:
    "images/sprites/Lark/Lark_Masked.png"
    zoom 0.75

###########################
image aurel neutral:
    "images/sprites/Aurel/Aurel_Base_Neutral.png"
    zoom 0.75
image aurel angry:
    "images/sprites/Aurel/Aurel_Angry.png"
    zoom 0.75
image aurel empty:
    "images/sprites/Aurel/Aurel_Empty.png"
    zoom 0.75
image aurel sad:
    "images/sprites/Aurel/Aurel_Sad.png"
    zoom 0.75
image aurel shocked:
    "images/sprites/Aurel/Aurel_Shocked.png"
    zoom 0.75
image aurel happy:
    "images/sprites/Aurel/Aurel_Smiling.png"
    zoom 0.75
image aurel smirk:
    "images/sprites/Aurel/Aurel_Smirking.png"
    zoom 0.75


###########################

image micah angry:
    "images/sprites/Micah/Micah_Angry.png"
    zoom 0.75
image micah confused:
    "images/sprites/Micah/Micah_Confused.png"
    zoom 0.75
image micah empty:
    "images/sprites/Micah/Micah_Empty_Eyes.png"
    zoom 0.75
image micah neutral:
    "images/sprites/Micah/Micah_Resting_Bitch_Face.png"
    zoom 0.75
image micah sad:
    "images/sprites/Micah/Micah_Sad.png"
    zoom 0.75
image micah shocked:
    "images/sprites/Micah/Micah_Shocked.png"
    zoom 0.75
image micah smiling:
    "images/sprites/Micah/Micah_Smiling.png"
    zoom 0.75


## fuck it, defining sprite positions here too lets gooo

#if four on screen, use these positions, goes from left to right
transform foura:
    xalign -0.05
    yalign 1.0
transform fourb:
    xalign 0.25
    yalign 1.0
transform fourc:
    xalign 0.65
    yalign 1.0
transform fourd:
    xalign 1.0
    yalign 1.0


#####################
#sfx define here to make it a tiny bit easier to call for script
#####################

define audio.footsteps = "audio/sfx/CoS_SFX_01_footsteps.ogg"
define audio.card1 = "audio/sfx/CoS_SFX_02_card_01.ogg"
define audio.card2 = "audio/sfx/CoS_SFX_03_card_02.ogg"
define audio.card3 = "audio/sfx/CoS_SFX__04_card_03.ogg"
define audio.curtains = "audio/sfx/CoS_SFX_05_curtains.ogg"
define audio.navhover = "audio/sfx/CoS_SFX_06_navi_hover.ogg"
define audio.navselected = "audio/sfx/CoS_SFX_07_navi_selected.ogg"
define audio.navconfirm = "audio/sfx/CoS_SFX_08_navi_confirm.ogg"
define audio.notifpopup = "audio/sfx/CoS_SFX_09_noti_popup.ogg"
define audio.menuhover = "audio/sfx/CoS_SFX_10_menu_hover"
define audio.igselected = "audio/sfx/CoS_SFX_11_ingame_selected.ogg"
define audio.kettle = "audio/sfx/CoS_SFX_12_kettle.ogg"
define audio.whistle = "audio/sfx/CoS_SFX_13_whistle.ogg"
define audio.machinefail = "audio/sfx/CoS_SFX_14_machine_fail.ogg"
define audio.thud = "audio/sfx/CoS_SFX_15_thud.ogg"
define audio.gate = "audio/sfx/CoS_SFX_16_gate.ogg"


#####################
#music define here to make it a tiny bit easier to call for script
#####################
#all of these are loop files btw

define audio.arcade = "music/music_loop_arcard.ogg"
define audio.badend = "music/music_loop_bad_ending.ogg"
define audio.badsituation = "music/music_loop_bad_situation.ogg"
define audio.badsitquiet = "music/music_loop_bad_situation_quiet.ogg"
define audio.quiet = "music/music_loop_circus_quiet.ogg" #ehehe this is what i called Isa's theme earlier, its so good
define audio.upbeat = "music/music_loop_circus_upbeat.ogg"
define audio.goodend = "music/music_loop_good_ending.ogg"
define audio.goodmoment = "music/music_loop_good_moment.ogg"
define audio.mmtheme = "music/music_loop_main_menu_theme.ogg"
define audio.sadpiano = "music/music_loop_sad_piano.ogg"
define audio.sadderwaltz = "music/music_loop_sadder_waltz_with_harpsichord.ogg"