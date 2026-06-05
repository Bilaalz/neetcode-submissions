class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.length = k
        self.heap = nums

        heapq.heapify(self.heap)


        #creating heap of size k so heap[0] is the kth largest element in a stream
        while len(self.heap) > self.length:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.length:
            heapq.heappop(self.heap)
        
        return self.heap[0]

        
