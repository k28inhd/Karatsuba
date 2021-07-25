KARATSUBA ALGORITHM (Pseudocode)

INPUT: two n-digit positive integers x and y. 
OUTPUT: the product x · y.
ASSUMPTION: n is a power of 2.

BASE CASE:
if n = 1 then
compute x · y in one step and return the result 

RECURSIVE CASE:
else
a, b := first and second halves of x
c, d := first and second halves of y 
compute p := a + b and q := c + d using grade-school addition
recursively compute ac := a · c, bd := b · d, and pq := p · q
compute adbc := pq - ac - bd using grade-school addition
compute 10n · ac + 10n/2 · adbc + bd using grade-school addition 
and return the result