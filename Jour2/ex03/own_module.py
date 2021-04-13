def bonjour(name="Elian"):
    print(f'Bonjour {name}')


def compute_day(bound_lower=0, bound_upper=7):
    day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    return day[bound_lower : bound_upper]


def write_file(path, mode, informations):
    with open(path, mode) as file:
        for info in informations:
            file.write(f'{info}\n')
# def compute_day(bound_lower, bound_upper):
#     day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
#
#     return day[bound_lower, bound_upper]
#
#
# def bonjour(name="Elian"):
#     print(f"Bonjour {name}")
#
#
# def aurevoir():
#     print('bonne journée!')