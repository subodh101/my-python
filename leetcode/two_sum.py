from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = dict()
#         for i in range(len(nums)):
#             # keep adding keys like 7 at 0, 2 at 1, -4 at 2...
#             d[target - nums[i]] = i      
#         for i in range(len(nums)):
#             # keep check in 2, 9, ... in d because that adds up to the target
#             # another check is to remove duplicate indices, because that's not allowed
#             if nums[i] in d and i != d[nums[i]]:
#                 return [i, d[nums[i]]]


#  Better implementation in terms of time complexity
#  Both the creation of the dictionary and thee check for the answer is being done in the same for loop.
#  This way there's no need to check for duplicate imdices because they are created after the check.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            # keep check in 2, 9, ... in d because that adds up to the target
            if nums[i] in d:
                return [i, d[nums[i]]]
            # if the check is unsuccessful then update the dictionary
            else:
                d[target - nums[i]] = i
