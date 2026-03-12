s = "([])"

stack = []

pairs = {')':'(', ']':'[', '}':'{'}

for char in s:
    if char in pairs.values():
        stack.append(char)
    else:
        if stack and stack[-1] == pairs[char]:
            stack.pop()
        else:
            print(False)
            break
else:
    print(len(stack) == 0)