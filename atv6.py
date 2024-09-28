preço = int(input("qual o preço do carro:"))
ano = int(input("Qual o ano do carro? "))
if ano <= 1990:
   imposto= print("esse é o valor do imposto",preço*0.01)
elif ano > 1990:
   imposto= print("esse é o valor do imposto é:",preço*0.015)