import re


def splitString(str, delimiters=[',']):
    """
    Splits the input string using the specified delimiters.

    Args:
        str (str): The input string to be split.
        delimiters (list, optional): A list of delimiter strings to split the input string. Defaults to [','].

    Returns:
        list: A list of substrings obtained by splitting the input string using the specified delimiters.

    Notes:
    - a regular expression is created by combining the delimiters using the '|' operator after escaping them. This is then used to split the input string. 
    """
    return re.split(f'{"|".join(map(re.escape, delimiters))}', str)


def sumOfString(input):
    if len(input) == 0:
        return 0
    sum = 0
    delimiters = [',']

    if input.startswith("//"):
        delimiterString, numberString = input.split("\n")
        delimiters = delimiterString[2:].strip("[]").split("][")
    else:
        numberString = input

    negative_numbers = []
    negatives_present = False
    for number in splitString(numberString, delimiters):
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
