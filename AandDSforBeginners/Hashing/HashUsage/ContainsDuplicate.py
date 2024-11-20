class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num in count.values():
            if num > 1:
                return True

        return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(count > 1 for count in Counter(nums).values())
