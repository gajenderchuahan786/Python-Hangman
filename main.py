import random

def hangman():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    word_display = ["_" for _ in word]

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in word_display:
        print("\nWord: " + " ".join(word_display))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_display[index] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

    if "_" not in word_display:
        print("\nCongratulations! You've guessed the word: " + word)
    else:
        print("\nSorry, you've run out of attempts. The word was: " + word)

if __name__ == "__main__":
    hangman()
