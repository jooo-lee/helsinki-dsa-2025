def check_number(number):
    # Here we can also import re and
    # check that our parameter number matches the
    # regular expression ^0[0-9]{8}$,
    # that is, a 0 followed by exactly eight digits
    if len(number) != 9 or number[0] != "0":
        return False

    sum = 0
    values = [3, 7, 1, 3, 7, 1, 3, 7]
    for i in range(8):
        sum += int(number[i]) * values[i]

    # We could instead write
    # last = (10 - sum % 10) % 10
    # and then check that
    # int(number[-1]) == last
    if sum % 10 == 0:
        return int(number[8]) == 0
    return 10 - (sum % 10) == int(number[8])
