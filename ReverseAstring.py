a = False
while not a:
    user_input = input("Enter a string (or 'q' to quit): ")
    
    # Allow the user to quit
    if user_input.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break
    
    # Handle empty strings
    if not user_input:
        print("You entered an empty string. Please try again.")
        continue
    
    # Check if the input is a valid string (not just digits)
    if user_input.isdigit():
        print("Please enter a valid string (not a number")
        continue
    
    # Reverse the string and display the result
    reversed_string = user_input[::-1]
    print("Reversed string is:", reversed_string)