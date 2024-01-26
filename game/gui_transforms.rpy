## Choice screen

transform choiceAnim:
    on show:
        parallel:
            alpha 0.0
            pause 0.5
            linear 0.5 alpha 1.0 
        parallel:
            yoffset 800
            linear 1.0 yoffset 0
    on hover:
        ease .25 yoffset -50
    on idle:
        ease .25 yoffset 0
transform choiceOverlay:
    on show:
        parallel:
            alpha 0.0 yoffset -200
            ease 1.0 yoffset 10 alpha 1.0 
            ease .5 yoffset 0 alpha 1.0
        parallel:
            zoom 1.05 xalign 0.5
            ease 1.5 zoom 1.0
    on hide:
        ease 1.0 yoffset -200 alpha 0.0

## Menu screen

transform mainHover:
    on hover:
        ease 0.5 yoffset -60
    on idle:
        ease 0.5 yoffset 0

transform curtainInLeft:
    on show:
        parallel:
            xoffset -500
            ease 2.0 xoffset 0

        parallel:
            alpha 0.0
            ease 1.0 alpha 1.0
    on hide:
        ease 1.0 xoffset -500 alpha 0.0

transform curtainInRight:
    on show:
        parallel:
            xoffset 500
            ease 2.0 xoffset 0

        parallel:
            alpha 0.0
            ease 1.0 alpha 1.0

    on hide:
        ease 1.0 xoffset 500 alpha 0.0

transform curtainOutLeft:
    # on show:
    parallel:
        xoffset 0
        ease 2.0 xoffset -1500

    parallel:
        alpha 0.0
        ease 1.0 alpha 1.0
    # on hide:
        # ease 1.0 xoffset 0 alpha 0.0

transform curtainOutRight:
    # on show:
    parallel:
        xoffset 0
        ease 2.0 xoffset 1500

    parallel:
        alpha 0.0
        ease 1.0 alpha 1.0

    # on hide:
        # ease 1.0 xoffset 0 alpha 0.0

transform navHover1:
    on hover:
        ease .25 xoffset 50
    on idle:
        ease .25 xoffset 0

transform navHover2:
    on hover:
        ease .25 xoffset -50
    on idle:
        ease .25 xoffset 0

transform gmOverlay0:
    on show:
        alpha 0.0
        ease .5 alpha 1.0
    on hide:
        ease 1.0 alpha 0.0

transform gmOverlay1:
    on show:
        parallel:
            alpha 0.0 yoffset -50
            ease .5 yoffset 5 alpha 1.0
            ease .5 yoffset 0
        parallel:
            zoom 1.05 xalign 0.5
            pause .25
            ease 1.5 zoom 1.0
    on hide:
        ease 1.0 yoffset -100 alpha 0.0

transform gmOverlay2:
    on show:
        parallel:
            alpha 0.0 yoffset -200
            pause .5
            ease 1.0 yoffset 5 alpha 1.0
            ease .5 yoffset 0 alpha 1.0
        parallel:
            zoom 1.05 xalign 0.5
            pause 1.25
            ease 1.5 zoom 1.0
    on hide:
        ease 1.0 yoffset -200 alpha 0.0

transform gmOverlay3:
    on show:
        alpha 0.0 yoffset -200
        pause 1.5
        ease 1.0 yoffset 20 alpha 1.0
        ease .5 yoffset 0 alpha 1.0

transform gmOverlay4:
    on show:
        alpha 0.0 yoffset -500
        pause 2.5
        ease 1.0 yoffset 10 alpha 1.0
        ease .5 yoffset 0 alpha 1.0
    on hide:
        ease 1.0 yoffset -500 alpha 0.0

transform gmOverlay5:
    on show:
        alpha 0.0 yoffset 300
        pause 2.5
        ease 1.0 yoffset -40 alpha 1.0
        ease .5 yoffset 0 alpha 1.0
    on hide:
        ease 1.0 yoffset 200 alpha 0.0

transform clockwise:

    rotate 0 xanchor 0.5 yanchor 0.5
    linear 30 rotate 360 xanchor 0.5 yanchor 0.5
    repeat

transform counterClockwise:

    rotate 0 xanchor 0.5 yanchor 0.5
    linear 30 rotate -360 xanchor 0.5 yanchor 0.5
    repeat

transform walkRight:

    parallel:
        ease 0.35 yoffset 10
        ease 0.35 yoffset -10
        repeat 9

    parallel:
        pause 1
        xoffset 0
        linear 5 xoffset 1000

transform walkLeft:

    parallel:
        ease 0.35 yoffset 10
        ease 0.35 yoffset -10
        repeat 9

    parallel:
        pause 1
        xoffset 0
        linear 5 xoffset -1000
