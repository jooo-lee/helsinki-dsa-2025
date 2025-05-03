def count_rounds(numbers):
    n = len(numbers)
    rounds = 1

    # Store indices of numbers in numbers list
    indices = [-1] * (n + 1) 
    for i in range(n):
        indices[numbers[i]] = i

    # If number occurs after number + 1, increment rounds
    for number in range(2, n + 1):
        if indices[number] < indices[number - 1]:
            rounds += 1

    return rounds
