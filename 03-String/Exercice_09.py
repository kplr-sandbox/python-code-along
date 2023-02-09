# Déclaration de la variable
feedback = "Went for boxing."

# Récupere l'information stockée dans la variable à la case 0
first_letter = feedback[0]

# Récupere l'information stockée entre la 9 et 15
first_words = feedback[9:15] 
first_words = feedback[-7:-1] 

#Imprimer la taille de la chaine de caractére

print('Première lettre :',first_letter)
print('Première mots :',first_words)

# Récupere l'information stockée dans la variable jusqu'à la case 9
first_words = feedback[:9]
Second_words = "working."

# coller deux variables (ou chaines de caractéres)
print("Result :",first_words + Second_words)

# Duplicer une chaines de caractéres
print("Result :",Second_words * 2)