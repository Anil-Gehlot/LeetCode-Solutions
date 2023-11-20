
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
    

        # Calculating prefix sum of  travel time between houses
        for i in range(1, len(travel)):
            travel[i] = travel[i] + travel[i-1]
            
            
        # Initialize variables to keep track of the time for each type of garbage
        metal_time = 0
        paper_time = 0
        glass_time = 0

        # Initialize variables to store the last occurrence of each garbage type
        last_paper_house = None
        last_glass_house = None
        last_metal_house = None

        # Initialize a count to keep track of the total number of garbage units
        total_garbage_count = 0 

        # Iterate through each house's garbage
        for house_index in range(len(garbage)):
            
        
            # Update the last occurrence of each garbage type
            
            if 'P' in garbage[house_index]:
                last_paper_house = house_index
            
            if 'G' in garbage[house_index]:
                last_glass_house = house_index
            
            if 'M' in garbage[house_index]:
                last_metal_house = house_index
                
            
                
            # Count the total number of garbage units in the current house
            total_garbage_count += len(garbage[house_index])
            

        # Initialize total travel time as the total number of garbage units
        total_travel_time = total_garbage_count
            
        # Update total travel time considering the travel time between the last occurrence of each garbage type
        if last_glass_house is not None and last_glass_house != 0:
            total_travel_time += travel[last_glass_house - 1]
    
        if last_paper_house is not None and last_paper_house != 0:
            total_travel_time += travel[last_paper_house - 1]
        
        if last_metal_house is not None and last_metal_house != 0:
            total_travel_time += travel[last_metal_house - 1]

        # Print and return the total travel time
        print(total_travel_time)
        return total_travel_time
