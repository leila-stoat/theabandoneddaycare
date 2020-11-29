init:
    $ right = Position(xpos=1.0, ypos=1.0, xalign=1.0, yalign= 1.0)
    $ right_off = Position(xpos=0.9, ypos=1.0, xalign=1.0, yalign= 1.0)

    $ left = Position(xpos=0.0, ypos=1.0, xalign=0.0, yalign= 1.0)
    $ left_off = Position(xpos=0.1, ypos=1.0, xalign=0.0, yalign= 1.0)

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
image mary = "draft/lucy.png"
image mary flipped = im.Flip("draft/lucy.png", horizontal=True)
define velvet = Character("Velvet")
image velvet = "draft/velvet.png"
image velvet grinning = "draft/velvet.png"

image title = "draft/title.jpg"
image breakfast = "draft/breakfast_scene.jpg"
image smooch = "draft/smooch_scene.jpg"
image schoolyard = "draft/title.jpg"

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
            jump school
        "Lucy's Room":
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

    show mary flipped at left_off
    lucas "You did what!!!???" (multiple=2)
    mary "You did what!!!???" (multiple=2)

    velvet "Chillax babies. It was a dare..."

    lucas "You knocked on the head or something? You know the rules..."

    velvet "The rules... I know the rules since your mom is a cop and annoys us with them everyday... At least she stopped asking us about our dolls..."

    stacy "Ye... Yea... Dolls... blush"

    lucas "Still, you shouldn't have done it. You know how Nowi is..."

    velvet "Don't worry they will show up."

    lucas "When?"

    velvet "Tonight."

    stacy "You aren't..."

    velvet "Oh yea I am! Tonight the both of you will meet me at midnight at the Abraham Woods!"

    lucas "You are crazy Velvet I am not going there!"

    velvet "What's wrong? Baby had an accident?"

    #[Cutscene Velvet checks Lucas pants]

    return
