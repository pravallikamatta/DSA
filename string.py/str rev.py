str = "pravallika"

strev= str[::-1]

print(strev)
#or

s = "hello"
s = list(s)

l = 0
r = len(s) - 1

while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1

print("".join(s))