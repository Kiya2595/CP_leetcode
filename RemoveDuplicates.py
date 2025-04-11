class Solution:
    def removeDuplicates(self, nums: List[int])->int:
        duplicates = 0
        for x in range(1,len(nums)):
            if nums[x] != nums[duplicates]:
                duplicates += 1
                nums[duplicates] = nums[x]
        return duplicates + 1
        if not nums:
            return 0
s = Solution()
result = s.removeDuplicates([1,1,2])
print(result)