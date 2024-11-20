class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, a in enumerate(nums):
            remainder = target - a

            if remainder in dic:
                return [dic[remainder], i]
            dic[a] = i
        