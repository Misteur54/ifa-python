import sys
#utilisation de la fonction print

print('Ici on découvre le formatage de la fonction print')

#la fonction print prend des arguments variadiques
print('papa', 'maman', 'IFA')
#de base le séparateur sont des espaces

print('papa', 'maman', 'IFA', sep='/')

#la fin d'un print comme vous le savez se termine par un \n en python nous pouvons changer ça facilement

print('PAPA', end='IFAERER')

#print sur la sortie d'erreur
print('PAPA', file=sys.stderr)

#print sur la sortie normale
print('PAPA', file=sys.stdout)

#utilisation de la methode % format

print('un string c est %s, un int c est %d' % ("papa", 120))


#utilisation de la methode .format


x = 'papa'
y = 1

print('ici c est le test nous avons qu {} {}'.format(x, y))

#Petit exercice Je veux une ligne avec print en utilisation la méthode .format, sep , end et file avec différent type de variable
# est aussi en utilisant des ' dans la chaine de caractère

#Petit exercice Je veux une ligne avec print en utilisation la méthode %format, sep , end et file avec différent type de variable
# est aussi en utilisant des ' dans la chaine de caractère

#Pour finir afficher une phrase truc en combinant le .format et le %format avec toutes les spécificités dites avant

#25 minutes pour faire tout ça
