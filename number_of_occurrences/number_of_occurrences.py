def number_of_occurrences(element, sample):
    i = 0
    for item in sample:
        if item == element:
            i += 1
    return i
