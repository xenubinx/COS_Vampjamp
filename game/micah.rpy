label micah:
    "test"
    "test"

    menu:
        "add 5":
            $ micah_goodend += 5 #(add point)

        "add 1":
            $ micah_goodend += 1 #(add point)



    #$ micah_goodend = 0
    if micah_goodend >= 2:
        jump micah_goodend
    else:
        jump micah_badend
    
label micah_goodend:
    "good end 4 mr mics!"
    jump end

label micah_badend:
    "bad end frowny face"
    jump end

## quick fix. had to comment it out bc it was causing game to crash.
# label end:  
    # return