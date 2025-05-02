def find_rounds(numbers):
    current = 1
    result = []
    while current <= len(numbers):
        round = []
        for number in numbers:
            if number == current:
                round.append(number)
                current += 1
        result.append(round)
    return result
