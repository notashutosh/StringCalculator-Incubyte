import re


def getNumbersList(input, delimiters=[',']):
    """
    Splits the input string using the specified delimiters.

    Args:
        input (str): The input string to be split.
        delimiters (list, optional): A list of delimiter strings to split the input string. Defaults to [','].

    Returns:
        list: A list of numbers obtained by splitting the input string using the specified delimiters.

    Notes:
    A regular expression is created by combining the delimiters using the '|' operator after escaping them. 
    This is then used to split the input string. 
    """
    return [int(x) for x in re.split(f'{"|".join(map(re.escape, delimiters))}', input)]


def parseInputString(input):
    """
    Parses the input string to extract numbers.

    If the input string starts with "//", it indicates that custom delimiters are used. 
    The custom delimiters are extracted from the string, and the remaining part of the string
    is considered as the list of numbers. If the input string does not start with "//", 
    the default delimiter (comma) is used.

    Args:
        input (str): The input string containing delimiters and numbers.

    Returns:
        list: A list of numbers as strings, split by the specified delimiters.
    """
    if input.startswith("//"):
        delimiterString, numberString = input.split("\n")
        delimiters = delimiterString[2:].strip("[]").split("][")
    else:
        numberString = input
        delimiters = [',']

    return getNumbersList(numberString, delimiters)


def sumOfString(input):
    """
    Calculate the sum of numbers in a given string.

    This function takes a string input, parses it for numbers, and returns the sum of those numbers.
    It ignores numbers greater than 1000 and raises an exception if any negative numbers are found.

    Spec:
    https://blog.incubyte.co/blog/tdd-assessment/
    and 
    https://osherove.com/tdd-kata-1/

    Examples:
    input: "" -> output: 0
    input: 1,1 -> output: 2
    input: //***\n1***1 -> output: 2
    input: -1, -2 -> raises ValueError with msg 'negative numbers not allowed -1,-2'
    input: //[;][***]\n1;2***3" -> output: 6
    input: 1001,2 -> output: 2
    """
    if len(input) == 0:
        return 0
    sum = 0

    negative_numbers = []
    negatives_present = False
    for number in parseInputString(input):
        if number >= 0:
            if number > 1000:
                continue
            sum += number
        else:
            negatives_present = True
            negative_numbers.append(number)

    if negatives_present:
        raise ValueError(
            f"negative numbers not allowed {','.join([str(i) for i in negative_numbers])}")

    return sum
