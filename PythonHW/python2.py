a = {}

a["이름"] = "이소정"
a["나이"] = "24살"
a["학번"] = "2018"
a["학과"] = "정치외교학과"
a["생일"] = "xxxxxx"

print(a)
print(len(a))
print()

del a["이름"] 
del a["나이"]
del a["학번"] 
del a["학과"]
del a["생일"] 

print(a)
print(len(a))
print()

a = dict(이름 = "이소정", 나이 = "24살", 학번 = "2018", 학과 = "정치외교학과")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))
