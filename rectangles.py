__author__ = 'january'

print("sdf")
print('sdfdfs')

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))


parents, babies = (1, 1)
while babies < 1000:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)