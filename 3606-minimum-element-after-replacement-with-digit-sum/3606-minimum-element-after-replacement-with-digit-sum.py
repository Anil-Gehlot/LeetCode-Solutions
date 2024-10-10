class Solution:
    def sum_of_digits(self, n):
        return sum(int(digit) for digit in str(n))

    def minElement(self, nums: List[int]) -> int:
        transformed_nums = [self.sum_of_digits(num) for num in nums]
        return min(transformed_nums)
        