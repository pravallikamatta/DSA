strg = input("enter a string:")
 
for i in strg:
   if 'a' <= i <= 'z':
      print(i.upper(), end="")
   else:
      print(i.lower(), end="")