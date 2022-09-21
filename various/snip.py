numbers = [42, 73, 0, 16, 10]

evens = []
for num in numbers:
    if num % 2:
        evens.append(num)

print(evens)    # [73]

evens = [num for num in numbers if num % 2]
print(evens)    # [73]
