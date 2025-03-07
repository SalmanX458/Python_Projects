Title = 'Basic Calculator'
print(Title.title())
first_number = float(input('Enter First Number: '))
operation = input('Choose Operation (+ , - , * , / , % , // ): ')
second_number = float(input('Enter Second Number: '))

if operation == '+':
   result =  first_number + second_number
   print('Result is: ', result)
elif operation == '-':
   result =  first_number - second_number
   print('Result is: ', result)
elif operation == '*':
   result =  first_number * second_number
   print('Result is: ', result)
elif operation == '/':
   result =  first_number / second_number
   print('Result is: ', result)
elif operation == '%':
   result =  first_number % second_number
   print('Result is: ', result)
elif operation == '//':
   result =  first_number // second_number
   print('Result is: ', result)
elif operation == '**':
   result =  first_number ** second_number
   print('Result is: ', result)
else:
   print('Invalid Input.')