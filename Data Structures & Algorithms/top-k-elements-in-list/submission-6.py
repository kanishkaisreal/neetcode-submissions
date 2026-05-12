import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

# alternate way to do this 
        # freq_map = defaultdict(int)
        
        # for num in nums:
        #     freq_map[num] +=1  # this will do the same thing as Counter(nums)

        freq_map = Counter(nums)
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for freq, num in heap:
            result.append(num)

        return result
