# Program to increment each digit of a number by one
def increment_digits_by_one(number):
    # Convert the number to a string to manipulate its digits
    number_str = str(number)
    result_str = ""
    for char in number_str:
        # Check if the character is a digit (0-9)
        if char.isdigit():
            new_digit = str((int(char) + 1) % 10)
            result_str += new_digit
        else:
            result_str += char
    result = int(result_str)    
    return result

number = int(input("Enter a number: "))
result = increment_digits_by_one(number)
print(f"Number with digits incremented by one: {result}")
