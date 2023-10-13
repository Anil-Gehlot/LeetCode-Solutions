class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Add 0 at the end to handle reaching the top of the stairs.
        cost.append(0)

        # Iterate through the cost list starting from the third element.
        for i in range(2, len(cost)):
            # Update the current cost by adding the minimum of the previous two costs.
            cost[i] += min(cost[i - 1], cost[i - 2])

        # Return the cost required to reach the top of the stairs.
        return cost[-1]

        