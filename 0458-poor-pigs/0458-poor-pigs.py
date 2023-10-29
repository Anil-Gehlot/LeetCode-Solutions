class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate the number of states per test.
        states = minutesToTest // minutesToDie + 1
        
        # Calculate the number of pigs needed using logarithms.
        result = round(math.log(buckets) / math.log(states), 6)
        
        # Round up the result to the nearest integer.
        return math.ceil(result)
