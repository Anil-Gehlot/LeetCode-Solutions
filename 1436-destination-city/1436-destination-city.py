class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        starting_cities = set()

        # Iterate through paths and add starting cities to the set
        for path in paths:
            starting_cities.add(path[1])

        # Iterate through paths and remove starting cities from the set
        for path in paths:
            if path[0] in starting_cities:
                starting_cities.remove(path[0])

        # The remaining city in the set is the destination city
        return starting_cities.pop()