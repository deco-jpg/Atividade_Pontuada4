import csv
import os

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

def exibir_menu():
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("7. Sair")

def cadastrar_funcionario(lista_funcionarios):
    print("\n--- Cadastrar Funcionário ---")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    while True:
        try:
            salario = float(input("Salário: "))
            if salario >= 0:
                break
            else:
                print("O salário deve ser um valor não negativo.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico para o salário.")

    funcionario = Funcionario(nome, cargo, salario)
    lista_funcionarios.append(funcionario)
    print(f"Funcionário '{nome}' cadastrado com sucesso!")

def listar_funcionarios(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários cadastrados.")
        return

    print("\n--- Lista de Funcionários ---")
    for i, funcionario in enumerate(lista_funcionarios):
        print(f"{i+1}. {funcionario}")

def atualizar_funcionario(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários para atualizar.")
        return

    listar_funcionarios(lista_funcionarios)
    while True:
        try:
            indice = int(input("\nDigite o número do funcionário que deseja atualizar: ")) - 1
            if 0 <= indice < len(lista_funcionarios):
                funcionario = lista_funcionarios[indice]
                print(f"\n--- Atualizar Funcionário: {funcionario.nome} ---")
                novo_nome = input(f"Novo nome ({funcionario.nome}): ") or funcionario.nome
                novo_cargo = input(f"Novo cargo ({funcionario.cargo}): ") or funcionario.cargo
                while True:
                    salario_str = input(f"Novo salário (R${funcionario.salario:.2f}): ") or str(funcionario.salario)
                    try:
                        novo_salario = float(salario_str)
                        if novo_salario >= 0:
                            break
                        else:
                            print("O salário deve ser um valor não negativo.")
                    except ValueError:
                        print("Entrada inválida. Digite um valor numérico para o salário.")

                funcionario.nome = novo_nome
                funcionario.cargo = novo_cargo
                funcionario.salario = novo_salario
                print(f"Funcionário '{funcionario.nome}' atualizado com sucesso!")
                break
            else:
                print("Índice inválido. Por favor, digite um número da lista.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def excluir_funcionario(lista_funcionarios):
    if not lista_funcionarios:
        print("\nNão há funcionários para excluir.")
        return

    listar_funcionarios(lista_funcionarios)
    while True:
        try:
            indice = int(input("\nDigite o número do funcionário que deseja excluir: ")) - 1
            if 0 <= indice < len(lista_funcionarios):
                funcionario_excluido = lista_funcionarios.pop(indice)
                print(f"Funcionário '{funcionario_excluido.nome}' excluído com sucesso!")
                break
            else:
                print("Índice inválido. Por favor, digite um número da lista.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def salvar_dados(lista_funcionarios, nome_arquivo="funcionarios.csv"):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'Cargo', 'Salário'])
            for funcionario in lista_funcionarios:
                writer.writerow([funcionario.nome, funcionario.cargo, funcionario.salario])
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados(lista_funcionarios, nome_arquivo="funcionarios.csv"):
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com uma lista vazia.")
        return

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            next(reader)
            lista_funcionarios.clear()
            for row in reader:
                if len(row) == 3:
                    nome, cargo, salario = row
                    try:
                        salario = float(salario)
                        funcionario = Funcionario(nome, cargo, salario)
                        lista_funcionarios.append(funcionario)
                    except ValueError:
                        print(f"Erro ao converter salário para o funcionário '{nome}'. Ignorando.")
                else:
                    print(f"Linha inválida encontrada no arquivo CSV: {row}. Ignorando.")
        print(f"Dados carregados com sucesso de '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def main():
    lista_funcionarios = []
    carregar_dados(lista_funcionarios)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_funcionario(lista_funcionarios)
        elif opcao == '2':
            listar_funcionarios(lista_funcionarios)
        elif opcao == '3':
            atualizar_funcionario(lista_funcionarios)
        elif opcao == '4':
            excluir_funcionario(lista_funcionarios)
        elif opcao == '5':
            salvar_dados(lista_funcionarios)
        elif opcao == '6':
            carregar_dados(lista_funcionarios)
        elif opcao == '7':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção do menu.")

if __name__ == "__main__":
    main()