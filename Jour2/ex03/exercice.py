import own_exercice
import os

own_exercice.writer('./own_module.txt', 'w', [10, 15, 14, 10, 10,1034,343443, 'rue nicolas chenin'])

# print(own_exercice.reader('./own_module.txt'))

# print(own_exercice.check_nb('1234er5'))

tmp = own_exercice.counter(os.getcwd())
print(tmp)
print(type(tmp))
