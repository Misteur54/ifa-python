# gestion d'erreur

# nb = input('nb premier')

# try:
#     nb = int(nb)
# except:
#     print('l âge n est pas bon')
# else:
#     print(f"le nombre est {nb}")
# finally:
#     print('Fin du programme')


nb1 = 150
nb2 = input('nb à diviser')

try:
    nb2 = int(nb2)
    print(f'Résultat = {nb1 / nb2}')
except ZeroDivisionError:
    print("Vous ne pouvez pas divisier par 0")

except ValueError:
    print("vous devez entrer un nombre.")

except:
    print("valeur incorrecte")

else:
    print("Bravo, tu as noté un nombre valide")
finally:
    print("Fin du programme")



#creation de notre propre error avec raise



#assert error

