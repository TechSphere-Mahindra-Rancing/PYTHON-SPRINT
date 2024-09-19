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

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    """Realiza o cadastro de um novo usuário."""
    while True:
        print(BARRA)
        print("\nPÁGINA DE CADASTRO\n")
        nome = input("Nome completo: ").strip()
        cadastro_usuario = input("Nome de Usuário (deve ser único): ").strip()
        
        if not nome or not cadastro_usuario:
            print("Nome completo e nome de usuário são obrigatórios.")
            continue

        # Verifica se o nome de usuário já está em uso
        if cadastro_usuario in usuarios:
            print(f"O nome de usuário '{cadastro_usuario}' já está em uso.")
            continue
        
        email = input("Email (deve ser único e válido): ").strip()
        
        # Verifica se o email já está em uso ou inválido
        if not validar_email(email):
            print("Email inválido. Tente novamente.")
            continue
        
        if any(usuario['email'] == email for usuario in usuarios.values()):
            print(f"O email '{email}' já está em uso.")
            continue
        
        senha = input("Senha: ").strip()
        
        if len(senha) < 6:
            print("A senha deve ter no mínimo 6 caracteres.")
            continue
        
        senha_hash = hash_senha(senha)

        # Armazena as informações do novo usuário
        usuarios[cadastro_usuario] = {
            'nome': nome,
            'email': email,
            'senha': senha_hash
        }

        print(f"\n✅ Usuário '{cadastro_usuario}' cadastrado com sucesso!\n")
        return True
    
# Função para realizar o login do usuário
def login_usuario(usuarios):
    """Realiza o login do usuário."""
    print(BARRA)
    print("\nPÁGINA DE LOGIN\n")
    login_usuario = input("Usuário: ").strip()
    login_senha = input("Senha: ").strip()
    senha_hash = hash_senha(login_senha)

    # Verifica se o nome de usuário e senha correspondem aos armazenados
    if login_usuario in usuarios and usuarios[login_usuario]['senha'] == senha_hash:
        print(f"\n✅ Usuário '{login_usuario}' logado com sucesso!\n")
        return login_usuario
    else:
        print("\nUsuário ou senha incorretos. Tente novamente.")
        return None