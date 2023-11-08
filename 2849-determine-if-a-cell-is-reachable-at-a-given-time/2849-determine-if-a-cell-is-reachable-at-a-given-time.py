class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        # calculating the horizontal and vertical distances between the starting cell (sx, sy) and 
        # the target cell (fx, fy) by taking the absolute differences of their x and y coordinates, respectively.
        horizontal_distance = abs(sx - fx)
        vertical_distance = abs(sy - fy)
        
        #  initialize a variable minimum_time to None, which I will use to
        #  determine the minimum time required to reach the target cell.
        minimum_time = None
        
        # comparing the horizontal and vertical distances and set minimum_time to the larger of the two distances. 
        # This is because I can either move horizontally or vertically, and I am considering the longer distance
        # as the minimum time required.
        if horizontal_distance > vertical_distance : 
            minimum_time = horizontal_distance
        else : 
            minimum_time = vertical_distance
            
        # If the minimum time is zero (meaning the starting and target cells are the same) and the time limit is 1,
        # then return False because I can't move to the same cell in one second. This is a special case to handle.
        if minimum_time == 0 and t==1:
            return False

        # check if the given time t is greater than or equal to the calculated minimum_time. 
        # If it is, then return True, indicating that it's possible to reach the target cell within the given time.
        # Otherwise,  return False to indicate that it's not possible.
        if t >= minimum_time : 
            return True
        else : 
            return False
            