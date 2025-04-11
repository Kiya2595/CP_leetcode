class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        reversed_number = 0
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10
        return num == reversed_number
sol = Solution()
x = 121
print(sol.isPalindrome(x))
