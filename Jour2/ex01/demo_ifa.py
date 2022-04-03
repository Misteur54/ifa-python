#comment importer

import random

print(random.randint(0, 10))

#utilisation

from random import *

#cette commande n'est pas opti
#mais si vous voulez importer juste une partie de la lib faite ceci

from random import randint

#import partiel



#Module important pour passer des paramètres

import sys

print(sys.argv)

if len(sys.argv) != 2:
    sys.exit("Error: il faut un argument")

for i in sys.argv:
    print(i)