class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # Base case: The first row always starts with 0
        if n == 1:
            return 0

        # Calculate the parent symbol of the Kth symbol in the current row
        # by moving up to the previous row (n - 1)
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # Check whether K is even or odd
        if k % 2 == 0:
            # If k is even, the symbol is the complement of the parent symbol
            return 1 - parent
        else:
            # If k is odd, the symbol is the same as the parent symbol
            return parent
