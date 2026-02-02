rounds = 0
score = 0
attempts = 0
seed = 7

print("🎯 Welcome to the Number Guessing Game! 🎯\n")
print("I have picked a number between 1 and 20. Can you guess it?")

while True:
    seed += 1
    a = 1103515245
    c = 12345
    m = 2**31
    seed = (a * seed + c) % m
    num = (seed % 20) + 1

    guess = input("Enter your guess: ")

    if guess.isdecimal():
        guess = int(guess)
    else:
        print("Please enter a number")
        continue

    if guess > 20 and guess < 1:
        print("Only enter number between 1 to 20")
    else:
        if (guess + 1) == num or (guess - 1) == num:
            print("➖ Close Enough")
            attempts += 1
            continue
        elif guess > num:
            print("⬇️ Too high!")
            attempts += 1
            continue
        elif guess < num:
            print("⬆️ Too low!")
            attempts += 1
            continue
        else:
            attempts += 1
            score += 1

            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            print(f"Your current score: {score}")

            play_nxt_round = input("Do you want to play another round? (yes/no): ")

            if play_nxt_round == "yes":
                attempts = 0
                print()
                print("I have picked a number between 1 and 20. Can you guess it?")
                continue
            else:
                print(f"\nThanks for playing! Your final score: {score}")
                break