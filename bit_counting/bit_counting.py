def count_bits(n):
    b = bin(n)
    b_digits = b.replace('0b', '')
    
    return b_digits.count('1')
