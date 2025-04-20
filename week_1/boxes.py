def min_count(product_count, box_size):
    boxes_needed = 0
    while product_count > 0:
        product_count -= box_size
        boxes_needed += 1
    return boxes_needed

# Alternate solution
import math
def min_count(product_count, box_size):
    return math.ceil(product_count / box_size)