# CRUD de Cadastro em Python 🐍

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![License](https://img.shields.io/badge/Licença-MIT-yellow)
![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindas-orange)
![Stars](https://img.shields.io/github/stars/KellyFurtado/crud-python-cadastro?style=social)
![Forks](https://img.shields.io/github/forks/KellyFurtado/crud-python-cadastro?style=social)
![Issues abertas](https://img.shields.io/github/issues/KellyFurtado/crud-python-cadastro)
![Issues fechadas](https://img.shields.io/github/issues-closed/KellyFurtado/crud-python-cadastro)
![Última atualização](https://img.shields.io/github/last-commit/KellyFurtado/crud-python-cadastro)

Este projeto é um **CRUD simples** (Create, Read, Update, Delete) feito em Python, utilizando arquivos JSON para armazenar os dados de pessoas (nome, idade e ID).

---

## 🚀 Funcionalidades
- **Cadastrar pessoa** (gera ID automático)
- **Listar pessoas** cadastradas
- **Pesquisar pessoa** pelo ID
- **Editar pessoa** (nome e/ou idade)
- **Excluir pessoa** do cadastro
- Dados salvos em arquivo `cadastro.json`

---

## 📂 Estrutura do projeto
crud-python-cadastro/
│── main.py          # Código principal do CRUD
│── cadastro.json    # Arquivo de dados (inicialmente vazio: [])
│── README.md        # Documentação do projeto

---

## 🛠️ Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/KellyFurtado/crud-python-cadastro.git

Entre na pasta:

bash
cd crud-python-cadastro
Execute o programa:

bash
python main.py

📜 Código (trecho de exemplo)
python
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
(O código completo está disponível no arquivo main.py do repositório.)

📌 Requisitos
Python 3 instalado na máquina

Biblioteca padrão json (já vem com Python)

💡 Melhorias futuras
Criar função para buscar por nome

Tratar erros caso o arquivo cadastro.json não exista

Interface gráfica simples (Tkinter ou PyQt)

Testes automatizados

👩‍💻 Autor
Projeto desenvolvido por Kelly Furtado como prática de programação em Python.
