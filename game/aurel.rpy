label aurel:
    "test"
    "test"

    #menu:
        #"add 5":
            #$ aurel_goodend += 5 #(add point)

        #"add 1":
            #$ aurel_goodend += 1 #(add point)



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

