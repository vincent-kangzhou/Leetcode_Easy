import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            large=stones[-1]
            small=stones[-2]
            diff=large-small
            stones.pop()
            stones.pop()
            if diff!=0:
                l=bisect.bisect_left(stones,diff)
                stones.insert(l,diff)

        return stones[0] if len(stones)==1 else 0
        
        
        
        
import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_index = 0
            second_max_index = 0
            ol = sorted(stones)
            for i in range(len(stones)):
                if ol[-1] == stones[i]:
                    max_index = i
                elif ol[-2] == stones[i] and max_index != i:
                    second_max_index = i
            if stones[max_index] == stones[second_max_index]:
                if max_index > second_max_index:
                    del stones[max_index]
                    del stones[second_max_index]
            else:
                stones[max_index] -= stones[second_max_index]
                del stones[second_max_index]
            #print stones
        return 0 if len(stones) == 0 else stones[0]
        
        
        
        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x : -x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, -abs(x - y))
        return 0 if not stones else -stones[0]
