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
    
# Função para exibir a página inicial com opções de cadastro ou login
def pagina_inicial(usuarios):
    """Exibe a página de cadastro com opções de cadastrar ou logar."""
    while True:
        print(BARRA)
        print("\nPÁGINA INICIAL\n")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        
        codigo_cadastro = input("\nEscolha a opção desejada: ").strip()
        
        if not codigo_cadastro.isdigit():
            print("\nOpção inválida. Por favor, insira um número.\n")
            continue
        
        match int(codigo_cadastro):
            case 1:
                cadastrar_usuario(usuarios)
            case 2:
                usuario_logado = login_usuario(usuarios)
                if usuario_logado:
                    return usuario_logado
            case 3:
                print("Saindo...")
                exit()
            case _:
                print("\nOpção inválida.\n")

# Função para exibir informações sobre equipes da Fórmula E
def equipes():
    """Exibe a lista de equipes e suas descrições."""
    equipes_lista = [
        ("DS Techeetah", "Equipe dominante liderada por Jean-Éric Vergne e António Félix da Costa."),
        ("Mercedes-Benz EQ", "Desempenho forte com Stoffel Vandoorne e Nyck de Vries."),
        ("Nissan e.dams", "História de sucesso com Sébastien Buemi e Oliver Rowland."),
        ("Audi Sport ABT Schaeffler", "Estabelecida com Lucas di Grassi e René Rast."),
        ("Jaguar Racing", "Representando a marca britânica com Mitch Evans e Sam Bird."),
        ("BMW i Andretti Motorsport", "Parceria com Jake Dennis e Maximilian Günther."),
        ("Mahindra Racing", "Presença constante com Alex Lynn e Alexander Sims."),
        ("Venturi", "Busca resultados sólidos com Edoardo Mortara e Norman Nato."),
        ("ROKiT Venturi Racing", "Nova parceria com Jake Hughes e Norman Nato."),
        ("NIO 333", "Melhorando com Oliver Turvey e Tom Blomqvist."),
        ("Porsche", "Entrou em 2019 com André Lotterer e Pascal Wehrlein.")
    ]
    
    print(BARRA)
    print("\nEQUIPES\n")
    
    for i, equipe in enumerate(equipes_lista, 1):
        print(f"{i} - {equipe[0]}")

    try:
        opcao_equipes = int(input("\nEscolha o número da equipe desejada: ").strip())
        if 1 <= opcao_equipes <= len(equipes_lista):
            equipe = equipes_lista[opcao_equipes - 1]
            print(f"\n{equipe[0]}: {equipe[1]}\n")
        else:
            print("\nOpção inválida.\n")
    except ValueError:
        print("\nEntrada inválida. Insira um número.\n")

# Função para exibir a página de conteúdos
def conteudo():
    """Exibe a página de conteúdos."""
    print(BARRA)
    print("\nPÁGINA DE CONTEÚDOS\n")
    print("1 - Equipes\n")

    try:
        opcao_entrada = int(input("Escolha o número do conteúdo desejado: ").strip())
        match opcao_entrada:
            case 1:
                equipes()
            case _:
                print("\nOpção inválida.\n")
    except ValueError:
        print("\nEntrada inválida. Insira um número.\n")

# Função para exibir a página de usuário logado
def pagina_usuario(usuario_logado):
    """Exibe a página inicial com opções de ver conteúdo ou logout."""
    while True:
        print(BARRA)
        print(f"\nPÁGINA DE USUÁRIO - {usuario_logado}\n")
        print("1 - Ver conteúdo")
        print("2 - Logout")

        codigo_inicio = input("\nEscolha a opção desejada: ").strip()
        
        if not codigo_inicio.isdigit():
            print("\nEntrada inválida. Insira um número.\n")
            continue

        match int(codigo_inicio):
            case 1:
                conteudo()
            case 2:
                print("\nLogout realizado com sucesso.\n")
                return
            case _:
                print("\nOpção inválida.\n")