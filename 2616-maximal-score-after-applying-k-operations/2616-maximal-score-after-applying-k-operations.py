class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
            
        # using heapify to convert list into heap
        heapq.heapify(nums)

        score = 0
        for i in range(k):
            # pop the largest element and add it to score
            max_element = -heapq.heappop(nums)
            score += max_element

            # push the ceild value into the heap
            heapq.heappush(nums, -(ceil(max_element/3)) )

        return score
        