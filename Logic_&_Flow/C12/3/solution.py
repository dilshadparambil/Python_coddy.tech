def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        # Calculate 100 divided by the input value
        # Return the result
        number = int(input_string)
        result = 100 / number
        print(result)
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        print("Input must be a number!")
    except ZeroDivisionError:
        # Handle the case where input is zero
        print("Cannot divide by zero!")
    except:
        # Handle any other unexpected exceptions
        print("Invalid input type!")
    return None