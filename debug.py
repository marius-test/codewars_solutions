# for testing and debugging code

test_data_1 = "1 2 3 4 5"
test_data_2 = "1 2 -3 4 5"
test_data_3 = "1 9 3 4 -5"


def high_and_low(numbers):
    str_list = numbers.split(" ")
    int_list = list(map(int, str_list))
    highest = max(int_list)
    lowest = min(int_list)
    return f"{highest} {lowest}"


if __name__ == "__main__":
    all_test_data = [test_data_1, test_data_2, test_data_3]
    for i, data in enumerate(all_test_data, start=1):
        high_low = high_and_low(data)
        print(f"Test {i}: input = {data} -> output = {high_low}")
