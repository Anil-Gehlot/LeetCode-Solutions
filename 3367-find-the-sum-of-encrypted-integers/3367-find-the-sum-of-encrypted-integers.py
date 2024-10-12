class Solution:
    def encrypt(self, nums):
        num_length = len(str(nums))

        max_digit = 0
        for i in range(4):
            if nums:
                max_digit = max(max_digit, nums%10)
                nums //= 10
        return int("1" * num_length) * max_digit
            

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += self.encrypt(num)
        return total_sum
        