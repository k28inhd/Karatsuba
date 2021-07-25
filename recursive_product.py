# Recursively compute the product of two integers

def compute_product(int_1, int_2):
  # Base Case: both integers are 0
  if int_1 == 0 or int_2 == 0:
    return 0
  # Recursive Case
  else:
    return int_1 + compute_product(int_1, (int_2 - 1))