nome = str(input("Digite seu nome: "))
velocidade = int(input("velocidade em Mbps: "))

if velocidade <= 50:
    plano = "Plano básico"

elif velocidade <= 100:
    plano = "Plano intermediario"
    
elif velocidade <= 499:
    plano = "Plano avançado"
    
else:
    velocidade >=500
    plano = "Plano ultra"

print("==== DADOS DO CLIENTE ====")    
print("cliente",nome)
print("velocidade contratada:",velocidade,"Mbps")
print(plano)               