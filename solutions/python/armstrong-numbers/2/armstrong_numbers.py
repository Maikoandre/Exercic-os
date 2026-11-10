def is_armstrong_number(number):
    digits = (int(digit) for digit in str(number))
    power = len(str(number))
    result = 0

    for digit in digits:
        result += digit ** power

    return result == number
