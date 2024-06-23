class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        start, end = 0, len(nums)-1
        min_average = math.inf

        while start <= end :
            avg = (nums[start] + nums[end]) / 2
            min_average = min(avg, min_average)
            start += 1
            end -= 1

        return min_average
