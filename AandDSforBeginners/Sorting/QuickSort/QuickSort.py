class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs


    def quickSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return

        #In place
        pivot = pairs[e] # right most
        left = s

        for i in range(s, e):
            # partition
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)
