from sortedcontainers import SortedSet

class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        # Dictionary to store cuisines and their corresponding sorted sets of (rating, food)
        self.cuisines_food = defaultdict(SortedSet) # cuisine -> (rating, food)

        # Dictionary to map foods to their respective cuisines
        self.cuisines = {} #food -> cuisine

        # Dictionary to store ratings for each food
        self.ratings = {} #food -> rating

        # Iterate through the input lists to populate the dictionaries
        for i in range (len (foods)):

            # Add the tuple (-rating, food) to the sorted set for the corresponding cuisine
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods [i]))

            # Map food to its cuisine
            self.cuisines[foods[i]] = cuisines[i]

            # Map food to its rating
            self.ratings[foods[i]] = ratings[i]


    def changeRating (self, food: str, newRating: int) -> None:

        # Get the cuisine and current rating of the food
        c = self.cuisines[food]
        r = self.ratings[food]

        # Remove the tuple (-current_rating, food) from the sorted set for the cuisine
        self.cuisines_food[c].remove((-r, food))

        # Add the new rating and food to the sorted set for the cuisine
        self.cuisines_food[c].add((-newRating, food))

        # Update the rating of the food in the ratings dictionary
        self.ratings[food] = newRating


    def highestRated (self, cuisine: str) -> str:

        # Access the first element (highest-rated) from the sorted set for the given cuisine
        return self.cuisines_food[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)