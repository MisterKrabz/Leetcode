class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        for shift in range(31, -1, -1):
            if (divisor << shift) <= dividend:
                dividend -= divisor << shift
                quotient += 1 << shift

        if negative:
            quotient = -quotient

        return quotient
