class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        day_count = 0

        for i in range(0, len(hours)):
            for j in range(i+1, len(hours)):

                total_hours = hours[i] + hours[j]

                if total_hours % 24 == 0:
                    day_count += 1
                    
        return day_count
        