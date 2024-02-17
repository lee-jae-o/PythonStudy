import random

def load_words():
    return ["python", "java", "programming", "computer", "algorithm", "developer", "coding", "debugging", "software"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    words = load_words()
    chosen_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")

    while attempts > 0:
        display = display_word(chosen_word, guessed_letters)
        print("Current Word:", display)
        print("Attempts Left:", attempts)

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in chosen_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts -= 1
                print("Incorrect guess. Try again.")
        else:
            print("Please enter a valid single letter.")

        if set(chosen_word) <= set(guessed_letters):
            print("Congratulations! You guessed the word:", chosen_word)
            break

    if attempts == 0:
        print("Sorry, you're out of attempts. The word was:", chosen_word)

if __name__ == "__main__":
    main()