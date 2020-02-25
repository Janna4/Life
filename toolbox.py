def get_number(prompt):
    """Give the user a prompt and get a number from the user."""
    number = input(prompt)
    while number.isalpha():
        prompt = """***You cannot enter letters.
Enter a new number. """
        number = input(prompt)
    number = float(number)
    return number


def get_integer(prompt):
    """Gets an integer from the user."""
    myInteger = input(prompt)
    while not is_integer(myInteger):
        print("Integers only please.")
        myInteger = input(prompt)
    myInteger = int(myInteger)
    return myInteger


def is_integer(testValue):
    """Returns True if testValue is an integer and False otherwise."""
    isInteger = True
    charactersDone = 0
    currentCharacter = 0
    positiveNegative = 0
    decimal = 0

    testValueString = str(testValue)
    testValueString = testValueString.strip()
    totalCharacters = len(testValueString)

    if totalCharacters == 0:
        isInteger = False

    while charactersDone < totalCharacters:
        if testValueString[currentCharacter] not in '-+0123456789. ':
            isInteger = False
        if testValueString[currentCharacter] in ['.', ' '] and testValueString[totalCharacters - 1] not in ['.', '0',
                                                                                                            ' ']:
            isInteger = False
        if testValueString[currentCharacter] in [' ', '-', '+', '.'] and totalCharacters == 1:
            isInteger = False
        if testValueString[currentCharacter] in ['-', '+'] and currentCharacter != 0:
            isInteger = False
        if testValueString[currentCharacter] in ['-', '+']:
            positiveNegative = positiveNegative + 1
        if testValueString[currentCharacter] in ['.']:
            decimal = decimal + 1
        if positiveNegative > 1 or decimal > 1:
            isInteger = False
        currentCharacter = currentCharacter + 1
        charactersDone = charactersDone + 1
    return isInteger


def is_number(testValue):
    """Returns True if testValue is an number and False otherwise."""
    isNumber = True
    charactersDone = 0
    currentCharacter = 0
    positiveNegative = 0
    decimal = 0

    testValueString = str(testValue)
    testValueString = testValueString.strip()
    totalCharacters = len(testValueString)

    if totalCharacters == 0:
        isInteger = False

    while charactersDone < totalCharacters:
        if testValueString[currentCharacter] not in '-+0123456789. ':
            isNumber = False
        if testValueString[currentCharacter] in [' ', '-', '+', '.'] and totalCharacters == 1:
            isNumber = False
        if testValueString[currentCharacter] in ['-', '+'] and currentCharacter != 0:
            isNumber = False
        if testValueString[currentCharacter] in ['-', '+']:
            positiveNegative = positiveNegative + 1
        if testValueString[currentCharacter] in ['.']:
            decimal = decimal + 1
        if positiveNegative > 1 or decimal > 1:
            isNumber = False
        currentCharacter = currentCharacter + 1
        charactersDone = charactersDone + 1
    return isNumber


def get_positive_number(prompt):
    """returns a positive number."""
    number = get_number(prompt)
    while number < 0:
        print("You have to enter a positive value.")
        number = get_number(prompt)
    return number


def get_integer_between(low, high, prompt="Enter an integer:"):
    prompt += " (" + str(low) + "-" + str(high) + ")"
    number = get_integer(prompt)
    while (number < low) or (number > high):
        number = get_integer(prompt)
    return number


def get_boolean(prompt):
    """Returns a boolean for a yes or no question."""
    response = input(prompt)
    response = response.lower()
    if response in ['yes', 'y', 'yep', 'sure', 'of course']:
        boolean = True
    elif response in ['no', 'nope', 'n', 'absolutely not']:
        boolean = False
    else:
        prompt = "Do you mean yes? "
        boolean = get_boolean(prompt)
    return boolean


def money(cost):
    """Turn numbers into dollar amounts."""
    cost = float(cost)
    #
    # Rounds the number to the hundreths
    #
    cost = round(cost, 2)
    cost = str(cost)
    if len(cost) > 1:
        #
        # Changes the way the number is displayed based on decimal placement
        #
        if cost[-3] == ".":
            pass
        elif cost[-2] == ".":
            cost = cost + "0"
        elif cost[-1] == ".":
            cost = cost + "00"
        else:
            cost = cost + ".00"
    else:
        cost = cost + ".00"
    cost = "$" + cost
    return cost


def get_string(prompt):
    """Get and return a non-empty string"""
    if prompt[-1] != " ":
        prompt = prompt + " "
    string = input(prompt)
    while not string:
        if prompt[-31:] != " (you have to enter something) ":
            prompt = prompt + "(you have to enter something) "
        string = input(prompt)
    return string


def print_separator(character, length=60):
    """Prints length number of characters."""
    string = (character[0] * int(length))
    print(string)


def print_centered(string, length=60, character=" "):
    """Prints a string centered on a line of length length."""
    stringLength = len(string)
    padding = int((length - stringLength) / 2)
    if padding > 0:
        centeredString = character[0] * padding + string + character[0] * padding
    else:
        centeredString = string[:length]
    print(centeredString)

