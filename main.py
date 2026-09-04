import json
import os

# ==== FUNÇÕES DE ARQUIVO ====

def carregar_cadastro():
    if not os.path.exists("cadastro.json"):
        with open("cadastro.json", "w") as arquivo:
            json.dump([], arquivo)  # cria lista vazia
    with open("cadastro.json", "r") as arquivo:
        lista_cadastro = json.load(arquivo)
    return lista_cadastro

def salvar_cadastro(lista_cadastro):
    with open("cadastro.json", "w") as arquivo:
        json.dump(lista_cadastro, arquivo, indent=4)

def emigrar_dado(lista_cadastro):
    for numero, pessoa in enumerate(lista_cadastro, start=1):
        if "id" not in pessoa:
            pessoa["id"] = numero
    salvar_cadastro(lista_cadastro)

# ==== FUNÇÕES AUXILIARES ====

def pedir_nome(mensagem):
    return input(mensagem).strip().title()

def pedir_id(mensagem):
    return int(input(mensagem))

def pedir_idade():
    while True:
        try:
            return int(input("Idade: "))
        except ValueError:
            print("Idade inválida. Tente novamente.")

def encontrar_pessoa(lista_cadastro, id_procurado):
    for pessoa in lista_cadastro:
        if pessoa["id"] == id_procurado:
            return pessoa
    return None

def lista_id(lista_cadastro):
    return [pessoa["id"] for pessoa in lista_cadastro]

def maior_id(lista_cadastro):
    return max(lista_id(lista_cadastro)) if lista_cadastro else 0

# ==== FUNÇÕES DO CRUD ====

def cadastro_pessoa(lista_cadastro):
    nome = pedir_nome("Nome: ")

    # Evita duplicar nomes
    for pessoa in lista_cadastro:
        if pessoa["nome"].lower() == nome.lower():
            print("Esse nome já está cadastrado. Tente novamente.")
            return

    idade = pedir_idade()
    novo_id = maior_id(lista_cadastro) + 1

    nova_pessoa = {"id": novo_id, "nome": nome, "idade": idade}
    lista_cadastro.append(nova_pessoa)
    salvar_cadastro(lista_cadastro)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas(lista_cadastro):
    for pessoa in lista_cadastro:
        print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")

def pesquisar_pessoa(lista_cadastro):
    id_digitado = pedir_id("Digite o ID que deseja pesquisar: ")
    pessoa = encontrar_pessoa(lista_cadastro, id_digitado)
    if pessoa:
        print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")
    else:
        print("Esse ID não consta em nosso cadastro.")

def editar_pessoa(lista_cadastro):
    id_editar = pedir_id("Digite o ID que deseja editar: ")
    pessoa = encontrar_pessoa(lista_cadastro, id_editar)
    if pessoa:
        print(f"Nome: {pessoa['nome']} \nIdade: {pessoa['idade']}")
        print("\n=== MENU ===")
        print("1- Nome")
        print("2- Idade")
        print("3- Nome e Idade")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pessoa['nome'] = pedir_nome("Novo nome: ")
        elif opcao == "2":
            pessoa['idade'] = pedir_idade()
        elif opcao == "3":
            pessoa['nome'] = pedir_nome("Novo nome: ")
            pessoa['idade'] = pedir_idade()
        else:
            print("Opção inválida.")
            return

        salvar_cadastro(lista_cadastro)
        print("Dados atualizados com sucesso!")
    else:
        print("Pessoa não encontrada.")

def excluir_pessoa(lista_cadastro):
    id_excluir = pedir_id("Digite o ID que deseja excluir: ")
    pessoa = encontrar_pessoa(lista_cadastro, id_excluir)
    if pessoa:
        print(f"Nome: {pessoa['nome']} \nIdade: {pessoa['idade']}")
        opcao = input("Tem certeza que deseja excluir? (s/n): ").strip().lower()
        if opcao == "s":
            lista_cadastro.remove(pessoa)
            salvar_cadastro(lista_cadastro)
            print("Exclusão feita com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Pessoa não encontrada.")

# ==== PROGRAMA PRINCIPAL ====

lista_cadastro = carregar_cadastro()
emigrar_dado(lista_cadastro)

while True:
    print("\n=== MENU ===")
    print("1- Cadastrar pessoa")
    print("2- Listar pessoas")
    print("3- Pesquisar pessoa")
    print("4- Editar pessoa")
    print("5- Excluir pessoa")
    print("6- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastro_pessoa(lista_cadastro)
    elif opcao == "2":
        listar_pessoas(lista_cadastro)
    elif opcao == "3":
        pesquisar_pessoa(lista_cadastro)
    elif opcao == "4":
        editar_pessoa(lista_cadastro)
    elif opcao == "5":
        excluir_pessoa(lista_cadastro)
    elif opcao == "6":
        print("Você saiu do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
