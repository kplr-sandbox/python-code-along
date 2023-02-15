#Création d'un dictionnaire
mon_dict = {'clef1':123,'clef2':[12,23,33],'clef3':['item0','item1','item2']}

# Recuperer la valeur de la troisieme clée
key3 = mon_dict['clef3']

# Recuperation de l'infos "item0"
key3_0 = mon_dict["clef3"][0]

# Affichage du reultat
print("Resultat :",key3)
print("Resultat :",key3_0)

# Création d'un dictionnaire
mon_dict = {'clef1':{"sous-clef":{"sous-clef":'valeur'}}}

# Dictionnaire imbriquer
valeur = mon_dict['clef1']['sous-clef']['sous-clef']
print(mon_dict)
