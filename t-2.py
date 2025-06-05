a = 'indivisibility'
dc = {}
for vr in a:
    dc[vr] = a.count(vr)
res = dict(sorted(dc.items(), key=lambda item: item[1], reverse=True))
# dict comprehension
res = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1], reverse=True)}

resm = max(res.values())

max_itm = [k for k, v in res.items() if v == resm]

for k, v in res.items():
    if v==resm:
        print(k,v)


