import random


def choose_difficulty():
    print("\nChoose your difficulty level:")
    print("1. Easy   - 1 to 50   - 10 attempts")
    print("2. Medium - 1 to 100  - 7 attempts")
    print("3. Hard   - 1 to 500  - 5 attempts")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            return 50, 10, "Easy", 1

        elif choice == "2":
            return 100, 7, "Medium", 2

        elif choice == "3":
            return 500, 5, "Hard", 3

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def get_performance_rating(score):
    if score >= 800:
        return "🏆 Excellent!"

    elif score >= 500:
        return "🔥 Great job!"

    elif score >= 200:
        return "👍 Good attempt!"

    else:
        return "💪 Keep practicing!"


def play_game():
    print("\n" + "=" * 45)
    print("🎯 NUMBER GUESSING GAME")
    print("=" * 45)

    maximum_number, max_attempts, difficulty, multiplier = choose_difficulty()

    secret_number = random.randint(1, maximum_number)

    attempts = 0
    previous_guesses = []

    print(f"\n🔥 Difficulty: {difficulty}")
    print(f"🎲 Guess a number between 1 and {maximum_number}")
    print(f"❤️ You have {max_attempts} attempts.")

    while attempts < max_attempts:

        try:
            guess = int(input("\n👉 Enter your guess: "))

        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess < 1 or guess > maximum_number:
            print(
                f"⚠️ Please enter a number between "
                f"1 and {maximum_number}."
            )
            continue

        if guess in previous_guesses:
            print("⚠️ You already guessed that number.")
            continue

        previous_guesses.append(guess)
        attempts += 1

        remaining_attempts = max_attempts - attempts

        if guess == secret_number:

            score = (max_attempts - attempts + 1) * 100 * multiplier

            print("\n🎉 CONGRATULATIONS!")
            print(f"✅ Correct number: {secret_number}")
            print(f"📊 Attempts: {attempts}")
            print(f"🏆 Score: {score}")
            print(f"⭐ Rating: {get_performance_rating(score)}")

            print(f"📝 Your guesses: {previous_guesses}")

            return score

        elif guess < secret_number:
            print("📈 Too low!")

        else:
            print("📉 Too high!")

        if remaining_attempts > 0:
            print(f"❤️ Remaining attempts: {remaining_attempts}")

            difference = abs(secret_number - guess)

            if difference <= 5:
                print("🔥 Very close!")

            elif difference <= 15:
                print("💡 You're getting closer!")

            else:
                print("🧊 You're far away!")

    print("\n💀 GAME OVER!")
    print(f"🎯 The correct number was: {secret_number}")
    print(f"📝 Your guesses: {previous_guesses}")
    print("💪 Better luck next time!")

    return 0


def main():
    high_score = 0

    print("\n🎮 Welcome to the Number Guessing Game!")

    while True:

        score = play_game()

        if score > high_score:
            high_score = score
            print(f"\n🏆 NEW HIGH SCORE: {high_score}!")

        print("\n" + "-" * 45)
        print(f"🏆 Current High Score: {high_score}")
        print("-" * 45)

        play_again = input("\n🔄 Do you want to play again? (y/n): ")

        if play_again.lower() != "y":
            print("\n👋 Thanks for playing!")
            print("🐍 Keep learning Python!")
            break


if __name__ == "__main__":
    main()