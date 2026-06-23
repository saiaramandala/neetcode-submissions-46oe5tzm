class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            store[sorted_s].append(s)
        
        return list(store.values())

        