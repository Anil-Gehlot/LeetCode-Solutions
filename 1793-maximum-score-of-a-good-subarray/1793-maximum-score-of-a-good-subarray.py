class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    # Get the length of the 'nums' list
    n = len(nums)

    # Initialize the 'ans' variable with the value at index 'k'
    ans = nums[k]

    # Initialize 'mini' variable with the value at index 'k'
    mini = nums[k]

    # Initialize pointers 'i' and 'j' to 'k'
    i = k
    j = k

    # Greedily expand the window and decrease 'mini' as slowly as possible (ASAP).
    while i > 0 or j < n - 1:
      # If 'i' reaches the beginning of the list, expand to the right
      if i == 0:
        j += 1
      # If 'j' reaches the end of the list, expand to the left
      elif j == n - 1:
        i -= 1
      # Compare the elements to the left and right, and expand towards the larger one
      elif nums[i - 1] < nums[j + 1]:
        j += 1
      else:
        i -= 1
      
      # Update 'mini' to the minimum value in the current window
      mini = min(mini, nums[i], nums[j])

      # Calculate the current score by multiplying 'mini' with the window's width
      ans = max(ans, mini * (j - i + 1))

    # Return the maximum score found
    return ans
