class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negatives = [-num for num in nums]

        heapq.heapify(negatives);

        for i in range(k - 1):
            -heapq.heappop(negatives)
            heapq.heapify(negatives)

        return -negatives[0]
