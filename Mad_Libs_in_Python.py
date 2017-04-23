# Created by Emmanuel Quinones for HackDrew event, stories are from redkid.net/madlibs
# Sunday, April 23, 2017


def start():
    print()
    story_pick_input = input(
        "Welcome to MadLibs in Python!\n\n"
        "Based on the story you pick, you will be asked to provide different types of words to complete it.\nYou "
        "have 5 options for a story.\nYou can pick between:\n- Prom\n- Bowling\n- Driving\n- Easter\n- Invention\n"
        "Type the name of the story you want and see how it turns out!: ")
    story_pick = story_pick_input.title()
    print()

    if story_pick == "Prom":
        print("You've selected Prom! Time to input some word choices!")
        print()
        adj1 = input("Adjective #1: ")
        adj2 = input("Adjective #2: ")
        adj3 = input("Adjective #3: ")
        noun1 = input("Noun #1: ")
        noun2 = input("Noun #2: ")
        noun3 = input("Noun #3: ")
        noun4 = input("Noun #4: ")
        noun5 = input("Noun #5: ")
        noun6 = input("Noun #6: ")
        body_part1 = input("Body Part #1: ")
        body_part2 = input("Body Part #2: ")
        past_verb = input("Past Tense Verb: ")
        plural_noun1 = input("Plural Noun #1: ")
        plural_noun2 = input("Plural Noun #2: ")
        ing_verb = input("Verb Ending in ING: ")
        print()
        print("If there's a melody you can't seem to get out of your", body_part1, "or a song running through your",
              body_part2, "then bring your feet to this year's", adj1, "prom!\nAs usual, our prom",
              "will be held in our high school",
              noun1 + ".\nA dress code will be observed.\nNo one will be admitted wearing",
              past_verb, "or torn", plural_noun1 + ". Girls must wear a", noun2, "and boys must wear a dress shirt and "
              "a", noun3 + ".\nAs always, hot", plural_noun2, "will be served, and there will be", adj2,
              "prizes and an award for the best", ing_verb, "couple.\nThe", adj3,
              "dance committee is also proud to announce that every girl who attends will receive a", noun4,
              "to pin to her", noun5 + ", and every boy will receive a complimentary", noun6 + "!")

    elif story_pick == "Bowling":
        print("You've selected Bowling! Time to input some word choices!")
        print()
        adj1 = input("Adjective #1: ")
        adj2 = input("Adjective #2: ")
        funny_noise1 = input("Funny Noise #1: ")
        funny_noise2 = input("Funny Noise #2: ")
        noun1 = input("Noun #1: ")
        noun2 = input("Noun #2: ")
        noun3 = input("Noun #3: ")
        noun4 = input("Noun #4: ")
        numb = input("Number: ")
        body_part = input("Body Part: ")
        place = input("Place: ")
        plural_noun1 = input("Plural Noun #1: ")
        plural_noun2 = input("Plural Noun #2: ")
        print()
        print("Almost every community in America now has a bowling", place, "because bowling has become very", adj1,
              "with young", plural_noun1 + ".\nMost of them become very", adj2,
              "at the game.\nThe main objective of the game is to roll a heavy bowling", noun1,
              "down the alley and knock down the", numb,
              "pins which are at the other end.\nIf you knock them down in one roll, it's called a",
              funny_noise1 + ".\nIf it takes two rolls, it's called a", funny_noise2 + ".\nMany alleys have automatic",
              noun2, "setters.\nOthers hire", plural_noun2, "who set the pins by", noun3 + ".\nThe most important thing"
              " to remember when bowling is to make sure you have a good grip on the",
              noun4, "or you're liable to drop it on your", body_part + "!")

    elif story_pick == "Driving":
        print("You've selected Driving! Time to input some word choices!")
        print()
        adj1 = input("Adjective #1: ")
        adj2 = input("Adjective #2: ")
        adj3 = input("Adjective #3: ")
        adverb = input("Adverb: ")
        noun1 = input("Noun #1: ")
        noun2 = input("Noun #2: ")
        noun3 = input("Noun #3: ")
        noun4 = input("Noun #4: ")
        noun5 = input("Noun #5: ")
        noun6 = input("Noun #6: ")
        plural_noun = input("Plural Noun: ")
        print()
        print("Driving a car can be fun if you follow this", adj1, "advice:\nWhen approaching a", noun1,
              "on the right, always blow your", noun2 + ".\nBefore making a", adj2, "turn, always stick your", noun3,
              "out of the window.\nEvery 2,000 miles, have your", noun4, "inspected and your", noun5,
              "checked.\nWhen approaching a school, watch out for", adj3, plural_noun + ".\nAbove all, drive",
              adverb + ".\nThe", noun6, "you save may be your own!")

    elif story_pick == "Easter":
        print("You've selected Easter! Time to input some word choices!")
        print()
        numb = input("Number: ")
        game = input("Type of Game: ")
        adj1 = input("Adjective #1: ")
        adj2 = input("Adjective #2: ")
        adj3 = input("Adjective #3: ")
        adj4 = input("Adjective #4: ")
        adj5 = input("Adjective #5: ")
        noun1 = input("Noun #1: ")
        noun2 = input("Noun #2: ")
        plural_noun1 = input("Plural Noun #1: ")
        plural_noun2 = input("Plural Noun #2: ")
        liquid1 = input("Type of Liquid #1: ")
        liquid2 = input("Type of Liquid #2: ")
        print()
        print("Spring vacation usually falls around Easter time. The schools are closed and all the", plural_noun1,
              "get",
              numb, "weeks off.\nThe", adj1, "teachers also get a vacation.\nSome kids loaf around and watch the",
              noun1 + ".\nOthers get outside and play",
              game + ", while more ambitious students spend their time studying their", adj2,
              "books so they will grow up to become", plural_noun2 + ".\nLittle kids also color", adj3,
              "eggs.\nHere's how you color an egg:\nFirst, mix a package of", adj4, "dye in the bowl full of",
              liquid1 + ".\nThen, dip a", noun2, "in the bowl and rinse it off with",
              liquid2 + '.\nThen, after it dries, you can paint it with a brush. Then you show it to your friends, '
              'who will say, "Boy, what a ', adj5, 'egg!"')

    elif story_pick == "Invention":
        print("You've selected Invention! Time to input some word choices!")
        print()
        adj1 = input("Adjective #1: ")
        adj2 = input("Adjective #2: ")
        adj3 = input("Adjective #3: ")
        adverb = input("Adverb: ")
        exclamation = input("Exclamation: ")
        fam_person1 = input("Famous Male Person #1: ")
        fam_person2 = input("Famous Male Person #2: ")
        noun1 = input("Noun #1: ")
        noun2 = input("Noun #2: ")
        noun3 = input("Noun #3: ")
        noun4 = input("Noun #4: ")
        noun5 = input("Noun #5: ")
        numb = input("Number: ")
        plural_noun1 = input("Plural Noun #1: ")
        plural_noun2 = input("Plural Noun #2: ")
        food = input("Plural Type of Food: ")
        liquid = input("Type of Liquid: ")
        print()
        print("The fist electric", noun1, "was invented in 1904 by a", adj1, "young man named",
              fam_person1 + ".\nHe and his brother", fam_person2, "ran a small", noun2,
              "repair shop, and in their spare time they studied",
              plural_noun1 + '.\nWhen they started to work on their invention, everyone said, "' + exclamation + "! You"
              + "'" + 'll never get it off the',
              noun3 + '."\nBut they built a', adj2, "model out of old", plural_noun2, "and a used",
              noun4 + ".\nThe model worked fine, and in ten minutes it toasted 24 slices of",
              food + ".\nIt also used up two gallons of", liquid, "an hour, and the top converted into a",
              noun5 + ".\nThey sold the patent to a", adj3, "millionaire for", numb, "dollars and lived", adverb,
              "ever after.")

    else:
        print("That's not one of the options!")

repeat = "y"

while repeat == "y":
    start()
    print()
    repeat_input = input("Would you like to do another?(y = yes, n = no, anything else will cause the program to end): "
                         "")
    repeat = repeat_input

if repeat == "n":
    print()
    print("Thanks for playing!")
