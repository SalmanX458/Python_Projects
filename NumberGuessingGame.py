import random

print('I am thinking about a number between 1 and 100. Guess It!')
secret_number = random.randint(1, 100)
a = False
try_count = 0
while True:
    while not a:
        number_entered = input('Enter a Number: ')
        try:
            number_entered = int(number_entered)
        except ValueError:
            print("Invalid Input. Please Input a number.")
            continue

        try_count += 1
        if number_entered == secret_number:
            print('That is Correct!')
            print("It took you ", try_count , "tries to Guess. ")
            break
        elif number_entered < secret_number:
            print('Low! Enter Again.')
            continue
        else:
            print('High! Enter Again.')
    # Play Again
    user_input = input("Do You want to Play Again (y/n): ")
    try:
        user_input = str(user_input)
    except ValueError:
        print("Invalid Answer.")
        continue
    if user_input.lower() == "y":
            print("Restarting...")
            continue
    else:
            exit()