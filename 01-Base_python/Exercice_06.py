# Creation des variables
livre = "Introduction to python"
nombre_de_livre = 12

# Savoir le type de variable
print("Type de la variable :",type(livre))
print("Type de la variable :",type(nombre_de_livre))

# Changer le type d'une variable

nombre_livre = '12'

print("Type de la variable :",int(nombre_de_livre))
print("Type de la variable :",type(nombre_de_livre))

# Validation du type de la variable

print("Valistation du type de la variable :",isinstance(nombre_livre,int))