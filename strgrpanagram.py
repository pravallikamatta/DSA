#Anagrams = Words that have the same letters but in different order.
from collections import defaultdict
str = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
# |This creates a dictionary for later
for i in str:
    key = "".join(sorted(i))
    
    groups[key].append(i)
print(list(groups.values())) 
 
    
