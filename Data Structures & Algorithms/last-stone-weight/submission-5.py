class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #create a max heap to get the heaviest stone 
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        #extract the two heaviest stones
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            diff = -(stone1 - stone2)

            if diff:
                heapq.heappush(heap, -diff)
        
        if heap:
            return -heap[0]
        
        return 0
        