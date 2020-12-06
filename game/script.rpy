init:
    $ right = Position(xpos=1.0, ypos=1.0, xalign=1.0, yalign= 1.0)
    $ right_off = Position(xpos=0.85, ypos=1.0, xalign=1.0, yalign= 1.0)

    $ left = Position(xpos=0.0, ypos=1.0, xalign=0.0, yalign= 1.0)
    $ left_off = Position(xpos=0.15, ypos=1.0, xalign=0.0, yalign= 1.0)

    $ center = Position(xpos=0.5, ypos=1.0, xalign=0.5, yalign= 1.0)


define laura = Character("Laura")
define nowi = Character("Nowi")

define news = Character("Newscaster")
image news = "draft/newscaster.png"
define lucas = Character("Lucas")
image lucas = "draft/lucas.png"
define mom = Character("Linda")
image mom = "draft/mom.png"
define lucy = Character("Lucy")
image lucy = "draft/lucy.png"

define mary = Character("Mary")
image mary = "draft/mary.png"
image mary flipped = im.Flip("draft/mary.png", horizontal=True)
define velvet = Character("Velvet")
image velvet = "draft/velvet.png"
image velvet grinning = "draft/velvet.png"

image title = "draft/title.jpg"
image breakfast = "draft/breakfast_scene.jpg"
image smooch = "draft/smooch_scene.jpg"
image mom_room = "draft/breakfast_scene.jpg"
image lucy_room = "draft/breakfast_scene.jpg"
image schoolyard = "draft/title.jpg"

default underwear = "boxers"

label start:

    # scene woods

    laura "[nowi], I am not sure of this..."
    nowi "Don't be a crybaby... It's gonna be fun!"
    laura "People have vanished around these woods for over 30 years now!"
    nowi "Probably got bored of this town... Can't blame them thou... And there it is!"

    # Not sure, but it'll probably be an image?
    "[[CUTSCENE]]"
    # scene daycare

    laura "[nowi]... is this... The Abandoned Daycare!?"
    nowi "Hell yea it is! Let's go!"
    laura "No way! I am going back home!"
    nowi "Awwwww... Did the little baby gone boom boom in hear diapee?"

    # We'll use "play" here
    "<Scary Sounds, ooooh>"

    laura "Did you hear that?"
    nowi "What did you say? I can't hear you from you stinky diaper!"
    laura "I am serious! There is something out here!"
    nowi "Yes, something is there... In your diap..."

    scene black
    with fade

    "<SCREAMS>" with vpunch

    "Two days later..."

    show news at center
    news """That just in: new information on the disappearance of Nowi Green and Laura Lukond has emerged.

    Some locals stated that they have seen the two girls heading towards the Abraham Woods. The police has yet to confirm if that is true or not.

    If that is the case, that would mark persons 46 and 47 that went missing in the Abraham Woods in the last 30 years. We will keep you updated as soon as new details appear.

    I have been Barbara Simmons for Channel 4 News."""

    scene black
    with fade

    show lucas at left
    lucas "No way! That's why they weren't at school!"

    show mom at right
    mom "It looks like it the chief just texted me the details... and you finish your breakfast young man!"

    scene breakfast
    with fade

    show lucas at left
    lucas "So, what are the details?"

    show mom at right
    mom "Apparently some locals saw them heading into Abraham Woods around 1AM."
    mom "Poor girls, they knew that the Woods are a restricted area, couldn't they just have stayed at home playing with their dolls?"

    lucas "They aren't little girls like Lucy mom..."

    show lucy at center
    lucy "I love my dollies!"
    hide lucy

    lucas "But still, there must be something that connects all those missing people. Let me think, what is up there in the Abraham Woods beside trees..."
    lucas "...The Abandoned Daycare!"

    mom "Great job, sweety! My little baby is gonna be a detective when we grows up!"

    lucas "I'm 21 mom... Anyway, have you investigated the daycare?"

    mom "We did it several times now, and every time nothing turns up..."

    lucas "Ever tried doing in during the night?"

    mom "We wanted to but the mayor gave us the red light every single time. It's restricted for everyone."

    lucas "Why is that, I wonder..."

    mom "I don't know sweety, the only thing I know is that I have the night shift today and I have to drop and pick Lucy from her daycare, so you are going to be alone today. Don't do anything silly young man!"

    show lucy at center
    lucy "Mommy, I'm ready!"

    mom "Alright honey! See you Later sweety!"

    scene smooch
    with fade

    "..."

    scene black
    with fade

    show lucas at left
    lucas "Well, they are gone. Should to the same, up in my room to take my bag and off to school."

    menu:
        "Lucas' Room":
            jump school
        "Linda's (Mom's) Room":
            jump mom_room
        "Lucy's Room":
            jump lucy_room

label mom_room:
    scene mom_room
    with fade

    show lucas at left
    lucas "Strange... Mom never lets the door of her room open... Are those panties!?" #blush

    show mom at left_off
    mom "Lucas! What are you doing in my room!"

    lucas "I..." #blush

    mom "Are those my panties?"

    lucas "Wait! I can explain!"

    mom "Oh you will young man, or should I say {i}young lady{/i}! I don't have time for this, we will talk when I get home, but you will be punished now!"

    #[Cutscene of Linda putting a lingerie set on Lucas]
    "..."
    $ underwear = "lingerie"

    lucas "Mom! I can't go to school like that!" #blush

    mom "Yes you can, {i}young lady{/i}! And don't you dare take it off, I will know it! So have fun at school, dear."
    hide mom

    lucas "Great..." #blush

    jump school

label lucy_room:
    scene lucy_room
    with fade

    show lucas at left
    lucas "So... This is Lucy's new room... Old crib gone and replaced with a new bed... what's this under it? Adult diapers? Those are big enough to fit me!"

    show mom at right
    mom "They certainly do sweety."

    lucas "Mom!? What are you still doing here I tough you were gone?"

    mom "I forgot something, glad I did, since I wouldn't caught you snooping around your sisters room!"

    lucas "No mom! It's not what it looks like! I swear! "

    mom "Save it for when you get home from school young man! For now, some punishment must be applied..."

    #[Cutscene of Linda diapers Lucas]
    "..."
    $ underwear = "diapers"

    lucas "Stop it mom! I am not a baby anymore! Why do you even have those in Lucy's room?" #blush

    mom "A young lady was shoplifting them for some reason, I didn't have time to return them to the store so I took them home to return them later... guess I have a use for them after all!" #giggles

    lucas "Mom! I can't go to school like that!" #blush

    mom "Yes you can young lady! And don't you dare take them off, I will know it! So have fun at school dear."
    hide mom

    lucas "Great..." #blush
    jump school

label school:
    lucas "Off to school I guess..."

    scene schoolyard
    with fade

    show velvet at right
    velvet "Yo Lucas. What's up?"

    show lucas at left
    lucas "Hey Velvet, Mary. Heard about Laura and Nowi?"

    show mary at right_off
    mary "We did! It... it's terrible! Why would they even go there?"

    velvet "I told them to."

    lucas "You did what!!!???" (multiple=2)
    mary "You did what!!!???" (multiple=2)

    velvet "Chillax babies. It was a dare..."

    lucas "You knocked on the head or something? You know the rules..."

    velvet "The rules... I know the rules since your mom is a cop and annoys us with them everyday... At least she stopped asking us about our dolls..."

    mary "Ye... Yea... Dolls... blush"

    lucas "Still, you shouldn't have done it. You know how Nowi is..."

    velvet "Don't worry they will show up."

    lucas "When?"

    velvet "Tonight."

    mary "You aren't..."

    velvet "Oh yea I am! Tonight the both of you will meet me at midnight at the Abraham Woods!"

    lucas "You are crazy Velvet I am not going there!"

    velvet "What's wrong? Baby had an accident?"
    show velvet at left_off

    #[Cutscene Velvet checks Lucas pants]
    "..."

    if underwear == "boxers":
        lucas "Hey! What are you..." #blush

        velvet "Awwwwww... Cute pokemon boxers."

        velvet "Anyway we will see you tonight, don't you dare to bail on us or you will be sorry... Ok see ya!"

        mary "See you tonight." #blushes
    elif underwear == "lingerie":
        velvet "My, my, Lucas! Nice panties! Where did you get them from? Victoria Secrets! I bet you have matching bra and stockings as well!" #laughs

        lucas "I can explain!"

        velvet "Sure you can, sweety! Screw the daycare! Tonight we are coming over for some fun! But I must admit... your booty looks smoking in it! See you tonight, {i}sissy{/i}!" #laughs

        lucas "Great... Can it get any worse?" #blush
    elif underwear == "diapers":
        velvet "I didn't really expect you to wear diapers! Awwwwwww, so cute! No brownies in those... for now!" #laughs

        lucas "I can explain!"

        velvet "Sure you can, sweety! Screw the daycare! Tonight we are coming over for some fun! But I must admit... you look pretty cute in those! See you tonight, {i}baby{/i}!" #laughs

        lucas "Great... Can it get any worse?" #blush

    return
