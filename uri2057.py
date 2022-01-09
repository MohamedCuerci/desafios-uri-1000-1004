
s, t, f = input().split()

s = int(s)
t = int(t)
f = int(f)

total = s + t + f

if total >= 24:
    print(total - 24)
elif total < 0:
    print(total + 24)
else:
    print(total)
