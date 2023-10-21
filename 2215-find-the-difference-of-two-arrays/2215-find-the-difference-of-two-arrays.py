class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # Create a list `answer` to store the differences found in `nums1` and `nums2`.
        # The first element (answer[0]) will store the elements in `nums1` that are not in `nums2`,
        # and the second element (answer[1]) will store the elements in `nums2` that are not in `nums1`.
        answer = [ [], [] ]
        
        # Iterate through each number in nums1.
        for number in nums1:
            # Check if the current number is not in nums2 and has not been added to answer[0] already.
            if number not in nums2 and number not in answer[0]:
                # If the number is not in nums2 and hasn't been added to answer[0], add it to answer[0].
                answer[0].append(number)

        # Iterate through each number in nums2.
        for number in nums2:
            # Check if the current number is not in nums1 and has not been added to answer[1] already.
            if number not in nums1 and number not in answer[1]:
                # If the number is not in nums1 and hasn't been added to answer[1], add it to answer[1].
                answer[1].append(number)

        # Return the `answer` list containing the differences.
        return answer
