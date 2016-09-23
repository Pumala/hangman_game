import getpass

def hangman_game():
    print "Welcome to the game of hangman!"
    # use getpass to hide the user's typed secret word from the screen
    phrase = getpass.getpass("Player 1: Please enter the secret word: ")
    # find the length of the phrase and store it in a variable
    letter_amt = len(phrase)
    # use letter_amt to generate how many letter positions
    lines = "_ " * (letter_amt - 1) + "_"
    # create a list => list stores blank values using "_"
    split_list = lines.split(" ")
    found_word = False
    # create a list of the phrase's letters
    # ex: phrase = "toy", stored_letters = ["t","o","y"]
    stored_letters = []
    count = 7
    i = 0
    while i < len(phrase):
        for letter in phrase:
            stored_letters.append(phrase[i])
            i += 1
    print stored_letters

    while count > 0 and not found_word:
        print "Player 2: You have %d guesses left." % count
        # Show Player 2 a visual of the word that is left to guess
        # ex: phrase = "school", split_list = ["_","c","_","o","o","_"]
        print split_list
        input = raw_input("Player 2: Choose a letter or guess the phrase: ")
        if input == phrase:
            print "Nice! You guessed the secret word: %s." % phrase
            found_word = True
        else:
            index = 0
            found_letter = False
            for letter in stored_letters:
                if input == letter:
                    split_list[index] = letter
                    found_letter = True
                    formed_word = "".join(split_list)
                    if formed_word == phrase:
                        print "Nice! You guessed the secret word: %s." % phrase
                        found_word = True
                index += 1
            if not found_letter:
                count -= 1
                if count == 0:
                    print "You ran out of guesses!"
                    print "The secret word was %s." % phrase

hangman_game()
