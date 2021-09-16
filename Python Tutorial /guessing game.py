secret_word = "Stella"
guess = ""
guess_count= 0
guess_limit= 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        print(f"you only have {guess_limit - guess_count} left")
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("you are out of guesses, lost the game")
else:
    print("You win!")
