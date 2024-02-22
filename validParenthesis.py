class Solution(object):
  
    def isValid(self, s):
      open_brackets = ['(', '{', '[']
      closing_brackets = [')', '}', ']']
      final = []
      
      for char in s:
          if char in open_brackets:
              final.append(char)
          elif char in closing_brackets:
              if not final:
                  print(False)
                  return
              if open_brackets.index(final[-1]) != closing_brackets.index(char):
                  print(False)
                  return
              final.pop()
      
      print(not final)




solution_instance = Solution()
solution_instance.isValid('[]')

      
            
        
        
        