
class Ecole:
    #constructor

    #attribut de classe
    nb_ecole = 0

    def __init__(self, name, located):
        print("création de l'école")
        self.name = name
        self.located = located
        Ecole.nb_ecole += 1



print("on lance le programme")


ifa = Ecole("IFA", "metz")
print(ifa.name, Ecole.nb_ecole)
univ = Ecole("univ", "nancy")
print(Ecole.nb_ecole)


#philosophie de python diff de C++ pas de getter setter etc accesseur

#3 MÉTHODES méthode normale méthode de classe
#global variale dans la class -> savoir combien il y a d'instance de la class
# classmethod, staticmethod
#methode de class avec cls
print('')