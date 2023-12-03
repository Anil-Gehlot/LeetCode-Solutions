class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        

        # Initialize total time to zero
        total_time = 0

        # Iterate array points till the second last cordinates
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            # Calculate horizontal and vertical distances
            horizontal_distance = abs(x2 - x1)
            vertical_distance = abs(y2 - y1)

            # Add the maximum of horizontal and vertical distances to total time
            total_time += max(horizontal_distance, vertical_distance)

        # Return the total time to visit all points
        return total_time