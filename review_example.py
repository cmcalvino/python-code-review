def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += i
    return total / len(numbers)

data = [10, 20, 30, 40]
print(calculate_average(data))
