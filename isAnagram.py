from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution -3
        #return sorted(s) == sorted(t)   
    
        #solution -2
        return Counter(s) == Counter(t)  # using collections.Counter to count characters in both strings
    
        ''' 
        sorted_s = ''.join(sorted(s))  # alphabetically sort the string
        sorted_t = ''.join(sorted(t))
        
        if(sorted_s ==sorted_t):  # if the sorted strings are equal, they are anagrams
            return True

        return False
        '''
        
      #solution -1
     
                
        
        
s="car"
t="rac"             
solution=Solution();
print(solution.isAnagram(s,t))


'''
Solution 2 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorted_s = ''.join(sorted(s))
        #sorted_t = ''.join(sorted(t))
        
        if(sorted(s) ==sorted(t)):
            return True

        return False
        
       
s="car"
t="rac"             
solution=Solution();
print(solution.isAnagram(s,t))





        

'''




        