
nome = str(input("Digite seu nome: "))

print("=== MENU DE DEFEITOS ===")
print(" 1 - sistema indisponível")
print(" 2 - sistema funcionando, mas com lentidão ou erros")
print(" 3 - problema que não impede o trabalho")
print(" 4 - outros problemas")

opcao = int(input("Com a ajuda do menu, digite o número do seu problema! "))
tempo = int(input("Digite a quantas horas o problema está ocorrendo? "))

if  opcao == 1: 
    problema = "sistema indisponível"
    prioridade = "crítica"
    
elif opcao == 2:
    problema = "sistema funcionando, mas com lentidão ou erros" 
    prioridade = "alta"
    
elif opcao == 3:
    problema = "problema que não impede o trabalho" 
    prioridade = "média" 
    
elif opcao == 4:
    problema = "outros problemas"
    prioridade = "baixa"
    
else:
    problema = "opção inválida"
    prioridade = "não definida"
        
print("=== CHAMADO DE SUPORTE ===")
print("usuário: ", nome)
print("problema: ", problema)
print("tempo: ", tempo, "hora(s)")
print("prioridade", prioridade)