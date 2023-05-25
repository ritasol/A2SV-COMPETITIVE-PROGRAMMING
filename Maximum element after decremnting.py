class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        left,right = 0,1
        while right < len(arr):
            l_val,r_val = arr[left] , arr[right]
            diff = r_val - l_val
            if diff > 1:
                arr[right] = (arr[left] + 1)
            left += 1
            right += 1
        return max(arr)
