def reverse_words(text):
    result = []
    word = ''
    for char in text:
        if char != ' ':
            word += char
        else:
            result.append(word[::-1])
            result.append(char)
            word = ''
    result.append(word[::-1])  # reverse the last word
    return ''.join(result)
