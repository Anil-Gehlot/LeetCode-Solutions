class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0

        for i in range(len(seats)):
            current_move = seats[i] - students[i]
            moves += abs(current_move)
        return moves