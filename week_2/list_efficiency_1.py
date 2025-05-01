import time

result = []


def add_to_end(items, n):
    for i in range(n):
        items.append(i)


input = pow(10, 5)
start_add = time.time()
add_to_end(result, input)
end_add = time.time()

print("time to add:", round(end_add - start_add, 6), "s")


def remove_from_end(items):
    while 0 < len(items):
        items.pop()


start_remove = time.time()
remove_from_end(result)
end_remove = time.time()

print("time to remove:", round(end_remove - start_remove, 6), "s")
