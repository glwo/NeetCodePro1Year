class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums, 0, (len(nums) - 1))
        return nums

    def quickSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return

        pivot = arr[e]
        left = s
        for i in range(s, e):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)
