import random


def create_file(path='file_create.txt', bound_lower=0, bound_upper=100, bound_range=1000):
    with open(path, 'w') as file:
        for i in range(0, bound_range):
            result = random.randint(bound_lower, bound_upper)
            file.write(f"{result}\n")


def read_file(path='file_create.txt', path_dest='file_create_admin.txt', mid_bound=50):
    with open(path, 'r') as file, open(path_dest, 'w', encoding="utf-8") as file_writer:
        tmp = []
        i = 0
        moyenne = 0

        for line in file:
            line = line.rstrip()
            if line.isdigit():
                line = int(line)
                if line < mid_bound:
                    file_writer.write(f'{line} recalé\n')
                else:
                    file_writer.write(f'{line} admis\n')

                tmp.append(line)
                moyenne += line
                i += 1
        return moyenne / i
create_file(path="test_create_file.txt")
moyenne = read_file(path="test_create_file.txt")

print(f'la moyenne est {moyenne:.2f}')

