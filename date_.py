from datetime import datetime, timedelta
s = datetime(1984, 9, 30)
e = datetime(2009, 9, 7)


w = 0


c_d = s
while c_d <= e:
    if c_d.weekday()==2:
        w += 1
    c_d += timedelta(days=1)

print(w)