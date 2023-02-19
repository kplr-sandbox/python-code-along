#Creation de la fonction en utilisant Kwargs
def ma_fonction(arg1, arg2, **kwargs):
    print(arg1)
    print(arg2)
    print(kwargs) 

#Execution
ma_fonction("a", "b", arg3="c", arg4="d")
