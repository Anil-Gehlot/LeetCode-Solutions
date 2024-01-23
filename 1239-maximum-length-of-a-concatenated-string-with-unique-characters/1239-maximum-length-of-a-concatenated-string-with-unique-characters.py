class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def is_unique(sub):
            return len(sub) == len(set(sub))

        def backtrack(start, current):
            nonlocal max_length

            if is_unique(current):
                max_length = max(max_length, len(current))

            for i in range(start, len(arr)):
                new_subsequence = current + arr[i]
                backtrack(i + 1, new_subsequence)

        max_length = 0
        backtrack(0, "")
        return max_length