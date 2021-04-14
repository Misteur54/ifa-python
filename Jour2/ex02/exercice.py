import sys


def read_dict(information):
    if type(information) is dict and len(information):
        tmp = 0
        i = 0
        for value in information.values():
            tmp += value
            i += 1
        return tmp / i
    else:
        print('ceci n est pas un dic', file=sys.stderr)


def read_dict_upper(information):
    if type(information) is dict and len(information):
        tmp = {'value': 0, "key": []}

        for key, value in information.items():
            if tmp.get('value') <= value:
                if tmp.get('value') == value:
                    tmp['key'].append(key)
                else:
                    tmp['key'] = []
                    tmp['key'].append(key)
                    tmp['value'] = value
        return tmp
    else:
        print('ceci n est pas un dic', file=sys.stderr)


def read_fake_cvs(path, mode):
    with open(path, mode) as file:
        data = {}

        for line in file:
            line = line.rstrip()
            line = line.split(';')

            if len(line) == 3:
                if line[0] in data:
                    print(f'Il existe déjà une personne avec cet identité {line[0]}, pour {line[1]} {line[2]}', file=sys.stderr)
                data[line[0]] = f"{line[1]} {line[2]}"
            else:
                print('Il manque des informations', file=sys.stderr)
        return data


def read_variadic(*items_dict):
    data = {}

    for item in items_dict:
        if type(item) is dict and len(item):
            for key, value in item.items():
                # print(key, value)
                if key in data:
                    print(key)
                    data[key].append(value)
                else:
                    data[key] = [value]
    print(data)
