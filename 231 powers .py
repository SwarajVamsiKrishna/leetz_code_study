class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        if n == 1:
            return True
        
        if n % 2 != 0:
            return False
        
        return self.isPowerOfTwo(n // 2)
        

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)

#//only for powers of 2 we can use bit masking as n & (n-1) == 0 , meaning it is a power of 2 , the power and next element are always different and & will give zero
# for the same thing power of three , if the highest power of threee is divisible by the number it is divisible by three for example 27 is divisble by 9 which means 3^3 is divisble by 3^2

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# for any other number lets say K
K = 9
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % K == 0:
            n //= K

        return n == 1


# for the power of 4 there is an additional condition where we need ti mash the bits with 010101010101 where 4 powers are haveing even 1 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (
            n > 0 and
            (n & (n - 1)) == 0 and
            (n & 0x55555555) != 0
        )
