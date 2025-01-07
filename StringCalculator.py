def sumOfString(input):
    if len(input) == 0:
        return 0
    sum = 0
    delimiter = ','

    if input.startswith("//"):
        delimiterString, numberString = input.split("\n")
        delimiter = delimiterString[2:]
    else:
        numberString = input

    for number in numberString.split(delimiter):
        sum += int(number)

    return sum
