def sumOfString(input):
    if len(input) == 0:
        return 0
    sum = 0
    delimiter = ','

    for number in input.split(delimiter):
        sum += int(number)

    return sum
