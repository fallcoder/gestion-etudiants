from Etudiant import Etudiant
from infos import afficher_infos

etudiant1 = Etudiant("momo", 21, "informatique")
etudiant2 = Etudiant("astou", 24, "infographie")

etudiant1.se_presenter()
afficher_infos(etudiant1)

etudiant2.se_presenter()
afficher_infos(etudiant2)



