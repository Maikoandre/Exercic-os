"""Return the number of steps it takes to reach 1 according to the rules of the Collatz Conjucture"""

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    starting_number = number
    while starting_number != 1:
        count += 1
        if starting_number % 2 == 0:
            starting_number /= 2
        else:
            starting_number = (starting_number * 3) + 1

    return count
