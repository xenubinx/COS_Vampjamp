label lark:
    "test"
    "test"

    menu:
        "add 5":
            $ lark_goodend += 5 #(add point)

        "add 1":
            $ lark_goodend += 1 #(add point)



    #$ micah_goodend = 0
    if lark_goodend >= 3:
        jump lark_goodend
    else:
        jump lark_badend
    
label lark_goodend:
    "good end 4 mr lark!"
    scene larkgood 
    $ persistent.unlock_Lark = True
    jump end

label lark_badend:
    "bad end frowny face"
    jump end

label end:  
    return