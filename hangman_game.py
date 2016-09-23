import getpass

def hangman_game():
    print "Welcome to the game of hangman!"
    phrase = getpass.getpass("Player 1: Please enter the secret word: ")
    letter_amt = len(phrase)
    lines = "_ " * (letter_amt - 1) + "_"
    split_list = lines.split(" ")
    found_word = False
    stored_letters = []
    count = 7
    i = 0
    while i < len(phrase):
        for letter in phrase:
            stored_letters.append(phrase[i])
            i += 1

    while count > 0 and not found_word:
        print "Player 2: You have %d guesses left." % count
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
