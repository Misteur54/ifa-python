# déclaration de list

list_one = []

print(type(list_one))

#réasignation de la valeur en python
#mélange de variable
list_one = ['1212', 10, 35]

print(list_one)

list_two = ['1245', 10, 34]

list_three = list_one + list_two

print(list_three)

list_one.append(list_two)
list_one.append("variable")
print(list_one)


list_four = list_one + list_two
print(list_four)


#indiçage négatif

print(list_one[0])
print(list_one[-1])

print(list_one[0:2])
#ajout d'un pas

print(list_one[0:6:2])

list_range = list(range(10))
print(list_range)

#ajout d'un interval

list_range = list(range(3, 20))
print(list_range)

#ajout d'un step

list_range = list(range(0, 1000, 200))

print(list_range)


