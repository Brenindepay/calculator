from database import *

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                   (nome, quantidade, preco))

    conn.commit()
    conn.close()
    print("Produto adicionado com sucesso!")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    print("\n--- ESTOQUE ---")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Qtd: {p[2]} | Preço: R${p[3]}")

    conn.close()

def menu():
    criar_tabela()

    while True:
        print("\n1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

menu()
