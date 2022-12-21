class Etudiant:
    def __init__(self, nom, postnom, prenom, sexe, age):
        self._nom = nom
        self._postnom = postnom
        self._prenom = prenom
        self._sexe = sexe
        self._age = age

    def get_nom(self):
        return self._nom
    def get_postnom(self):
        return self._postnom
    def get_prenom(self):
        return self._prenom
    def get_sexe(self):
        return self._sexe
    def get_age(self):
        return self._age
if __name__ == '__main__':
    an = Etudiant("BAZAYAMA","MBOTI","Abel","Masculin", 18)
    print("Nom : ",an.get_nom)
    print("Postnom : ",an.get_postnom)
    print("Prenom : ",an.get_prenom)
    print("Sexe : ",an.get_sexe)
    print("Age : ",an.get_age)
