# Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Requirements

#     You can assume you will be given an integer input.
#     You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
#     NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

# Example

# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */

# if number doesn't end in 1 3 7 9  is not prime 
# if it ends in 1 3 7 9  and the sum of numbers is divizible with 3 is not prime 
#  if it divides by 7 and 11 is not prime  

# test.assert_equals(is_prime(0),  False, "0  is not prime")
# test.assert_equals(is_prime(1),  False, "1  is not prime")
# test.assert_equals(is_prime(2),  True, "2  is prime")
# test.assert_equals(is_prime(73), True, "73 is prime")
# test.assert_equals(is_prime(75), False, "75 is not prime")
# test.assert_equals(is_prime(-1), False, "-1 is not prime")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(int(25**0.5))