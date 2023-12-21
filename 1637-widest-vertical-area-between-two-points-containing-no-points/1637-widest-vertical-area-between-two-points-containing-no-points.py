class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        # Extract X-coordinates from the points
        x_coordinates = [point[0] for point in points]

        # Sort the X-coordinates in ascending order
        x_coordinates.sort()

        # Initialize the variable to store the widest vertical area
        widest_vertical_area = 0

        # Iterate through the sorted X-coordinates to find the maximum width
        for index in range(len(x_coordinates) - 1):
            
            # Calculate the difference between consecutive X-coordinates
            current_width = x_coordinates[index + 1] - x_coordinates[index]

            # Update the widest vertical area if the current width is greater
            if current_width > widest_vertical_area:
                widest_vertical_area = current_width

        # Return the maximum width of the vertical area
        return widest_vertical_area
