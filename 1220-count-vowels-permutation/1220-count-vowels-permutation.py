class Solution:
  def countVowelPermutation(self, n: int) -> int:
    # Define a modulus value to prevent integer overflow
    kMod = 1_000_000_007
    # Initialize a dictionary to store the counts for each vowel
    dp = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

    # Iterate n-1 times to calculate permutations of length n
    for _ in range(n - 1):
      # Calculate new permutation counts based on the specified rules
      newDp = {'a': dp['e'] + dp['i'] + dp['u'],
               'e': dp['a'] + dp['i'],
               'i': dp['e'] + dp['o'],
               'o': dp['i'],
               'u': dp['i'] + dp['o']}
      # Update the dp dictionary with the new counts
      dp = newDp

    # Return the sum of all counts modulo kMod
    return sum(dp.values()) % kMod
