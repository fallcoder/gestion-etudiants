class Etudiant:
    def __init__(self, nom = "inconnu", age = 18, filière = "comptabilité"): #valeur par défaut
        self.nom = nom
        self.age = age
        self.filière = filière 

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans et je suis dans la filière {self.filière}")