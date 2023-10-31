class Solution:
  # The class "Solution" is defined, indicating that this code might be a part of a solution to some problem.
  # It has a method called "findArray" which takes a list of integers called "pref" and returns a list of integers.

  def findArray(self, pref: List[int]) -> List[int]:
    # This is the method "findArray" that takes a list of integers "pref" as input and returns a list of integers.
    
    # Create a list called "ans" with the same length as the input list "pref" and initialize all elements to 0.
    ans = [0] * len(pref)

    # Set the first element of the "ans" list to be the same as the first element of the "pref" list.
    ans[0] = pref[0]

    # Iterate through the rest of the elements in the "pref" list.
    for i in range(1, len(ans)):
      # Calculate the value for each element in the "ans" list by performing a bitwise XOR (^) operation
      # between the current element in the "pref" list and the previous element in the "pref" list.
      ans[i] = pref[i] ^ pref[i - 1]

    # Return the resulting "ans" list, which contains the calculated values.
    return ans
