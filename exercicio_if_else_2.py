produto = str(input("Digite o nome do produto "))
quantidade = int(input("Digite a quantidade em estoque "))


if quantidade == 0:
    estoque = "esgotado"
    
elif quantidade <= 5:
    estoque = "critico"
    
elif quantidade <= 20:
    estoque = "baixo"     
    
else: 
    quantidade >= 21
    estoque = "normal"


print("produto: ", produto)
print("quantidade disponível: ", quantidade)
print("estoque: ", estoque)
print(10 + 10)      