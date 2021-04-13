import exercice


data = {'Elian': 10, 'Kevin': 18, 'Momo': 20, 'Olivier': 19, 'Thibaud': 18, 'Fabrice': 7}

print(exercice.read_dict(data))

print(exercice.read_dict_upper(data))
# try:
#     print(exercice.read_dict({}))
# except ZeroDivisionError:
#     print('je suis dans l exception')