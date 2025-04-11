class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
nums = [1,2,3,1]
result = Solution()
print(result.containsDuplicate(nums))