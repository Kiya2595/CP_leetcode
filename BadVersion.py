def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
n = 5
bad = 4
res = sol.firstBadVersion(5)
print(res)