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
