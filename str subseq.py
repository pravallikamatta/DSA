#logic pass i from 1 pass j frm 2 if 10 j0 same J++ IF NO I AND J++
#then if i over scaning done
s = "ace"
t = "abcde"

i = 0
j = 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1

if i == len(s):
    print("True")
else:
    print("False")