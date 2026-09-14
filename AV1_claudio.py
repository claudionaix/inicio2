print("==== Sistema para Biblioteca ====")
print("1 - Cadastrar Livros")
print("2 - Cadastrar Alunos")
print("3 - Realizar Empréstimo")
print("4 - Sair")

opcao = int(input("Digite a opção desejada. "))

if opcao == 1:

    quantidade = int(input("Quantos livros deseja cadastrar? "))
    for i in range(1, quantidade +1):
        
         print(f"=== Livro {i}  ===")
         codigo = str(input("Código do livro: "))
         titulo = str(input("Título do livro: "))
         autor = str(input("Autor do livro: "))
         ano = int(input("Ano de publicação: "))
         qtd = int(input("Quantidade: "))
         print("=== Livro cadastrado com sucesso ===")
    
elif opcao == 2:
    quantidade = int(input("Quantos alunos deseja cadastrar? "))
    for i in range(1, quantidade + 1):
         
         print(f"=== Aluno {i}  ===")
         matricula = int(input("Mátricula: "))
         nome = str(input("Nome do aluno: "))
         turma = str(input("Turma: "))
         
         print("=== Aluno cadastrado com sucesso ===")
   
elif opcao == 3:
    
    codigo = int(input("Código do livro: "))
    matricula = int(input("Matricula do aluno: "))
    quantidade = int(input("Quantidade disponível: "))    
         
    if quantidade == 0:
        print("Não é possível realizar o empréstimo.")
        print("Não há exemplares disponíveis.")
    else:
        print("==== Empréstimo ====")
        print("Código do Livro:",codigo)
        print("Matrícula do aluno:",matricula)
        print("Quantidade disponível:",quantidade)
        print("== Empréstimo realizado com sucesso ==")                
         
         
         
elif opcao == 4:
    print('Sair')
        
else: 
      acesso = print("Opção inválida")      
