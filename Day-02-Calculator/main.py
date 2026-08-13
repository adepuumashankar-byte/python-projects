import math


def display_menu():
    print("\n" + "=" * 50)
    print("🧮 PYTHON ADVANCED CALCULATOR")
    print("=" * 50)

    print("1.  ➕ Addition")
    print("2.  ➖ Subtraction")
    print("3.  ✖️ Multiplication")
    print("4.  ➗ Division")
    print("5.  %  Modulus")
    print("6.  🔢 Power")
    print("7.  // Floor Division")
    print("8.  √  Square Root")
    print("9.  📊 Percentage")
    print("10. |x| Absolute Value")
    print("11. 📜 Calculation History")
    print("12. 🗑️ Clear History")
    print("13. 🔄 Use Previous Result")
    print("14. ❌ Exit")


def get_number(message):
    while True:
        try:
            return float(input(message))

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def format_number(number):
    if number.is_integer():
        return str(int(number))

    return f"{number:.4f}".rstrip("0").rstrip(".")


def calculate(num1, num2, choice):

    if choice == "1":
        return num1 + num2

    elif choice == "2":
        return num1 - num2

    elif choice == "3":
        return num1 * num2

    elif choice == "4":

        if num2 == 0:
            return None

        return num1 / num2

    elif choice == "5":

        if num2 == 0:
            return None

        return num1 % num2

    elif choice == "6":
        return num1 ** num2

    elif choice == "7":

        if num2 == 0:
            return None

        return num1 // num2


def get_operator(choice):

    operators = {
        "1": "+",
        "2": "-",
        "3": "×",
        "4": "÷",
        "5": "%",
        "6": "**",
        "7": "//"
    }

    return operators.get(choice)


def show_history(history):

    print("\n" + "=" * 50)
    print("📜 CALCULATION HISTORY")
    print("=" * 50)

    if not history:
        print("📭 No calculations available.")

    else:

        for index, calculation in enumerate(history, start=1):
            print(f"{index}. {calculation}")


def main():

    history = []
    previous_result = None
    operation_count = 0

    print("\n🎉 Welcome to the Python Advanced Calculator!")

    while True:

        display_menu()

        choice = input("\n👉 Choose an option: ")

        # EXIT
        if choice == "14":

            print("\n" + "=" * 50)
            print("👋 Thank you for using the calculator!")
            print(f"📊 Total calculations: {operation_count}")
            print("=" * 50)

            break

        # HISTORY
        elif choice == "11":

            show_history(history)
            continue

        # CLEAR HISTORY
        elif choice == "12":

            if history:

                history.clear()

                print("\n🗑️ Calculation history cleared!")

            else:

                print("\n📭 History is already empty.")

            continue

        # PREVIOUS RESULT
        elif choice == "13":

            if previous_result is None:

                print("\n❌ No previous result available.")

            else:

                print(
                    f"\n🔄 Previous result: "
                    f"{format_number(previous_result)}"
                )

            continue

        # SQUARE ROOT
        elif choice == "8":

            num = get_number("\nEnter a number: ")

            if num < 0:

                print("❌ Cannot calculate square root of a negative number.")
                continue

            result = math.sqrt(num)

            calculation = (
                f"√{format_number(num)} = "
                f"{format_number(result)}"
            )

            print(f"\n✅ Result: {calculation}")

            history.append(calculation)
            previous_result = result
            operation_count += 1

        # PERCENTAGE
        elif choice == "9":

            number = get_number("\nEnter the number: ")
            percentage = get_number("Enter percentage: ")

            result = (number * percentage) / 100

            calculation = (
                f"{format_number(percentage)}% of "
                f"{format_number(number)} = "
                f"{format_number(result)}"
            )

            print(f"\n✅ Result: {calculation}")

            history.append(calculation)
            previous_result = result
            operation_count += 1

        # ABSOLUTE VALUE
        elif choice == "10":

            num = get_number("\nEnter a number: ")

            result = abs(num)

            calculation = (
                f"|{format_number(num)}| = "
                f"{format_number(result)}"
            )

            print(f"\n✅ Result: {calculation}")

            history.append(calculation)
            previous_result = result
            operation_count += 1

        # BASIC OPERATIONS
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

            num1 = get_number("\nEnter first number: ")

            num2 = get_number("Enter second number: ")

            result = calculate(num1, num2, choice)

            if result is None:

                print("\n❌ Cannot divide or perform modulus by zero.")
                continue

            operator = get_operator(choice)

            calculation = (
                f"{format_number(num1)} "
                f"{operator} "
                f"{format_number(num2)} "
                f"= "
                f"{format_number(result)}"
            )

            print(f"\n✅ Result: {calculation}")

            history.append(calculation)

            previous_result = result

            operation_count += 1

        # INVALID MENU OPTION
        else:

            print("\n❌ Invalid option.")
            print("Please choose an option from 1 to 14.")


if __name__ == "__main__":
    main()