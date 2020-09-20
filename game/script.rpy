
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

image title = "draft/title.jpg"
image breakfast = "draft/breakfast_scene.jpg"
image smooch = "draft/smooch_scene.jpg"

image blackout = "#000"
image whiteout = "#fff"

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
    news """That's just in. New information on the missing of Nowi Green and Laura Lukond has emerged.

    Some locals stated that they have seen the two girls heading towards the Abraham Woods. The police has yet to confirm if that's true or not.

    If that is the case, that would mark person 46 and 47 that went missing in the Abraham Woods in the last 30 years. We will keep you updated as soon as new details appear.

    I have been Barbara Simmons for Channel 4 News."""

    scene black
    with fade

    show lucas at left
    lucas "No way! That's why they weren't at school!"

    show mom at right
    mom "It looks like it the chief just texted me the details... Finish your breakfast young man!"

    scene breakfast
    with fade

    show lucas at left
    lucas "So, what are the details?"

    show mom at right
    mom "Apparently some locals saw them heading inside the Abraham Woods around 1AM. Poor girls, they knew that the Woods are a restricted area, couldn't they just stay at home and play with their dolls?"

    lucas "They aren't little girls like Lucy mom..."

    show lucy at center
    lucy "I love my dollies!"
    hide lucy

    lucas "But still, there must be something that connects all those missing persons. Let me think what is up there in the Abraham Woods beside trees... The Abandoned Daycare!"

    mom "Great job sweety! My little baby is gonna be a detective when we grows up!"

    lucas "I'm 21 mom... Have you investigated the daycare?"

    mom "We did it several time now, and always nothing..."

    lucas "Tried doing in during the night?"

    mom "We wanted to but the mayor gave us the red light every single time, its restricted for everyone."

    lucas "Why is that I wonder..."

    mom "I don't know sweety, the only thing I know is I have the night shift today and I have to drop and pick Lucy from her daycare, you are gonna be alone today. Don't do anything silly young man!"

    show lucy at center
    lucy "Mommy, I'm ready!"

    mom "Alright honey! See you Later sweety!"

    scene smooch
    with fade

    "..."

    return
