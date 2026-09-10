nome = str(input("digite o nome do aluno: "))
idade = int(input("digite sua idade: "))
print("possui cadastro ? 1 para sim e 2 para não. ")
cad_ativo = int(input("digite a opção: "))

if cad_ativo == 2:
    acesso = "Acesso Negado"
    
elif cad_ativo == 1 and idade <= 13:
    acesso = "Acesso Permitido somente com acompanhante"
    
elif cad_ativo == 1 and idade <=17:
    acesso = "Acesso Permitido, com limitações"  
    
else:
    cad_ativo == 1 and idade >=18
    acesso = "Acesso Permitido"     


print("== Status do Aluno ==")        
print("Aluno ", nome)
print(acesso)
    
    