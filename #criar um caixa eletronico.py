#criar um caixa eletronico


valor = round(float(input("qual o valor que deseja sacar:"))*100)
    
if valor <= 0:

    print("erro digite um valor valido")
else:

    print(f"seu valor de {valor} sera enviado para você aguarde um pouco...")
    
    
    cedulas = [20000,10000,5000,2000,1000,500,200,100,50,25,10,5,1]
    for cedula in cedulas:
        quantidade = valor // cedula
        sobra = valor % cedula
        valor = sobra

        if quantidade >0:
         
            print(f"{quantidade}x R${cedula/100:.2f}") 
     
    
     
