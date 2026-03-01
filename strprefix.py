str = ["pravu", "prabu"]

first = str[0]
second = str[1]
str1=[]
for i in range(min(len(first), len(second))):
        if first[i] == second[i]:
       
         str1.append(first[i])
        else:
         break
print("".join(str1))