from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #we are using defaultdict to create a dictionary that will automatically create a new list for each new key
        # defaultdict(list) creates a dictionary where each key maps to a list
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


solution=Solution()
strs = ["act","pots","tops","cat","stop","hat"]
solution.groupAnagrams(strs)
print(solution.groupAnagrams(strs))


# explanation of above code
#step 1- import defaultdict from collections and List from typing - defaultdict is a subclass of dict that returns a default value when a key is not found
#step 2- create a defaultdict of type list called res
#step 3- iterate through each string in the input list
#step 4- sort the string and join it to create a new string called sortedS
#step 5- append the original string to the list in res corresponding to the sorted string
#step 6- return the values of res as a list
