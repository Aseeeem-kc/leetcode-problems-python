class Solution(object):
    def longestCommonPrefix(self, strs):
      if not strs:
        return ""

      prefix = strs[0]
      for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
      return prefix
                      
                    

solution_instance = Solution()
strs = ["flower","flower","flower"]
result = solution_instance.longestCommonPrefix(strs)
print(result)