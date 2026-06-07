class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #creates hashmap of counts in tasks
        count = Counter(tasks)

        #create a max heap to track the most freq counter to use
        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) #decrements freq

                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        