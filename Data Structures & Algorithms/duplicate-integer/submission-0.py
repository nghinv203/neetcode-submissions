class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set();
        mySet.update(nums)
        if len(mySet) == len(nums):
            return False;
        return True;
        