class Solution:
    def isPalindrome(self, x: int) -> bool:
        index = str(x)
        if x < 0:
            return False
        else:
            for i in range(len(index)):
                if index[i] != index[len(index)-1-i]:
                    return False
            return True
        