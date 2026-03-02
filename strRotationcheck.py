strg1= "abcd"
strg2= "cdab"

if len(strg1) == len(strg2) and strg2 in (strg1 + strg1):
    print(True)
else:
    print(False)
