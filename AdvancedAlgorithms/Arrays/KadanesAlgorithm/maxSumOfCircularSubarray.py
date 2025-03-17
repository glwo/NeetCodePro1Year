# Brute force, O(n^2) time, O(1) space
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            cur_sum = 0
            for j in range(i, i + n):
                cur_sum += nums[j % n]
                res = max(res, cur_sum)

        return res

# Kadane's, O(n) time, O(1) space
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax

# Prefix and Suffix sums, O(n) time, O(n) space
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)

        max_sum = nums[0]
        cur_max = 0
        prefix_sum = 0

        for i in range(n):
            cur_max = max(cur_max, 0) + nums[i]
            max_sum = max(max_sum, cur_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i + 1])

        return max_sum
