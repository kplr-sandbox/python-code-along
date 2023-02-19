#Methode 1
file = open("12-Fichiers/Example1.txt",'r')

print(file.read())

#Methode 2
with open("12-Fichiers/Example1.txt",'r') as file1:
    file_content=file1.read()
    
print(file_content)