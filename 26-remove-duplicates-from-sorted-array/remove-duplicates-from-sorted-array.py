class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0  # index of last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[k]:   # found a new unique value
                k += 1
                nums[k] = nums[i]    # move it to the next unique position

        return k + 1                 # number of unique elements
