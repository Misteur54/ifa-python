tmp = ['ifa', 'elian', 'davy', 'lol', 'ifa']
#
# for name in tmp:
#     print(name)
#

for i in range(0, len(tmp), 1):
    print(tmp[i], f"i = {i}")
    # print(name)

#
# i = 0
# len_tmp = len(tmp)
#
# while i != len_tmp:
#     print(tmp[i])
#     i += 1


print(tmp.index('ifa'))



week = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']


for day in week[0:5]:
    print(day)

for day in range(0, 5, 1):
    print(week[day])


for day in week[5:7]:
    print(day)



for nb in range(1, 11, 1):
    print(nb, end='')


list_impaire = []

for nb in range(1, 100, 2):
    list_impaire.append(nb)
#
for nb in range(0, 100, 1):
    if nb % 2 != 0:
        list_impaire.append(nb)

print(list_impaire, 'deux')

list_pair = []

for i in list_impaire:
    list_pair.append(i + 1)

print(list_pair)


for i in range(1, 15, 1):
    print('*' * i)

for i in range(15, 0, -1):
    print('*' * i)
