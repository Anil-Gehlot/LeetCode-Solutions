class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # Count occurrences of each number in the input list
        nums_counter = collections.Counter(nums)

        # Find the maximum occurrence to determine the number of rows in the result matrix
        max_occurrence = max(nums_counter.values())

        # Initialize a 2D array with empty lists for each row
        result_matrix = [[] for _ in range(max_occurrence)]

        # Populate the result matrix by appending each number based on its occurrence
        for num, occurrence in nums_counter.items():
            for index in range(occurrence):
                result_matrix[index].append(num)

        return result_matrix