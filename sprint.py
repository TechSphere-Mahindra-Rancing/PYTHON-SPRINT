import re
import hashlib

# Constante para separação visual
BARRA = "-" * 100

# Armazenamento de dados (dicionário para usuários)
usuarios = {}

# Função para exibir mensagem de boas-vindas
def boas_vindas():
    """Exibe mensagem de boas-vindas."""
    print(BARRA)
    print("\nMahindra")
    print("Seja bem vindo(a)!\n")

# Função para validar o formato de email
def validar_email(email):
    """Valida o formato de email usando regex."""
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao_email, email)

# Função para criptografar senha
def hash_senha(senha):
    """Gera o hash da senha utilizando SHA-256."""
    return hashlib.sha256(senha.encode()).hexdigest()