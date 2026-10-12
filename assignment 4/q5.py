
secret_number = 37
attempts = 0

while attempts < 5:
    guess = int(input("Guess the secret number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("You Win! Correct guess.")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

if guess != secret_number:
    print("You Lose! The secret number was", secret_number)

print("Attempts used:", attempts)
