# Slower
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



# Faster
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSortHelper(nums, 0, len(nums) - 1)
        return nums

    def quickSortHelper(self, arr, s, e):
        if s >= e:
            return

        # Use median-of-three pivot selection
        pivot_index = self.medianOfThree(arr, s, e)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[e] = arr[e], arr[pivot_index]

        # Partitioning
        left = s
        for i in range(s, e):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[e] = arr[e], arr[left]

        # Recursively apply to sub-arrays
        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)

    def medianOfThree(self, arr, s, e):
        mid = (s + e) // 2
        a, b, c = arr[s], arr[mid], arr[e]
        if a < b:
            if b < c:
                return mid
            elif a < c:
                return e
            else:
                return s
        else:
            if a < c:
                return s
            elif b < c:
                return e
            else:
                return mid

class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        return self.sortArray(left) + [pivot] + self.sortArray(right)
