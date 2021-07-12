from typing import List

# Logic

# create a dp 2d array of size (n+1)*(m+1) with all zero elements.
# iterate over the elements and check:
    # if there's an element match, add one to the diagonal element.
    # else do nothing

# ---------------------------------------

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]
        dp = [[0]*(len(nums2)+1) for i in range(len(nums1)+1)]
        ans = 0

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])

        return ans
