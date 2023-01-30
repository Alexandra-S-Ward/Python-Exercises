def main():
    guess_limit = int(input("How many maximum guesses?"))
    guess_word = "Pineapple"
    guesses = 0
    while guesses < guess_limit:
        guess = input("What is your guess? ")
        if guess == guess_word:
            print("You guessed correctly!")
            return
        guesses +=1
        print(f"You have {guess_limit - guesses} guesses remaining.")
    print("You didn't succeed in guessing correctly.")


if __name__ == '__main__':
    main()