import os

class Writer:
    def __init__(self):
        pass


    def writerStr(self, path, mode, informations):
        assert mode in ['w', 'wb', 'wb+'], 'Les modes disponibles sont w, wb, wb+'

        with open(path, mode) as file:
            if isinstance(informations, dict):
                for key, value in informations.items():
                    file.write(f"{value}\n")
            if isinstance(informations, list):
                for nb in informations:
                    file.write(f"{nb}\n")
    # def writerJson(self, path, mode, informations):
    #     {'test': 10}
    #
    #     with open(path, mode) as file:
    #         if isinstance(informations, dict):
    #             for key, value in informations.items():
    #                 file.write(f"{value}\n")


    def readerStr(self, path, mode):
        assert mode in ['r', 'rb', 'rb+'], 'Les modes disponibles sont r, rb, rb+'
        assert os.path.exists(path), 'Le fichier n existe pas'
        print('test')
        with open(path, mode) as file:
            return file.readlines()
            # for line in file:


