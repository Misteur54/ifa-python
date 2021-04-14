class Ecole:

    def __init__(self, name, located):
        self.name = name
        self._located = located

    def _getlocated(self):
        return self._located

    def _setlocated(self, newLocated):
        self._located = newLocated
    located = property(_getlocated, _setlocated)


ifa = Ecole('ifa', "metz")
print(ifa.located)

#ici on va controler l'accès à la variable located