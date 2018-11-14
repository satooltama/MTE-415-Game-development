
define e=Character("Eileen")
define l=Character("Lucy")

label start:

    #scene #scenefile

    #show #characterfile
    e "Hi I'm Eileen."

    #show #lucy at right
    l "Hi I'm Lucy."
    menu:
        "Hey Lucy you look nice today!":
            jump lucylooknice
        "Hey Lucy you suck!":
            jump lucysuck
    label lucylooknice:
        l "wow thanks!"
        return

    label lucysuck:
        l "WTF DOOD!?"
        "Lucy walk away"
        "hellow"
        "how are you"
        return


    return
