# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(input_number):
    # if input number is one-digit number then return count = 0
    if 0 <= input_number <= 9:
        return 0

    # Our variables
    current_number = input_number   # current_number
    output_number = 1               # output number
    count = 1                       # multiplicative persistence

    while True:
        while current_number:
            # Take last digit from current number and multiple his at output number
            last = current_number % 10
            current_number = current_number // 10
            output_number *= last

        # If result is between 0 and 9 then return multiplicative persistence (count).
        # Otherwise we run cycle 'while True' again.
        if 0 <= output_number <= 9:
            return count
        else:
            current_number = output_number
            output_number = 1
            count += 1
