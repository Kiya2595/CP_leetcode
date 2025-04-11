class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        intersection = []
        for num in count1:
            if num in count2:
                intersection.extend([num] * min(count1[num],count2[num]))
        return intersection
nums1 = [1,2,2,1]
nums2 = [2,2]
sol = Solution()
print(sol.intersect(nums1,nums2))