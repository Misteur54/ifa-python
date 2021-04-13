import random

#La façon simple
def reader():
    file = open('./test.txt', 'r')

    content = file.readlines()
    for line in content:
        print(line)

    file.close()


def reader_with_context():
    with open('./test.txt', 'r') as file:
        for line in file:
            print(line)

        line = file.readline()
        while line != "":
            print(line)
            line = file.readline()
        # lines = file.read()
        # print(lines)
        # for lines in file.read()

# reader_with_context()

def writer_with_content():
    with open('./test_ifa.txt', 'w') as file:
        tmp = ['Ecole', 'Fac', 'Univ', 'Lorraine']
        for i in tmp:
            file.write(f"{i}\n")


# writer_with_content()


def writer_with_context_two():
    with open('./test_ifa.txt', 'r') as file, open('./test_ifa_two.txt', 'w') as file_writer:
        value = ['Ecole', 'Fac']
        for line in file:
            line = line.rstrip()
            print(line, end=' ')
            if line in value:
                file_writer.write(f"{line}")



def writer_random_nb():
    with open('./nb_rand', 'w', encoding="utf-8") as file:
        for i in range(0, 1000):
            result = random.randint(0, 20)
            file.write(f'{result}\n')

    return 'str', 'Papa', 234

a, b, c = writer_random_nb()

print(a, b, c)































#
# content = open('test.txt', 'r')
#
# lines = content.readlines()
#
# for line in lines:
#     print(line)
#
# content.close()
#
# #meilleure façon
#
# with open('test.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)
#
#
# with open('test.txt', 'r') as file:
#     lines = file.read()
#     print(lines)
#
#
# #prend en compte ligne par ligne
#
# print('test')
# with open('test.txt', 'r') as file:
#     lines = file.readline()
#     while lines != "":
#         print(lines)
#         lines = file.readline()
#     print(lines)
#
#
# #python nous facilite la vie
#
# with open('test.txt', 'r') as file:
#     for line in file:
#         print(line)
#
#
# test =  ['test', 'lol', 'papap']
# with open('test_demo.txt', 'w') as file:
#     for t in test:
#         file.write(t)
#
#
#
# #nous on veut avec un bon format avec le\n
#
# with open('test_demo_good.txt', 'w') as file:
#     for t in test:
#         file.write(f'{t}\n')
#
#
#
# #ouvrir deux fichiers
#
# with open('test.txt', 'r') as file_one, open('test_demo.txt', 'w') as file_two:
#     for line in file_one:
#         file_two.write(f'+ {line}')
#
#
# #format et respect
#
# import random
#
# with open('moyenne.txt', 'w') as file:
#     for i in range(0, 1000):
#         file.write(f"{str(random.randint(0, 20))}\n")
