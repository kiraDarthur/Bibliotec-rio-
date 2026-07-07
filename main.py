import csv, auth, os


# Classe que estrutura os dados do livro na memória
class Livro:
    def __init__(self, isbn, titulo, autor, ano, categoria, total, disponiveis):
        self.isbn, self.titulo, self.autor = isbn, titulo, autor
        self.ano, self.categoria = ano, categoria
        self.total, self.disponiveis = int(total), int(disponiveis)


acervo = []


# Função para organizar o terminal, limpando registros anteriores
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Lê o arquivo CSV e converte cada linha em um objeto da classe Livro
def carregar_acervo():
    acervo.clear()
    # Verifica se o arquivo existe, caso não, cria a estrutura básica
    if not os.path.exists('acervo.csv'):
        with open('acervo.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ISBN', 'Titulo', 'Autor', 'Ano', 'Categoria', 'Total', 'Disponiveis'])
        return
    with open('acervo.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        next(leitor)  # Pula a linha do cabeçalho
        for linha in leitor: acervo.append(Livro(*linha))


# Atualiza o arquivo CSV com os dados atuais salvos na memória
def salvar_acervo():
    with open('acervo.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ISBN', 'Titulo', 'Autor', 'Ano', 'Categoria', 'Total', 'Disponiveis'])
        for l in acervo:
            writer.writerow([l.isbn, l.titulo, l.autor, l.ano, l.categoria, l.total, l.disponiveis])


# Cadastro com validação de campos vazios (ENTER cancela) e numéricos
def cadastrar_livro():
    print("\n--- CADASTRO DE NOVO LIVRO (ENTER vazio para cancelar) ---")
    isbn = input("ISBN: ");
    if not isbn: return
    titulo = input("Título: ");
    if not titulo: return
    autor = input("Autor: ");
    if not autor: return
    ano = input("Ano: ");
    if not ano: return
    categoria = input("Categoria: ");
    if not categoria: return

    # Loop de validação para garantir que o estoque seja um número
    while True:
        total_input = input("Quantidade total: ")
        if not total_input: return  # Aborta cadastro se pressionar ENTER
        if total_input.isdigit():
            total = int(total_input)
            break
        print("Erro: Digite apenas números inteiros!")

    novo_livro = Livro(isbn, titulo, autor, ano, categoria, total, total)
    acervo.append(novo_livro)
    salvar_acervo()  # Salva imediatamente no CSV
    print("\nSUCESSO: Livro adicionado!")
    input("Pressione ENTER para continuar...")


# Painel principal onde o bibliotecário realiza as operações
def menu_gestao(nome):
    while True:
        limpar_tela()
        print(f"\n--- PAINEL DO BIBLIOTECÁRIO ({nome}) ---")
        print("1. Listar Acervo \n2. Registrar Empréstimo \n3. Registrar Devolução \n4. Cadastrar Livro \n0. Logout")
        op = input("Opção: ")

        if op == '1':  # Listagem simples do inventário
            limpar_tela()
            print("--- ACERVO ATUAL ---")
            for l in acervo: print(f"Livro: {l.titulo:<20} | Estoque: {l.disponiveis}/{l.total}")
            input("\nPressione ENTER para voltar ao menu...")

        elif op == '2':  # Lógica de saída de estoque
            nome_livro = input("Nome do livro para empréstimo (ou ENTER para cancelar): ")
            if not nome_livro: continue # Pula o resto do código e volta para o menu
            for l in acervo:
                if nome_livro.lower() in l.titulo.lower() and l.disponiveis > 0:
                    l.disponiveis -= 1
                    salvar_acervo()
                    print("\nSUCESSO: Empréstimo registrado!")
                    break
            else:
                print("\nERRO: Livro indisponível ou não encontrado.")
            input("Pressione ENTER para continuar...")

        elif op == '3':  # Lógica de entrada de estoque
            nome_livro = input("Nome do livro para devolução (ou ENTER para cancelar): ")
            if not nome_livro: continue
            for l in acervo:
                if nome_livro.lower() in l.titulo.lower() and l.disponiveis < l.total:
                    l.disponiveis += 1
                    salvar_acervo()
                    print("\nSUCESSO: Devolução registrada!")
                    break
            else:
                print("\nERRO: Erro na devolução.")
            input("Pressione ENTER para continuar...")

        elif op == '4':
            cadastrar_livro()

        elif op == '0':  # Sai do loop de gestão
            break


# Início do programa principal
carregar_acervo()
while True:
    limpar_tela()
    print("\n--- SISTEMA DE GESTÃO BIBLIOTECÁRIA ---")
    print("1. Login \n2. Cadastro de Funcionário \n3. Sair")
    op = input("Opção: ")
    if op == '1':
        user = auth.fazer_login()
        if user: menu_gestao(user)  # Inicia sessão se o login for válido
    elif op == '2':
        auth.cadastrar_usuario() #ligação do auth.py
    elif op == '3':
        break