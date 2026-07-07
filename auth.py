import csv
import os


# Função para cadastrar novos funcionários
def cadastrar_usuario():
    nome = input("Digite o novo login de funcionário: ")
    senha = input("Digite a senha: ")
    # O modo 'a' (append) adiciona ao arquivo sem sobrescrever
    with open('usuarios.csv', mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, senha])
    print("Funcionário cadastrado com sucesso!")


# Função para validar o acesso
def fazer_login():
    # Validação: Se o arquivo não existir, cria-o automaticamente
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            pass  # Cria o arquivo vazio
        print("Nenhum funcionário cadastrado no sistema.")
        return None

    nome = input("Login: ")
    senha = input("Senha: ")
    with open('usuarios.csv', mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if linha[0] == nome and linha[1] == senha:
                return nome  # Retorna o nome para identificar a sessão
    print("Acesso negado.")
    return None