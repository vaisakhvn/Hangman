import random

# List of words for the game
words = ["apple", "banana", "cherry", "grape", "kiwi", "orange", "pear", "strawberry", "watermelon",
         "cat", "dog", "elephant", "giraffe", "lion", "tiger", "zebra", "frog", "turtle", "snake",
         "car", "bicycle", "bus", "motorcycle", "train", "truck", "boat", "airplane", "helicopter",
         "computer", "keyboard", "monitor", "mouse", "printer", "laptop", "phone", "tablet", "camera",
         "book", "pen", "pencil", "notebook", "dictionary", "magazine", "newspaper", "guitar", "piano",
         "violin", "drums", "trumpet", "flute", "saxophone", "basketball", "football", "soccer", "tennis",
         "volleyball", "baseball", "swimming", "hiking", "cycling", "dancing", "singing", "painting", "cooking",
         "sun", "moon", "star", "planet", "galaxy", "universe", "mountain", "ocean", "river", "lake",
         "forest", "desert", "island", "city", "village", "farm", "house", "apartment", "castle", "cave",
         "flower", "tree", "grass", "cloud", "rain", "snow", "wind", "thunder", "lightning", "fire",
         "ice", "earth", "air", "water", "rock", "sand", "gold", "silver", "diamond", "emerald",
         "ruby", "sapphire", "topaz", "amethyst", "quartz", "red", "blue", "green", "yellow", "orange",
         "purple", "pink", "brown", "gray", "black", "white", "happy", "sad", "angry", "surprised",
         "excited", "bored", "tired", "hungry", "thirsty", "zeppelin", "carousel", "jazz", "whisper", "xylophone",
         "cucumber", "puzzle", "kangaroo", "acoustic", "aluminum", "mosquito", "octopus", "helmet", "goggles",
         "penguin",
         "volcano", "astronaut", "telescope", "monument", "wristwatch", "umbrella", "tornado", "dragon", "sunflower",
         "seashell", "ocean", "mountain", "river", "forest", "desert", "island", "city", "village", "farm", "house",
         "apartment", "castle", "cave", "flower", "tree", "grass", "cloud", "rain", "snow", "wind",
         "thunder", "lightning", "fire", "ice", "earth", "air", "water", "rock", "sand", "gold",
         "silver", "diamond", "emerald", "ruby", "sapphire", "topaz", "amethyst", "quartz", "red", "blue",
         "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white", "happy",
         "sad", "angry", "surprised", "excited", "bored", "tired", "hungry", "thirsty", "zeppelin", "carousel",
         "jazz", "whisper", "xylophone", "cucumber", "puzzle", "kangaroo", "acoustic", "aluminum", "mosquito",
         "octopus",
         "helmet", "goggles", "penguin", "volcano", "astronaut", "telescope", "monument", "wristwatch", "umbrella",
         "tornado", "dragon", "sunflower", "seashell", "butterfly", "elephant", "panda", "dolphin", "otter",
         "parrot", "rhinoceros", "iguana", "chameleon", "peacock", "platypus", "jaguar", "hedgehog", "beaver",
         "lemur", "cockatoo", "meerkat", "okapi", "anteater", "armadillo", "chimpanzee", "tapir", "aardvark", "gazelle"]


def choose_word():
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            break

    if "_" in display_word(word_to_guess, guessed_letters):
        print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")


if __name__ == "__main__":
    hangman()
