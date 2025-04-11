def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1,n
        while low <= high:
            mid = (low + high)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1
solu = Solution()
n = 10 
pick = 6
result = solu.guessNumber(10)
print(result)