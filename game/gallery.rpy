## Images
image Aurel_unlocked_image = "gallery/Aurel_unlocked.png"
image Aurel_locked_image = "gallery/Aurel_locked.png"
image Aurel_CG = "gallery/Aurel_CG.png"

image Lark_unlocked_image = "gallery/Lark_unlocked.png"
image Lark_locked_image = "gallery/Lark_locked.png"
image Lark_CG = "gallery/Lark_CG.png"

image Micah_unlocked_image = "gallery/Micah_unlocked.png"
image Micah_locked_image = "gallery/Micah_locked.png"
image Micah_CG = "gallery/Micah_cg.png"

## Gallery buttons
init python:
    g = Gallery()

    g.button("CG_Aurel")
    g.condition("persistent.unlock_Aurel")
    g.image("Aurel_CG")
    g.transition = dissolve

    g.button("CG_Lark")
    g.image("Lark_CG")
    g.condition("persistent.unlock_Lark")
    g.transition = dissolve

    g.button("CG_Micah")
    g.image("Micah_CG")
    g.condition("persistent.unlock_Micah")
    g.transition = dissolve

## Gallery scree
default gallery_page = 1
define total_pages = 3

screen gallery:
    tag menu

    if gallery_page == 1:
        add g.make_button("CG_Aurel","Aurel_unlocked_image","Aurel_locked_image", xalign = 0.5, yalign = 0.4)
    
    if gallery_page == 2:
        add g.make_button("CG_Lark","Lark_unlocked_image","Lark_locked_image", xalign = 0.5, yalign = 0.4) 

    if gallery_page == 3:
        add g.make_button("CG_Micah","Micah_unlocked_image","Micah_locked_image", xalign = 0.5, yalign = 0.4)


    add "curtain1" at curtainOutLeft
    add "curtain2" at curtainOutRight
    add gui.game_menu_background_1 at gmOverlay1
    add gui.game_menu_background_7 at gmOverlay2

    frame:
        align(0.5,0.5)
        xfill True
        yfill True
        background None
        at gmOverlay4

        add gui.game_menu_background_6:
            at clockwise
            align(0.075, 0.125)
    
        add gui.game_menu_background_6:
            at counterClockwise
            align(0.925, 0.125)

    frame:
        align(0.5,0.5)
        xfill True
        yfill True
        background None
        at gmOverlay5

        add gui.game_menu_background_5:
            at walkLeft
            pos(4087, 1600)
        
        add gui.game_menu_background_5v2:
            at walkRight
            pos(-1227, 1600)

    add gui.game_menu_background_8 yoffset 200 at gmOverlay2

    frame:
        style_prefix "navigation3"
        background None
        xfill True
        at gmOverlay5
    
        if gallery_page > 1:
            textbutton _("< Prev") action SetScreenVariable("gallery_page", gallery_page - 1) align(0.1, 0.99) at mainHover
    
        textbutton _("Home") action Return() align(0.5, 0.99) at mainHover
    
        if gallery_page < total_pages:
            textbutton _("Next >") action SetScreenVariable("gallery_page", gallery_page + 1) align(0.9, 0.99) at mainHover

    frame:
        style_prefix "game_menu"
        at gmOverlay4
        background None
        xfill True
        yfill True
        
        add gui.game_menu_background_4 align(0.5,0.01)
        frame:
            background None
            align(0.5,0.0875)
                    
            if gallery_page == 1:
                label "Aurel"
            
            if gallery_page == 2:
                label "Lark"

            if gallery_page == 3:
                label "Micah"