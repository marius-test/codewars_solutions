# input data
# valid

ip1 = "1.2.3.4"
ip2 = "123.45.67.89"

# invalid
ip3 = "1.2.3"
ip4 = "1.2.3.4.5"
ip5 = "123.456.78.90"
ip6 = "123.045.067.089"


def is_valid_IP(strng):
    """This function checks if the input is a valid ip address, it outputs True or False booleans"""
    # split string into a list, separated at '.'
    strng_list = strng.split('.')
    
    # check exactly 4 octets ("numbers")
    if len(strng_list) != 4:
        return False
    
    # iterate through all the elements in the list
    for elem in strng_list:
    # check for non-digit character and empty strings
        if not elem.isdigit():
            return False
        
        # check for leading zeros, one '0' is valid'
        if len(elem) > 1 and elem.startswith('0'):
            return False
        
        #check if the octet is within the valid range (0-255)
        num = int(elem)
        if not 0 <= num <= 255:
            return False
        
    # if the loop completes, all conditions have been met
    return True


if __name__ == "__main__":
    test_data = [ip1, ip2, ip3, ip4, ip5, ip6]
    
    for ip in test_data:
        print(is_valid_IP(ip))
