import random

words = ['pakistan', 'iran', 'china', 'dubai', 'london']

def choose_word():
    return random.choice(words)

def display(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_ '
    return display_word

def play_game():
    word = choose_word() #python
    guessed_letters = []
    wrong_guesses = 0
    max_tries = 6

    while wrong_guesses < max_tries:
        print(f"Word: {display(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_tries - wrong_guesses} tries left.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break

    if wrong_guesses == max_tries:
        print(f"Sorry, you lost! The word was: {word}")
if __name__ == '__main__':
  play_game()
