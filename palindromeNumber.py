class Solution(object):
    def isPalindrome(self, x):
        if x< 0 :
            return False
        rev = int(str(x)[::-1])
        return True if rev == x else False
    
solution_instance = Solution()
x = 121
result = solution_instance.isPalindrome(-121)
print(result)
          