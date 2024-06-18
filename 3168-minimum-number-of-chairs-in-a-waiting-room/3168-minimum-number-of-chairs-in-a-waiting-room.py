class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chair = 0

        current_chair = 0
        for event in s:
            if event == "E":
                current_chair += 1
                max_chair = max(current_chair, max_chair)
            else:
                current_chair -= 1
            
        return max_chair

        