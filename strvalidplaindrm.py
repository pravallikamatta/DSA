s = "A man, a plan, a canal: Panama"

cleaned = ""

for ch in s:
    if ch.isalnum():     # keep only letters and numbers
        cleaned += ch.lower()

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)