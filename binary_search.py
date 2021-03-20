def handler(numbers, number):
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        
        if guess == number:
            return mid

        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
            
    return None
  
if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    print(handler(numbers, 2))
