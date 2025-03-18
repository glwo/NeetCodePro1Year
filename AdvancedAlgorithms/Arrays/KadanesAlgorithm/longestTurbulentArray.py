# Brute force O(n^2) time, O(1) space
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 1

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                continue

            sign = 1 if arr[i] > arr[i + 1] else 0
            j = i + 1
            while j < n - 1:
                if arr[j] == arr[j + 1]:
                    break
                curSign = 1 if arr[j] > arr[j + 1] else 0
                if sign == curSign:
                    break
                sign = curSign
                j += 1

            res = max(res, j - i + 1)

        return res

# Sliding Window O(n) time, O(1) space
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res

# Iteration O(n) time, O(1) space
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = cnt = 0
        sign = -1

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                cnt = cnt + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                cnt = cnt + 1 if sign == 1 else 1
                sign = 0
            else:
                cnt = 0
                sign = -1

            res = max(res, cnt)

        return res + 1
