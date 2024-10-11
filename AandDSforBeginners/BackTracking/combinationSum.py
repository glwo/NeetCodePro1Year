class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        currSumArr = []
        def dfs(i, currSum):
            if i >= len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(currSumArr.copy())
                return

            currSumArr.append(nums[i])
            currSum += nums[i]
            dfs(i, currSum)
            currSum -= nums[i]
            currSumArr.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)
        return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
