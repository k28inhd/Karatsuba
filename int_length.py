# Determine if integer has 1 digit
# Returns True if 1 digit, otherwise returns False

def numLength(num):
    converted_num = str((num))
    if len(converted_num) == 1:
        return True
    else:
        return False