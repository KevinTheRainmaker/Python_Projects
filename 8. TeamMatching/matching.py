target =  {'gender':'M', 'age':21, 'smoking':'Y', 'cold':1}
members = [{'gender':'M', 'age':22, 'smoking':'Y', 'cold':0},{'gender':'F', 'age':21, 'smoking':'Y', 'cold':1},{'gender':'M', 'age':21, 'smoking':'Y', 'cold':1}]

candidates = []
for i in range(len(members)):
    if target['gender'] == members[i]['gender']:
        candidates.append(members[i])
print(candidates)

rate = [1,2,4,3]

