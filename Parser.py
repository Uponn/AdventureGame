def parser_rooms(the_input, current_floor):
    first_word = ""
    second_word = ""

    flag1 = False
    flag2 = False

    movement_kwrds = ["go", "enter"]

    question = the_input
    input_words = question.lower().split()
    rooms = current_floor
    for word in input_words:
        if word in movement_kwrds:
            flag1 = True
            first_word = word
    for word in input_words:
        if word in rooms:
            flag2 = True
            second_word = word
    if flag1 and flag2:
        return second_word
    elif flag1 == False and flag2:
        print("Do you mean 'go' or 'enter' to the {}?".format(second_word))
    elif flag1 and flag2 == False:
        print("Do you want to %s to some of those rooms" % first_word, format(current_floor) + "?")


def parser_furniture(the_input, furniture):
    first_word = ""
    second_word = ""
    flag1 = False
    flag2 = False

    action_kwrd = ["go", "check", "inspect"]

    question = the_input
    input_words = question.lower().split()

    for word in input_words:
        if word in action_kwrd:
            flag1 = True
            first_word = word
    for word in input_words:
        if word in furniture:
            flag2 = True
            second_word = word
    if flag1 and flag2:
        return second_word
    elif flag1 and flag2 == False:
        print("Do you want to '{}' to one of those furnitures".format(first_word), furniture, "?")
    elif flag1 == False and flag2:
        print("Did you mean '{}', '{}' or '{}' the".format(*action_kwrd), second_word, "?")


def parser_items(the_input, items):
    first_word = ""
    second_word = ""

    flag1 = False
    flag2 = False

    action_kwrds = ["take", "grab", "use"]

    question = the_input
    input_words = question.lower().split()

    for word in input_words:
        if word in action_kwrds:
            flag1 = True
            first_word = word
    for word in input_words:
        if word in items:
            flag2 = True
            second_word = word
    if flag1 and flag2:
        return second_word
    elif first_word and flag2 == False:
        print("Did you mean '{}' the '{}'?".format(first_word, *items))
    elif flag1 == False and flag2:
        print("Did you mean '{}' or '{}' for the".format(*action_kwrds), second_word + "?")
    else:
        return False
