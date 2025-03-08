Title = "My Calculator"
print(Title.title(), "| Enter q to Quit.")

# Calculations
quit_calc = False
while not quit_calc:
    first_number = input('Enter First Number (or q to quit): ')
    if first_number.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    operation = input('Choose Operation (+ , - , * , / , % , // , ** ): ')
    if operation.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    second_number = input('Enter Second Number (or q to quit): ')
    if second_number.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    # Validate inputs
    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Perform calculations
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number == 0:
            print("Cannot divide by zero.")
            continue
        result = first_number / second_number
    elif operation == '%':
        result = first_number % second_number
    elif operation == '//':
        if second_number == 0:
            print("Cannot divide by zero.")
            continue
        result = first_number // second_number
    elif operation == '**':
        result = first_number ** second_number
    else:
        print("Invalid operation. Please choose a valid operation.")
        continue

    # Display result
    print(f"Result: {result}")