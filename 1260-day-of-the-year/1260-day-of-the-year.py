class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")
        total_days = int(date[2])

        for i in range(1, int(date[1])):
            if i == 2:
                if (int(date[0]) % 400 == 0) or (int(date[0]) % 4 == 0 and int(date[0]) % 100 != 0):
                    total_days += 29
                else:
                    total_days += 28
            elif i in set([1, 3, 5, 7, 8, 10, 12]):
                total_days += 31
            else:
                total_days += 30


        return total_days



        