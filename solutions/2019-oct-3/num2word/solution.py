import math


units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
elevens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
magnitudes = ["thousand", "million", "billion", "trillion"]

def num2word(n: int, depth=0) -> str:
    """
        returns the word representation of a number 
    """
    # othe ranges are not allowed
    assert n >= 0 and n <= 11_000_000

    # special case for deeper zeros
    if depth > 0 and n == 0:
        return ""

    if n >=0 and n <= 9:
        return units[n]

    if n >= 10 and n <= 19:
        return elevens[n % 10]

    if n >= 20 and n <= 99:
        result = tens[n // 10]
        remaining = num2word(n % 10, depth+1)
        if remaining != "":
            result = result + "-" + remaining
        # if depth > 0:
        #     result = "and " + result
        return result

    if n >= 100 and n <= 999:
        result = units[n // 100] + " hundred"
        remaining = num2word(n % 100, depth+1)
        if remaining != "":
            result = result + " and " + remaining
        return result

    # if n >= 1000:
    leading = n // 1000
    remaining = n % 1000

    # 1_000_000

    firstSegment = num2word(leading, depth+1) 

    if leading % 1000 != 0:
        firstSegment = firstSegment + " " + magnitudes[depth] 

    remainingSegment = num2word(remaining, depth+1)
    if remainingSegment != "":
        if remaining < 100:
            firstSegment += " and"
        return firstSegment  + " " + remainingSegment
    else:
        return firstSegment
