import os

def writer(path, mode='w', informations=['']):
    with open(path, mode) as file:
        for info in informations:
            file.write(f"{info}\n")


def check_nb(nb):
    return nb.isdigit()


def check_alpha(alpha):
    return alpha.isalpha()


def reader(path, mode='r'):
    if os.path.exists(path) and not os.path.isdir(path):
        with open(path, mode, encoding='utf-8') as file:
            lines = []
            for line in file:
                line = line.rstrip()
                print(line)
                if check_nb(line):
                    lines.append(int(line))
                elif check_alpha(line):
                    lines.append(str(line))
                else:
                    lines.append(str(line))
        return lines
    else:
        return 'Le fichier n existe pas'


def counter(path):
    files = os.listdir(path)
    nb_files = 0
    nb_folder = 0
    for file in files:
        if os.path.isdir(file):
            nb_folder += 1
        else:
            nb_files += 1
    return nb_files, nb_folder, 10, 320, 2034343, 10