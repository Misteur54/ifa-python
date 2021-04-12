import sys
# #utilisation de la fonction print

print('Ici on découvre le formatage de la fonction print')

print('ici', 'la', '3', '4', sep='  ', end='c est la fin\n', file=sys.stdout)

print('ici', 'la', '3', '4', sep='  ', end='c est la fin\n', file=sys.stderr)


name = "olivier"

name = "mon prénom est %s et j'ai %d ans" % ("Olivier", 34)

print(name)

name = "mon nom prénom est {1} et j'ai {0} ans".format("olivier", 34)
print(name)

#
# #la fonction print prend des arguments variadiques
# print('papa', 'maman', 'IFA')
# #de base le séparateur sont des espaces
#
# print('papa', 'maman', 'IFA', sep='/')
#
# #la fin d'un print comme vous le savez se termine par un \n en python nous pouvons changer ça facilement
#
# print('PAPA', end='IFAERER')
#
# #print sur la sortie d'erreur
# print('PAPA', file=sys.stderr)
#
# #print sur la sortie normale
# print('PAPA', file=sys.stdout)
#
# #utilisation de la methode % format
#
# print('un string c est %s, un int c est %d' % ("papa", 120))
#
#
# #utilisation de la methode .format
#
#
# x = 'papa'
# y = 1
#
# print('ici c est le test nous avons qu {} {}'.format(x, y))
#
#
#


# #Petit exercice Je veux une ligne avec print en utilisation la méthode .format, sep , end et file avec différent type de variable
# # est aussi en utilisant des ' dans la chaine de caractère
#

name = "PAPA"
age = 34
job = "IT"
print("je m'appelle %s j'ai %d je travaille dans %s" % (name, age, job), 'test separateur ',sep = ' papa ', end="\n\n", file=sys.stdout)


# #Petit exercice Je veux une ligne avec print en utilisation la méthode %format, sep , end et file avec différent type de variable
# # est aussi en utilisant des ' dans la chaine de caractère
print("je m'appelle {0} j'ai {1} je travaille dans {2}".format(name, age, job), 'test separateur ',sep = ' papa ', end="\n\n", file=sys.stdout)

