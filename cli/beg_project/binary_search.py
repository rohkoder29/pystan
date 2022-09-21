from random import randint, seed
from timeit import default_timer as timer


# seq = [randint(1, 50) for _ in range(15)]
# seq = [23, 3, 33, 6, 45, 36, 41, 43, 5, 12, 33, 14, 30, 13, 15]
# seq.sort()
# print(seq)

# seed(1)
dataset = [randint(-4200, 4200) for _ in range(3650)]
dataset.sort()
# print(len(dataset))

# n = int(input('Enter number whose position is to be searched: '))
NUMBER = randint(-4200, 4200)


# standard if...in block
print("\nstandard if...in block")
start = timer()
if NUMBER in dataset:
    print(f"Element {NUMBER} at index {dataset.index(NUMBER)}")
else:
    print(f"Element {NUMBER} not in list.")
end = timer()

print(f"Search took {round((end - start)*1000000)} ms to complete.")


# standard for-loop
print("\nstandard for-loop")

start = timer()
for i in dataset:
    if i == NUMBER:
        print(f"Element {NUMBER} at index {dataset.index(NUMBER)}")
        break
end = timer()

print(f"Search took {round((end - start)*1000000)} ms to complete.")


# standard while-loop
print("\nstandard while-loop")

i = 0
start = timer()
while len(dataset) > i:
    if dataset[i] == NUMBER:
        print(f"Element {NUMBER} at index {dataset.index(NUMBER)}")
        break
    i += 1
end = timer()

print(f"Search took {round((end - start)*1000000)} ms to complete.")


# binary search

print("\nbinary search")

def binary_search(item: int, seq: list) -> int:
    """ Implementation of the Binary Search algorithm. """
    dts_start = 0
    dts_end = len(seq) - 1
    dts_mid = 0

    while dts_start <= dts_end:
        dts_mid = (dts_end + dts_start) // 2
        if seq[dts_mid] < item:
            dts_start = dts_mid + 1
        elif seq[dts_mid] > item:
            dts_end = dts_mid - 1
        else:
            return dts_mid

    return -1


start = timer()
result = binary_search(NUMBER, dataset)
end = timer()

if result != -1:
    print(f"Element {NUMBER} is at index {result}")
else:
    print(f"Element {NUMBER} not in list.")

print(f"Search took {round((end - start)*1000000)} ms to complete.")
