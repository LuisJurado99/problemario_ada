def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])
if __name__ == "__main__":
    print(sumalista([3,5,2,4]))
    pass