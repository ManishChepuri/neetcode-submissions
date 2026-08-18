class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int) # num: count

        for num in nums:
            d[num] += 1
        
        output = []
        for i in range(k):
            output.append(max(d, key=d.get))
            d.pop(output[i])

        return output
        
