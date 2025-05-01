def find_segments(data):
    count = 1
    currChar = data[0]
    output = []
    for i in range(1, len(data)):
        if data[i] == currChar:
            count += 1
        else:
            output.append((count, currChar))
            currChar = data[i]
            count = 1
    output.append((count, currChar))
    return output


# Alternative approach:
# Create output list and set count variable to 0
# for i in range(len(data)):
#   Increment count by 1
#   If i == len(data) - 1 i.e. we have reached the end of the string
#   or if data[i] != data[i + 1], then append pair to output and reset count
# return output
#
# There is also a regular expression approach below that I do not understand yet
# import re
#
# def find_segments(data):
#     matches = re.findall(r"(([a-z])\2*)", data)
#     result = [(len(match[0]), match[1]) for match in matches]
#     return result
