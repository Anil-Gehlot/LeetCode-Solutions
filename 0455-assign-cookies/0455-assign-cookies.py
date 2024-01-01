class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()

        # Initialize pointers for greed factors and cookie sizes
        i, j = 0, 0
        content_children = 0

        # Iterate through the lists
        while i < len(g) and j < len(s):
            
            # If the current cookie size is greater than or equal to the current child's greed factor
            # Assign the cookie to the child and move both pointers
            if s[j] >= g[i]:
                content_children += 1
                i += 1
                
            # Move to the next cookie size, regardless of whether it satisfies the current child
            j += 1

        return content_children