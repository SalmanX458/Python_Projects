import random

print('I am thinking about a number between 100 and 200. Guess It!')
secret_number = random.randint(100, 200)
i = 0
while i <= 5:
    number_entered = int(input('Enter a Number: '))
    if number_entered == secret_number:
        print('That is Correct!')
        break;
    elif number_entered < secret_number:
        print('Low! Enter Again.')
        continue;
    elif number_entered > secret_number:
        print('High! Enter Again.')
        continue;
    else:
        print("Invalid Number! Try Again.")
        continue;
print('Game Over!')

