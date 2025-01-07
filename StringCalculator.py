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

    negative_numbers = []
    negatives_present = False
    for number in numberString.split(delimiter):
        n = int(number)
        if n >= 0:
            if n > 1000:
                continue
            sum += n
        else:
            negatives_present = True
            negative_numbers.append(n)

    if negatives_present:
        raise ValueError(
            f"negative numbers not allowed {','.join([str(i) for i in negative_numbers])}")

    return sum
