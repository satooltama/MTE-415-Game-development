
define Z=Character("Zac")
define M=Character("Mint")
define W=Character("Win")

label start:

    #scene #scenefile

    " ณ โรงเรียนแห่งหนึ่ง "

    #show #characterfile
    Z "Hi I'm Eileen."

    #show #lucy at right
    M "Hi I'm Lucy."
    menu:
        "Hey Lucy you look nice today!":
            jump lucylooknice
        "Hey Lucy you suck!":
            jump lucysuck
    label lucylooknice:
        M "wow thanks!"
        return

    label lucysuck:
        M "WTF DOOD!?"
        "Lucy walk away"
        "hellow"
        "how are you"
        return


    return
