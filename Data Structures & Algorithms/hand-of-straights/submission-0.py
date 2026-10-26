class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        countMap = Counter(hand)
        minHeap = hand
        heapq.heapify(minHeap)
        while minHeap:
            element = heapq.heappop(minHeap)
            if countMap[element] == 0:
                continue
            countMap[element] -= 1
            for i in range(groupSize - 1):
                element += 1
                if countMap[element] > 0:
                    countMap[element] -= 1
                else:
                    return False
        return True
