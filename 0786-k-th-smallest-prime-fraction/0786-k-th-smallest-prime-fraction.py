class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # empty list to store fractions
        fractions = []
        
        # two pointers for iterating through the array
        start, end = 0, len(arr)-1
        
        # Loop until the start pointer reaches the second-to-last element
        while start <= len(arr)-2:

            # If the end pointer reaches the same position as the start pointer,
            # reset the end pointer to the end of the array and increment the start pointer
            if end == start:
                end = len(arr)-1
                start += 1
                
            else:
                # Calculate the fraction and append it to the list along with the numerator and denominator
                fractions.append( [arr[start]/arr[end], arr[start], arr[end]] )
                
                # Decrement the end pointer
                end -= 1
                
        # Sort the list of fractions
        fractions.sort()
       
        # Return the numerator and denominator of the kth smallest fraction
        return fractions[k-1][1:]
