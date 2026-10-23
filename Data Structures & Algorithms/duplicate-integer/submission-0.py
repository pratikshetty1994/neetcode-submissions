class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
