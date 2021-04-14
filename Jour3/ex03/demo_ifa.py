class objetJeu:

    maxItem = 10

    def __init__(self):
        self.catory = "arme"


class arme:
    def __init__(self):
        self.name = "P90"
        self.munition = "9mm"


class fusil(objetJeu, arme):
    def __init__(self):
        objetJeu.__init__(self)
        arme.__init__(self)



if __name__ == "__main__":

    fusilSniper = fusil()
    objetJeu = objetJeu()
    arme = arme()

    print(fusilSniper.name, fusilSniper.catory)
    print(isinstance(fusilSniper, objetJeu))















# #héritage isinstance, issubclass
#
#
# #class Mère
# class Humain:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def presentation(self):
#         print(f"je me nomme {self.name}")
#
# #class fille
# class Etudiant(Humain):
#     def __init__(self):
#         self.category = "IT"
#         self.reduct = "15%"
#         Humain.__init__(self, "Olivier", 30)
#
#     def etatEtudiant(self):
#         print(f'je vais bien mais j ai bientôt mes partiels')
#
#
# class Employe(Humain):
#     def __init__(self):
#         Humain.__init__(self, "Olivier2")
#
#
# if __name__ == "__main__":
#     etudiant = Etudiant()
#     human = Humain("Elian", 30)
#     human.presentation()
#
#     print(isinstance(etudiant, int))
#     print(issubclass(Etudiant, Humain))
#     print(issubclass(Humain, Etudiant))
