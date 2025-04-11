class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 0
        power_of_5 = 5
        while n >= power_of_5:
            x += n // power_of_5
            power_of_5 *= 5
        return x
result = Solution()
print(result.trailingZeroes(3))