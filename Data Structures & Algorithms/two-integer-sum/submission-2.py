class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # brute force solution
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return[]
        """

        # 2 pointers and Sorting approach

        check: List[Tuple[int,int]]=[]

        for ind,num in enumerate(nums):
            check.append([num,ind])

        check.sort()
        i,j = 0,len(check)-1

        while i<j:
            added_val = check[i][0] + check[j][0] # [0] refer to column
            if target == added_val:
                return sorted([check[i][1],check[j][1]])
            elif target > added_val:
                i +=1
            else:
                j -=1

        return[] 



        '''
        # best approach
        lookup: dict = {}

        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]

            lookup[target - nums[i]] = i
        return[]
        '''