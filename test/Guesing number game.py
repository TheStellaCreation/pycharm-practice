print("Guess the number！ \nNumber is between 1-100.\n\n")

secret_num = 20
guess_num = ""
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
    guess_num = int(input())
    if guess_num == secret_num:
        print("Congrats YOU WON!")
        break

    elif guess_num < secret_num:
        print("Your guess was too low: Guess a number higher than " + str(guess_num))
    else:
        print("Your guess was too high: Guess a number lower than " + str(guess_num))
    guess_count += 1

if not guess_count < guess_limit:
    print("YOU LOSE!!! The number is ", str(secret_num))
