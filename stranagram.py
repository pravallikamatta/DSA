wrd1=input("enter 1st:").lower()
wrd2=input("enter 2nd:").lower()

if sorted(wrd1)==sorted(wrd2):
    print("anagram")
else:
    print(wrd1,"and are not anagram", wrd2)    

## or if  Counter(s1) == Counter(s2):