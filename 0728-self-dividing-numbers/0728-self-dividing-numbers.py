class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        for num in range(left, right+1):
            num_str = str(num)
            if "0" in num_str:
                continue
            else:
                for digit in num_str:
                    if num%int(digit) != 0:
                        break
                else:
                    self_dividing_nums.append(num)

        return self_dividing_nums

        