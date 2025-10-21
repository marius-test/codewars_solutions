# for testing and debugging code

n = 58


def bit_counting(n):
    b = bin(n)
    b_digits = b.replace('0b', '')
    
    return b_digits.count('1')

if __name__ == "__main__":
    print(bit_counting(n))
