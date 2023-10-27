class Solution:
  def longestPalindrome(self, s: str) -> str:
    # Check if the input string is empty
    if not s:
      return ''

    # Initialize indices to store the start and end of the longest palindrome
    indices = [0, 0]

    # Returns [start, end] indices of the longest palindrome extended from s[i..j]
    def extend(s: str, i: int, j: int) -> Tuple[int, int]:
      while i >= 0 and j < len(s):
        # Check if the characters at both ends match
        if s[i] != s[j]:
          break
        i -= 1
        j += 1
      # Return the indices of the longest palindrome
      return i + 1, j - 1

    # Iterate through the characters of the input string
    for i in range(len(s)):
      # Check for palindromes with odd length (e.g., "aba")
      l1, r1 = extend(s, i, i)
      # Update indices if a longer palindrome is found
      if r1 - l1 > indices[1] - indices[0]:
        indices = l1, r1
      # Check for palindromes with even length (e.g., "abba")
      if i + 1 < len(s) and s[i] == s[i + 1]:
        l2, r2 = extend(s, i, i + 1)
        # Update indices if a longer palindrome is found
        if r2 - l2 > indices[1] - indices[0]:
          indices = l2, r2

    # Return the longest palindrome found in the input string
    return s[indices[0]:indices[1] + 1]
