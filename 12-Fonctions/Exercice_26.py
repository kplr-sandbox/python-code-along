# Methode classique

a1=5
b1=5
c1=a1+b1+2*a1*b1-1
if c1<0:
    c1=0
else:
    c1=5
print("Le Resultat est :",c1)

a2=5
b2=5
c2=a2+b2+2*a2*b2-1
if c2<0:
    c2=0
else:
    c2=5
print("Le resultat de la  premiere methode est :",c2)


#2eme Methode Fonction

def equation(a,b):
    c=a+b+2*a*b-1
    if c<0:
        c=0
    else:
        c=5
    return c

a1=5
b1=5
c1=equation(a1,b1)
print('Le resurtat de la 2eme methode est :',c1)