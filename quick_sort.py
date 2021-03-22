def handler(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
    
    return handler(less) + [pivot] + handler(greater)


if __name__ == '__main__':
    numbers = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]
    print(handler(numbers))
