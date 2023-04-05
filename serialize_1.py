import pickle, json
d = dict(name='Bob', age=20, score=88)
s = pickle.dumps(d)

p = pickle.loads(s)
print(p)

j = json.dumps(d)
print(j)
o = json.loads(j)
print(o)