import sys
import os

files = sys.argv
len_argv = len(files)


def count_line(len_argv=1):
    for i in range(1, len_argv, 1):
        if os.path.exists(files[i]):
            with open(files[i], 'r') as file:
                len = 0
                for line in file:
                    len += 1
            print(f"{files[i]} contient {len} lignes")
        else:
            print(f'le fichier {files[i]}n existe pas', file=sys.stderr)

if len(sys.argv) >= 2:
    count_line(len_argv=len(sys.argv))

