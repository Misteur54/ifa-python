import exercice


data = {'Elian': 10, 'Kevin': 18, 'Momo': 20, 'Olivier': 19, 'Thibaud': 18, 'Fabrice': 7}
data1 = {'Elian': 11, 'Kevin': 19, 'Momo': 18, 'Olivier': 19, 'Thibaud': 18, 'Fabrice': 7}
data2 = {'Elian': 12, 'Kevin': 20, 'Momo': 16, 'Olivier': 19, 'Thibaud': 18, 'Fabrice': 7}

# print(exercice.read_dict(data))
#
# print(exercice.read_dict_upper(data))
#
#
# print(exercice.read_fake_cvs('./exo_identification', 'r'))
# try:
#     print(exercice.read_dict({}))
# except ZeroDivisionError:
#     print('je suis dans l exception')


print(exercice.read_variadic(data, data1, {}, [], data2))