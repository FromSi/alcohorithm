def make(numbers):
    N = len(numbers)
    for i in range(N + 1):
        for j in range(N - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == '__main__':
    numbers = [123, 12, 34, 111, 5]
    print(make(numbers))
