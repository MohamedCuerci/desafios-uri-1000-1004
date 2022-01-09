

f, b, m = input().split()

f = int(f)
b = int(b)
m = int(m)

tf, tb, tm = input().split()

tf = int(tf)
tb = int(tb)
tm = int(tm)

verdadeiroTotalkkkkk = 0

total = tf - f 
if total > 0:
    verdadeiroTotalkkkkk += total

total1 = tb - b
if total1 > 0:
    verdadeiroTotalkkkkk += total1

total2 = tm - m
if total2 > 0:
    verdadeiroTotalkkkkk += total2

print(verdadeiroTotalkkkkk)