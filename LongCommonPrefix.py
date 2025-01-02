class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        shortest_string = min(strs, key=len)

        strs.remove(shortest_string)

        print(strs)
        for i in range(len(shortest_string)):
            for word in strs:
                if word[i] != shortest_string[i]:
                    return ans  
            ans += shortest_string[i]

        return ans
        