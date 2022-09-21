def square_sum(numbers):
    squared_numbers_list = []
    for i in numbers:
        squared_numbers_list.append(i**2)
    return sum(squared_numbers_list)
