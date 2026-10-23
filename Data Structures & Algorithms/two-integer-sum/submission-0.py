class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i,num in enumerate(nums):
            if num in diff:
                diff[num].append(i)
                return diff[num]
            complement = target - num
            diff[complement] = [i]
        return []
        

        