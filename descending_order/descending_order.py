def descending_order_v1(num):
    # create an empty list to store the digits
    num_list = []
    
    # iterate through each character in the string representation of the number
    for digit in str(num):
        # convert the character to an integer and add it to the list
        num_list.append(int(digit))
    
    # sort the list of digits in descending order.
    # the sort() method modifies the list in-place.
    num_list.sort(reverse=True)
    
    # initialize an empty string to build the new number
    intermediary_string = ""
    
    # loop through the sorted list of digits
    for i in num_list:
        # convert each digit back to a string and append it to the intermediary string
        intermediary_string += str(i)
    
    # convert the final string back to an integer
    intermediary_string = int(intermediary_string)
    
    # return the result
    return intermediary_string


def descending_order_v2(num):
    # step 1: create a list of digits using a list comprehension.
    # this is a concise way to loop through the string and convert each character to an integer.
    num_list = [int(digit) for digit in str(num)]
    
    # step 2: sort the list in place in descending order.
    # the sort() method is used because we don't need a copy of the list.
    num_list.sort(reverse=True)
    
    # step 3: join the digits back into a string and convert to an integer.
    # a generator expression is used with the join() method to efficiently
    # concatenate the string representations of the digits.
    return int("".join(str(i) for i in num_list))


def descending_order_v3(num):
    # this one-liner combines all the steps using a chain of function calls.
    # 1. str(num): converts the integer to a string.
    # 2. sorted(..., reverse=True): sorts the characters of the string in descending order,
    #    returning a list of characters.
    # 3. "".join(...): joins the sorted characters back into a single string.
    # 4. int(...): converts the final string back into an integer.
    return int("".join(sorted(str(num), reverse=True)))
