class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        book = {}

        for i, n in enumerate(numbers):
            diff = target - n

            if diff in book:
                return [book[diff], i + 1]
            
            book[n] = i + 1
        return []
            
        