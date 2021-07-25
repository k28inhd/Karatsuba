
import split_int_in_half as half_int
import recursive_product
import int_length

def karatsuba(int1, int2):
    # Confirm length of two integers is the same
    if len(str(int1)) != len(str(int2)):
        return ("Length of integers must be the same!")
    # Base Case: length of integers is 1
    elif int_length.numLength(int1) and int_length.numLength(int2):
        return int1 * int2
    # Recursive Case
    else:
        a, b = half_int.inHalf(int1)
        c, d = half_int.inHalf(int2)
        p = a + b
        q = c + d
        ac = recursive_product.compute_product(a, c)
        bd = recursive_product.compute_product(b, d)
        pq = recursive_product.compute_product(p, q)
        adbc = pq - ac - bd
        n = len(str(int1))
        result = int(((10 ** n) * ac) + ((10 ** (n / 2)) * adbc) + bd)
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)
        print("d = ", d)
        print("p = ", p)
        print("q = ", q)
        print("ac = ", ac)
        print("bd = ", bd)
        print("pq = ", pq)
        print("adbc = ", adbc)
        print("n = ", n)
        print("Karatsuba says the answer is?! ")
    
        return result

# Test Cases
print(karatsuba(123, 5678))
print(karatsuba(1, 5))
print(karatsuba(1234, 5678))
