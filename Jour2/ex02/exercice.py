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
