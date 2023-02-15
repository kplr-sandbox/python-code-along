#Creation de la fonction avec Args
def ma_fonction(arg1,arg2,*args):
    print(arg1)
    print(arg2)
    print(args)
    
# Execution
ma_fonction('a','b','c','d','e')