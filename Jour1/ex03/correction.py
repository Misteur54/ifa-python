import sys

while True:
    print('Bienvenue dans un jeu')

    user_age = input("âge du joueur : ")
    if not user_age.isdigit():
        print("Uniquement des chiffres / nombres")
        continue

    user_taille = input("taille du joueur : ")
    if not user_taille.isdigit():
        print("Uniquement des chiffres / nombres")
        continue

    user_job = input("métier du joueur : ")
    if not user_job.isalpha():
        print("uniquement des lettres")
        continue

    user_hobbies = input("passions du joueur : ").split(' ')[0:2]

    tmp = ""
    for hobbie in user_hobbies:
        tmp += f"{hobbie} "

    print(f"votre âge est:{user_age}, votre taille est {user_taille}, métier {user_job}, passions {tmp}")

    user_dmd = input("Tester la fonction nombre premier ? [y/n]")
    if user_dmd != 'y':
        sys.exit("Le joueur ne voulait pas jouer")
    while True:
        nb = input("Nombre / chiffre à tester?")
        if nb == 'q':
            break
        if not nb.isdigit():
            print('Merci de mettre un nombre / chiffre valide')
            continue

        nb = int(nb)
        i = 2
        while i < nb and nb % i != 0:
            i = i + 1
        if i == nb:
            print("il est premier")
        else:
            print('il n est pas premier')
        # if nb > 1 and nb % 2 == 0:
        #     print('')
# print(user_entry)
# print(user_entry.isdigit())