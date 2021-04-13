def compute():
    print('je suis dans le compute')


def compute_several(name, age):
    print(f'j ai {age}, je suis {name}')


#même si aucune variable est donnée, on dit que name et age prendront la valeur de base elian et 34
def compute_default(name='Elian', age='34'):
    print(f'j ai {age} et je suis {name}')



#ici c'est pour avoir un nombre de variable non défini
def compute_variadic(*all_items):
    for i in all_items:
        print(i)


