class Solution:
    def clearDigits(self, s: str) -> str:
        num_set = {"0", "1","2","3","4","5","6","7","8","9"}
        result = ''


        for char in s:
            if char in num_set:
                result = result[:-1]
            else:
                result += char
        return result


        # num_set = {"0", "1","2","3","4","5","6","7","8","9"}
        # count = 0

        # for char in s:
        #     if char in num_set :
        #         count += 1

        # while count > 0:
        #     for i in range(len(s)):
        #         if s[i] in num_set:
        #             s = s[:i-1] + s[i+1:]
        #             break
        #     count -= 1
        # return s

        