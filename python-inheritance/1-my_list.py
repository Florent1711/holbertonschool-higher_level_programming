# Définition de la classe MyList
class MyList(list):
    # Méthode publique qui affiche la liste triée
    def print_sorted(self):
        # Création d'une copie de la liste
        sorted_list = self.copy()
        # Tri de la copie par ordre croissant
        sorted_list.sort()
        # Affichage de la copie triée
        print(sorted_list)

# Création d'une instance de MyList
my_list = MyList()
# Ajout de quelques éléments à la liste
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
# Affichage de la liste originale
print(my_list)
# Affichage de la liste triée
my_list.print_sorted()
# Affichage de la liste originale (inchangée)
print(my_list)
