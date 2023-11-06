
class SeatManager:
    def __init__(self, n: int):
        # Initialize the SeatManager with 'n' seats.
        # Create a min-heap with seat numbers from 1 to 'n'.
        self.minHeap = [i + 1 for i in range(n)]

    def reserve(self) -> int:
        # Reserve and return the smallest available seat.
        return heapq.heappop(self.minHeap)

    def unreserve(self, seatNumber: int) -> None:
        # Return the unreserved seat back to the available seats.
        heapq.heappush(self.minHeap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)