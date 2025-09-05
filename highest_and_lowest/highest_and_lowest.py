def high_and_low(numbers):
    str_list = numbers.split(" ")
    int_list = list(map(int, str_list))
    highest = max(int_list)
    lowest = min(int_list)
    return f"{highest} {lowest}"
