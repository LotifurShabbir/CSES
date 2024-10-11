# cook your dish here
s = input()

ans = 1
l, r = 0, 0
while r < len(s):
    if s[l] == s[r]:
        r += 1
        ans = max(ans, r - l)
    elif s[l] != s[r]:
        ans = max(ans, r - l)
        l += 1


print(ans)