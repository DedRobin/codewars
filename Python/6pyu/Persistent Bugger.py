# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(input_number):
    current_number = input_number
    output_number = 1
    while True:
        while current_number:
            last = current_number % 10
            current_number = current_number // 10
            output_number *= last
        if 0 <= output_number <= 9:
            return output_number
        else:
            current_number = output_number
            output_number = 1
