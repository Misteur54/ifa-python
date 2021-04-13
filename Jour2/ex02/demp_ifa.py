#Qu'est ce qu'un dict

dict = {}
dict["ecole"] = 'IFA'

print(dict)
dict_test = {'ecole': 'IFA'}
print(dict_test)

#pas d'ordre en particularité



dict_test['ecole'] = "fac"
print(dict_test)

#dans un cas réel
list_tmp = ["34", "186", "elian"]
#problème on ne sait pas l'ordre /  à quoi ça vaut
# avec un dict

dict_tmp = {"age": 34, "taille": 186, "name": "elian"}

print(dict_tmp)

print(dict_tmp["age"])


for key in dict_tmp:
    print(key, dict_tmp[key])


for key in dict_tmp.keys():
    print(key)


for value in dict_tmp.values():
    print(value)


for k,v in dict_tmp.items():
    print(k, v)



#comment savoir si une clé existe


if 'papa' in dict_tmp:
    print('papa existe')
