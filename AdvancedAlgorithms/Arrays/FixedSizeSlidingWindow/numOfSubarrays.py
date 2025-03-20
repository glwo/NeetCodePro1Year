# Brute force
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        for r in range(len(arr) - k + 1):

            tmp = arr[r:r + k]

            avg = sum(tmp) / k

            if avg >= threshold:
                count += 1

        return count

# Sliding window
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res
