# List all of the factors of a value
def list_factors(n):
    # Explain the line of code below.
    return [i for i in range (1, n+1) if n % i == 0]
# Comment your explination here.
# It return the out and check the number is an odd number or a even number.
# This will take whatever number we put in and check.


if __name__ == '__main__': # Check to see of the application is running locally.
    user_input = input('Please enter a number here: ') # Ask the user for a number.

try: 
    # Convert that user input to an interger.
    number = int(user_imput)
    # Check to see if the number is positive or negative.
    if number <= 0:
        print('Please enter a positive number: ')
    else: 
        # Get the facters for the value input.
        factors = list_factors(number)
        # Print the factors of the input value.
        print(f'The factors of {number} are {factors}')

except ValueError: 
    # handles the exception negative values or 0.
    print('That is an invalid number. Please input a positive interger: ')