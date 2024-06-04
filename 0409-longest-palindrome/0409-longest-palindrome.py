class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        s_counter = Counter(s)
        
        odd_frequency = 0
        longest_palindrome_length = 0
        
        for val in s_counter.values():
            if val % 2 == 0:
                longest_palindrome_length += val
            else:
                longest_palindrome_length += val - 1
                odd_frequency += 1
        
        if odd_frequency:
            return longest_palindrome_length + 1
        else:
            return longest_palindrome_length