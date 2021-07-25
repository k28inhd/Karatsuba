# Splits integer with even number of digits into 2 
# equal lengths and returns each half as an INT

# "number" must have an even length
import math

def inHalf(number): 
    num_as_str = str(number)
    
    # Print Original String
    print("Original number is : ", number)

    # Determine Half Number Length 
    half_length = int(len(num_as_str) / 2)

    # Create List of 2 Items: First and Second Halves of Original Number 
    half_number = []
    for digit in range(0, len(num_as_str), half_length):
        half_number.append(int(num_as_str[digit : digit + half_length]))
    
    return half_number[0], half_number[1]