#La façon simple

content = open('test.txt', 'r')

lines = content.readlines()

for line in lines:
    print(line)

content.close()

#meilleure façon

with open('test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)


with open('test.txt', 'r') as file:
    lines = file.read()
    print(lines)


#prend en compte ligne par ligne

print('test')
with open('test.txt', 'r') as file:
    lines = file.readline()
    while lines != "":
        print(lines)
        lines = file.readline()
    print(lines)


#python nous facilite la vie

with open('test.txt', 'r') as file:
    for line in file:
        print(line)


test =  ['test', 'lol', 'papap']
with open('test_demo.txt', 'w') as file:
    for t in test:
        file.write(t)



#nous on veut avec un bon format avec le\n

with open('test_demo_good.txt', 'w') as file:
    for t in test:
        file.write(f'{t}\n')



#ouvrir deux fichiers

with open('test.txt', 'r') as file_one, open('test_demo.txt', 'w') as file_two:
    for line in file_one:
        file_two.write(f'+ {line}')


#format et respect

import random

with open('moyenne.txt', 'w') as file:
    for i in range(0, 1000):
        file.write(f"{str(random.randint(0, 20))}\n")
