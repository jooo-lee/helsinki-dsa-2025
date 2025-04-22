def check_year(year):
    first_half = int(str(year)[:2])
    second_half = int(str(year)[2:])
    return pow((first_half + second_half), 2) == year
