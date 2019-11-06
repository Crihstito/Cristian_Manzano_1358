# Una función recursiva que calcule la suma de los elementos de una lista que al ser llamada de la siguiente forma imprima 11. 
lst = [3,5,2,1] # debe imprimir 11
def suma_lista(numero):
    if numero > 0 and numero < len(lst):
        lst[0]+1
        suma_lista(numero)
    else:
        print("la suma es", numero)
    
    
print( suma_lista(lst) )
    
    
    
