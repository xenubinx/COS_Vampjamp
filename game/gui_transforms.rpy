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
        alpha 0.0 yoffset -200
        ease 1.5 yoffset 0 alpha 1.0
    on hide:
        ease 1.0 yoffset -200 alpha 0.0

## Menu screen

transform gmOverlay0:
    on show:
        alpha 0.0
        ease .5 alpha 1.0
    on hide:
        ease 1.0 alpha 0.0

transform gmOverlay1:
    on show:
        alpha 0.0 yoffset -50
        ease .5 yoffset 40 alpha 1.0
        ease .5 yoffset 0
    on hide:
        ease 1.0 yoffset -100 alpha 0.0

transform gmOverlay2:
    on show:
        alpha 0.0 yoffset -200
        pause .5
        ease 1.0 yoffset 40 alpha 1.0
        ease .5 yoffset 0 alpha 1.0
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
        alpha 0.0 yoffset -200
        pause 2.5
        ease 1.0 yoffset 40 alpha 1.0
        ease .5 yoffset 0 alpha 1.0
    on hide:
        ease 1.0 yoffset -200 alpha 0.0

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
        ease 0.25 yoffset 10
        ease 0.25 yoffset -10
        repeat

    parallel:
        pause 3
        xoffset 0
        linear 20 xoffset 5200
        repeat

transform walkLeft:

    parallel:
        ease 0.25 yoffset 10
        ease 0.25 yoffset -10
        repeat

    parallel:
        pause 3
        xoffset 0
        linear 20 xoffset -5200
        repeat

transform swinging:
    parallel:
        ease 2 rotate -.5 xanchor 0.5 yanchor 0.5
        ease 2 rotate .95 xanchor 0.5 yanchor 0.5
        repeat 
    parallel:
        align(0.5,0.2)