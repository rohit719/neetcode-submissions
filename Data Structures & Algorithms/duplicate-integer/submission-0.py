"""
# Brute force solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums:List[int] = nums
        for i in range(len(self.nums)-1):
            for j in range(self.nums.index(i)+1):
                if self.num[i] == self.num[j]:
                    return  True
        return False
"""
'''
# Reducing time complexity to O(nlogn)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums: List[int] = sorted(nums)

        for i in range(len(self.nums) - 1):
            if self.nums[i] == self.nums[i + 1]:
                return True

        return False
'''

# Reducing time complexity to O(n) using set 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums: List[int] = nums

        seen:set[int] = set()

        for i in self.nums:

            if i in seen:
                return True
            seen.add(i)

        return False
