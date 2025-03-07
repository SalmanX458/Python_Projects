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
        print('Too Low! Enter Again.')
        continue;
    elif number_entered > secret_number:
        print('Too High! Enter Again.')
        continue;
    else:
        print("Invalid Number! Tru Again.")
        continue;
print('Game Over!')

