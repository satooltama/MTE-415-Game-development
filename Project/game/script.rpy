init:

    #background
    image pokeB = Image("image/bs.png")
    image streetB = Image("image/street.png")
    image whB = Image("image/wh.jpg")
    image seaB = Image("image/sea.jpg")
    image sodercampB = Image("image/mb.jpg")
    image policeB = Image("image/police.png")

    #battleBG
    image bCc = Image("battle/battleCc.png")
    image bFin = Image("battle/battleFin.png")
    image bPw = Image("battle/battlePw.png")
    image bTo = Image("battle/battleTo.png")
    image bTu = Image("battle/battleTu.png")

    #character
    image soderC = Image("character/s69.png")
    image ccC = Image("character/cc.png")
    image finC = Image("character/fin.png")
    image toC = Image("character/pto.png")
    image pwC = Image("character/pw.png")
    image prayutC = Image("character/tu.png")


define soder = Character("ทหาร69")
define cc = Character("ท่านชัชช่า")
define pw = Character("ดันตือ")
define prayut = Character("ลุงตูบ")
define fin = Character("ฟินนี่เดอะชาร์ค")
define to = Character("บังโต")

default result = "none"
default selection = "none"
default score = 0
default enemy = 0
default ties = 0

default persistent.cheating = 0


label start:



    #scene #scenefile
    scene sodercampB
    "ณ ค่ายทหาร"
    show soderC at right

    soder "เฮ้อ... เหนื่อยเป็นบ้า ดันตือสั่งซ่อมทั้งวันเลย อาบน้ำดีกว่า"

    soder "เฮ้ย! นั่นมัน.."

    show toC at left
    "บังโตปรากฏตัว"

    to "ทหาร69! เรามาเล่นเกมข่มขืนกันเถอะ"

    soder "ไม่!!"

    to "เริ่มต้นได้สวย"

    "บังโต ต้องการที่จะตุ๋ยตูดคุณ"

    label rps_label1:


        scene bTo
    # The above statement expects a file called rps (jpg or png) inside the images folder.
        show screen stats
        #show toC at right


    label rps_select1:

        if not persistent.cheating:
            menu:

                "ค้อน":
                    style menu_choice_button
                    $selection = "ค้อน"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])

        else:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = "กรรไกร"
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = "ค้อน"
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = "กระดาษ"


    label results1:

    ####rock####

        if result == "ค้อน":
            if selection == "ค้อน":
                jump win1
            elif selection == "กระดาษ":
                jump win1
            elif selection == "กรรไกร":
                jump win1

    ####paper####

        elif result == "กระดาษ":
            if selection == "ค้อน":
                jump win1
            elif selection == "กระดาษ":
                jump win1
            elif selection == "กรรไกร":
                jump win1

    ####scissors####

        elif result == "กรรไกร":
            if selection == "ค้อน":
                jump win1
            elif selection == "กระดาษ":
                jump win1
            elif selection == "กรรไกร":
                jump win1


    label win1:

        soder "[selection]ชนะ[result]อยู่แล้ว ! เจ้ามันกากเอง"
        $ score += 1
        if score == 3:
            soder "อย่ามาห้าวกับพี่!"
            jump pw_scene
        jump rps_select1





label pw_scene:
    hide screen stats
    $ result = "none"
    $ selection = "none"
    $ score = 0
    $ enemy = 0
    $ ties = 0

    hide soderC
    hide toC
    #scene #scenefile
    scene sodercampB
    "ณ ค่ายทหาร"

    show pwC at right
    "ดันตือปรากฏตัว"


    pw "เสียงดังโวยวายอะไรกัน!"

    pw "แกอีกแล้วหรอ ทหาร69! ไปวิดพื้น 100 ครั้ง!"
    show soderC at left
    soder "ไม่ !!!"
    pw "ไม่อย่างนั้นหรอ ! มึงเจอกู !!"


    label rps_label2:

        scene bPw
    # The above statement expects a file called rps (jpg or png) inside the images folder.
        show screen stats


    label rps_select2:

        if not persistent.cheating:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])

        else:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = "กรรไกร"
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = "ค้อน"
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = "กระดาษ"


    label results2:

    ####rock####

        if result == "ค้อน":
            if selection == "ค้อน":
                jump tie2
            elif selection == "กระดาษ":
                jump win2
            elif selection == "กรรไกร":
                jump lose2

    ####paper####

        elif result == "กระดาษ":
            if selection == "ค้อน":
                jump lose2
            elif selection == "กระดาษ":
                jump tie2
            elif selection == "กรรไกร":
                jump win2

    ####scissors####

        elif result == "กรรไกร":
            if selection == "ค้อน":
                jump win2
            elif selection == "กระดาษ":
                jump lose2
            elif selection == "กรรไกร":
                jump tie2

    label tie2:

        pw "เสมองั้นรึ !!"
        $ ties += 1
        jump rps_select2

    label win2:

        soder "[selection] ชนะ [result] เหอะ ไอ้อ้วนขาเบียด อย่างแกหน่ะแค่เดินก็แทบจะไม่ไหวอยู่แล้ว"
        $ score += 1
        if score == 3:
            jump tufin_scene

    label lose2:

        pw "[result]ของฉันชนะ[selection]ก็มาดิคร้าบบ!"
        $ enemy += 1
        jump rps_select2


label tufin_scene:
    hide screen stats
    $ result = "none"
    $ selection = "none"
    $ score = 0
    $ enemy = 0
    $ ties = 0
    #scene #scenefile
    scene sodercampB
    "ณ ค่ายทหารในเช้าวันต่อมา"

    show prayutC at left
    prayut "เมื่อวานใครซ้อมดันตือ !!"

    "..."

    prayut "อย่าคิดว่าข้าไม่รู้นะ ทหาร69!"

    show soderC at right
    soder "ชิบหายละ!"

    prayut "ทหาร! ลากมันไปปรับทัศนคติกับฉลาม!"

    soder "ม่ายยยยยย!"

    hide prayutC
    hide soderC

    scene seaB
    "ณ ทะเลใกล้ๆค่ายทหาร"
    show soderC at left
    soder "ทำไมเราต้องมาเจออะไรแบบนี้ด้วย"

    show finC at right
    "ฟินนี่เดอะชาร์ค ปรากฏตัว"
    fin "แฮ่~"

    label rps_label3:

        scene bFin
    # The above statement expects a file called rps (jpg or png) inside the images folder.
        show screen stats


    label rps_select3:

        if not persistent.cheating:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])

        else:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = "กรรไกร"
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = "ค้อน"
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = "กระดาษ"


    label results:

    ####rock####

        if result == "ค้อน":
            if selection == "ค้อน":
                jump tie3
            elif selection == "กระดาษ":
                jump win3
            elif selection == "กรรไกร":
                jump lose3

    ####paper####

        elif result == "กระดาษ":
            if selection == "ค้อน":
                jump lose3
            elif selection == "กระดาษ":
                jump tie3
            elif selection == "กรรไกร":
                jump win3

    ####scissors####

        elif result == "กรรไกร":
            if selection == "ค้อน":
                jump win3
            elif selection == "กระดาษ":
                jump lose3
            elif selection == "กรรไกร":
                jump tie3

    label tie3:

        fin "แฮ่~![result]"
        $ ties += 1
        jump rps_select3

    label win3:

        fin "[selection]แฮ่~![result]"
        $ score += 1
        if score == 3:
            fin "แฮ่ ๆๆๆๆ"
            jump tu_scene

    label lose3:

        fin "[result]แฮ่~![selection]"
        $ enemy += 1
        jump rps_select3



label tu_scene:
    hide screen stats
    $ result = "none"
    $ selection = "none"
    $ score = 0
    $ enemy = 0
    $ ties = 0

    hide finC
    hide soderC

    #scene #scenefile
    scene whB
    "ณ ทำเนียบรัฐบาล"

    show soderC at right
    soder "ลุงตูบ วันนี้คือวันตายของเจ้า"
    show prayutC at left
    prayut "โอหัง ! แน่จริงก็เข้ามา"

    label rps_label4:

        scene bTu
    # The above statement expects a file called rps (jpg or png) inside the images folder.
        show screen stats


    label rps_select4:

        if not persistent.cheating:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])

        else:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = "กรรไกร"
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = "ค้อน"
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = "กระดาษ"

    label results4:

    ####rock####

        if result == "ค้อน":
            if selection == "ค้อน":
                jump tie4
            elif selection == "กระดาษ":
                jump win4
            elif selection == "กรรไกร":
                jump lose4

    ####paper####

        elif result == "กระดาษ":
            if selection == "ค้อน":
                jump lose4
            elif selection == "กระดาษ":
                jump tie4
            elif selection == "กรรไกร":
                jump win4

    ####scissors####

        elif result == "กรรไกร":
            if selection == "ค้อน":
                jump win4
            elif selection == "กระดาษ":
                jump lose4
            elif selection == "กรรไกร":
                jump tie4

    label tie4:

        prayut "ออก[result]เหมือนกัน! ยังพอไปได้นะเนี่ย"
        $ ties += 1
        jump rps_select4

    label win4:

        soder "[selection] หน่ะชนะ [result] นะไอตูบ!"
        $ score += 1
        if score == 3:
            soder "[selection] หน่ะชนะ [result]แน่นอนอิอิ ม.69ก็ทำอะไรกูไม่ได้"
            "หลังจากนั้น ทหาร69 ก็ถูกปลดกระจำการ"
            jump cc_scene

    label lose4:

        soder "[result] ของข้าชนะ [selection]ของเจ้า เจ้าประเมินพลังข้าต่ำไป!"
        $ enemy += 1
        jump rps_select4



label cc_scene:
    hide screen stats
    $ result = "none"
    $ selection = "none"
    $ score = 0
    $ enemy = 0
    $ ties = 0

    hide prayutC
    hide soderC

    #scene #scenefile
    scene streetB
    "ระหว่างทหาร69 กลับบ้าน"
    show ccC
    "ท่านชัชช่าปรากฏตัว"
    show ccC at right
    cc "นายเป็นคนที่ล้ม ม.69 ได้สินะ "
    cc "อยากเจอนายมาตั้งนานแล้ว มาวัดพลังกันหน่อยสิ!"
    show soderC at left
    soder "อย่าดีกว่าท่านทำอะไรผมไม่ได้หรอก!"
    cc "เมื่อก่อนฉันเคยท้าซุปเปอร์แมนต่อย"
    cc "โดยที่ใครแพ้ให้ใส่กางเกงในไว้ข้างนอกเชียวนะ!"


    label rps_label5:

        scene bCc
    # The above statement expects a file called rps (jpg or png) inside the images folder.
        show screen stats


    label rps_select5:

        if not persistent.cheating:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = renpy.random.choice(['ค้อน', 'กระดาษ', 'กรรไกร'])

        else:
            menu:

                "ค้อน":
                    $selection = "ค้อน"
                    $result = "กรรไกร"
                "กระดาษ":
                    $selection = "กระดาษ"
                    $result = "ค้อน"
                "กรรไกร":
                    $selection = "กรรไกร"
                    $result = "กระดาษ"


    label results5:

    ####rock####

        if result == "ค้อน":
            if selection == "ค้อน":
                jump lose5
            elif selection == "กระดาษ":
                jump lose5
            elif selection == "กรรไกร":
                jump lose5

    ####paper####

        elif result == "กระดาษ":
            if selection == "ค้อน":
                jump lose5
            elif selection == "กระดาษ":
                jump lose5
            elif selection == "กรรไกร":
                jump lose5

    ####scissors####

        elif result == "กรรไกร":
            if selection == "ค้อน":
                jump lose5
            elif selection == "กระดาษ":
                jump lose5
            elif selection == "กรรไกร":
                jump lose5

    label lose5:

        cc "ไม่รู้หรอว่า [result] ชนะ [selection] ได้ หุหุ"
        $ enemy += 1
        if enemy == 5:
            soder "อะไรกันเนี่ยเป็นไปไม่ได้ ! แต่ข้ายังไหว"
            jump rps_select5
        elif enemy ==10:
            cc "ไม่มีทางหรอกน่า เจ้าหน่ะได้ตายไปแล้ว !"
            soder "ม่ายยยยยยยยยยยยย"
            jump end_scene
        jump rps_select5
label end_scene:
    hide screen stats
    $ result = "none"
    $ selection = "none"
    $ score = 0
    $ enemy = 0
    $ ties = 0
    scene policeB
    "หลังจากนั้น ทหาร69 ก็โดนจับเข้าคุก"
    "ทำให้เกมนี้จบลงโดยที่สุด ขอบคุณที่ทนเล่นมาได้ขนาดนี้"
