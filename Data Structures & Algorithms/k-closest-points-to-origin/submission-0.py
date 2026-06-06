class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        #create max heap and add the distances
        for x, y in points:
            distance = -(x*x + y*y)

            heapq.heappush(heap, (distance, x, y))

            #remove the largest value of distance
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for distance, x, y in heap:
            res.append([x, y])
        
        return res
        

            

        