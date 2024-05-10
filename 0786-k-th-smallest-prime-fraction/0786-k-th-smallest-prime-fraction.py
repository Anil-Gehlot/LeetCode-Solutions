class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        fractions = []
        start, end = 0, len(arr)-1
        
        while start <= len(arr)-2:

            if end == start:
                end = len(arr)-1
                start += 1
            else:
                fractions.append( [arr[start]/arr[end], arr[start], arr[end]] )
                end -= 1
                
        fractions.sort()
       
        return fractions[k-1][1:]
        