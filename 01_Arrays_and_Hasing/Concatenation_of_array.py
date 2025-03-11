class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        store = []
        for i in range(2):
            for n in nums:
                store.append(n)

        return store

        