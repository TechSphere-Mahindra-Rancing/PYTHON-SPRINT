import re
import hashlib
import random

# Constante para separação visual
BARRA = "-" * 100

# Armazenamento de dados
usuarios = {}
historico_acesso = {}
favoritos = {}
comentarios_equipes = {}
desempenho_temporadas = {}
pontuacao_conquistas = {}
temas = {}

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

# Função para autenticação de dois fatores (simples)
def autenticar_2fa():
    """Simula uma autenticação de dois fatores (2FA) via código."""
    codigo_2fa = random.randint(100000, 999999)
    print(f"\nCódigo de autenticação (2FA): {codigo_2fa}")
    codigo_usuario = input("Insira o código de autenticação enviado: ").strip()
    return codigo_usuario == str(codigo_2fa)

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
        favoritos[cadastro_usuario] = []
        desempenho_temporadas[cadastro_usuario] = {}
        comentarios_equipes[cadastro_usuario] = []
        pontuacao_conquistas[cadastro_usuario] = 0
        temas[cadastro_usuario] = 'Claro'  # Tema padrão

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

    if login_usuario in usuarios and usuarios[login_usuario]['senha'] == senha_hash:
        print(f"\n✅ Usuário '{login_usuario}' logado com sucesso!\n")
        
        # Autenticação de dois fatores
        if autenticar_2fa():
            historico_acesso.setdefault(login_usuario, []).append('Login realizado')
            return login_usuario
        else:
            print("Autenticação 2FA falhou. Tente novamente.")
            return None
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

# Função para editar o perfil do usuário
def editar_perfil(usuario_logado):
    """Permite ao usuário editar seu perfil."""
    print(BARRA)
    print("\nEDIÇÃO DE PERFIL\n")
    novo_nome = input(f"Nome atual ({usuarios[usuario_logado]['nome']}): ").strip()
    novo_email = input(f"Email atual ({usuarios[usuario_logado]['email']}): ").strip()

    if novo_nome:
        usuarios[usuario_logado]['nome'] = novo_nome
    if novo_email and validar_email(novo_email):
        usuarios[usuario_logado]['email'] = novo_email

    print("\nPerfil atualizado com sucesso!\n")

# Função para favoritar equipes
def favoritar_equipe(usuario_logado):
    """Permite ao usuário favoritar equipes."""
    equipes_lista = ["DS Techeetah", "Mercedes-Benz EQ", "Nissan e.dams", "Audi Sport ABT Schaeffler", "Jaguar Racing"]
    
    print(BARRA)
    print("\nFAVORITAR EQUIPES\n")
    
    for i, equipe in enumerate(equipes_lista, 1):
        print(f"{i} - {equipe}")

    opcao = input("\nEscolha o número da equipe que deseja favoritar: ").strip()

    if opcao.isdigit() and 1 <= int(opcao) <= len(equipes_lista):
        equipe_favorita = equipes_lista[int(opcao) - 1]
        favoritos[usuario_logado].append(equipe_favorita)
        print(f"\n{equipe_favorita} favoritada!\n")
    else:
        print("\nOpção inválida.\n")

# Função para ver histórico de acesso
def ver_historico_acesso(usuario_logado):
    """Exibe o histórico de acessos do usuário."""
    print(BARRA)
    print("\nHISTÓRICO DE ACESSO\n")
    acessos = historico_acesso.get(usuario_logado, [])
    if acessos:
        for i, acesso in enumerate(acessos, 1):
            print(f"{i} - {acesso}")
    else:
        print("Nenhum histórico de acesso disponível.")

# Função para exibir o desempenho nas temporadas
def desempenho_temporadas_func(usuario_logado):
    """Exibe o desempenho do usuário nas temporadas."""
    print(BARRA)
    print("\nDESEMPENHO NAS TEMPORADAS\n")
    desempenho = desempenho_temporadas.get(usuario_logado, {})
    if desempenho:
        for temporada, pontos in desempenho.items():
            print(f"{temporada}: {pontos} pontos")
    else:
        print("Nenhum desempenho registrado.")

# Função para exibir a pontuação e conquistas
def pontuacao_conquistas_func(usuario_logado):
    """Exibe a pontuação e conquistas do usuário."""
    print(BARRA)
    print("\nPONTUAÇÃO E CONQUISTAS\n")
    pontos = pontuacao_conquistas.get(usuario_logado, 0)
    print(f"Pontuação: {pontos}")

# Função para adicionar comentários sobre equipes
def adicionar_comentarios(usuario_logado):
    """Permite ao usuário adicionar comentários sobre equipes."""
    equipes_lista = ["DS Techeetah", "Mercedes-Benz EQ", "Nissan e.dams", "Audi Sport ABT Schaeffler", "Jaguar Racing"]
    
    print(BARRA)
    print("\nADICIONAR COMENTÁRIOS SOBRE EQUIPES\n")
    
    for i, equipe in enumerate(equipes_lista, 1):
        print(f"{i} - {equipe}")

    opcao = input("\nEscolha o número da equipe para comentar: ").strip()

    if opcao.isdigit() and 1 <= int(opcao) <= len(equipes_lista):
        equipe_comentada = equipes_lista[int(opcao) - 1]
        comentario = input("Seu comentário: ").strip()
        comentarios_equipes.setdefault(usuario_logado, []).append((equipe_comentada, comentario))
        print(f"\nComentário sobre {equipe_comentada} adicionado com sucesso!\n")
    else:
        print("\nOpção inválida.\n")

# Função para alterar o tema
def alterar_tema(usuario_logado):
    """Permite ao usuário alterar o tema."""
    print(BARRA)
    print("\nALTERAR TEMA\n")
    print("1 - Claro")
    print("2 - Escuro")
    
    opcao = input("\nEscolha o tema: ").strip()

    match opcao:
        case "1":
            temas[usuario_logado] = 'Claro'
        case "2":
            temas[usuario_logado] = 'Escuro'
        case _:
            print("\nOpção inválida.\n")
    
    print(f"Tema alterado para {temas[usuario_logado]}.")

# Função para exibir a página de usuário logado
def pagina_usuario(usuario_logado):
    """Exibe a página inicial com opções de ver conteúdo ou logout."""
    while True:
        print(BARRA)
        print(f"\nPÁGINA DE USUÁRIO - {usuario_logado}\n")
        print("1 - Editar Perfil")
        print("2 - Favoritar Equipes")
        print("3 - Ver Histórico de Acesso")
        print("4 - Desempenho nas Temporadas")
        print("5 - Pontuação e Conquistas")
        print("6 - Comentários sobre Equipes")
        print("7 - Alterar Tema")
        print("8 - Logout")

        codigo_inicio = input("\nEscolha a opção desejada: ").strip()

        if not codigo_inicio.isdigit():
            print("\nEntrada inválida. Insira um número.\n")
            continue

        match int(codigo_inicio):
            case 1:
                editar_perfil(usuario_logado)
            case 2:
                favoritar_equipe(usuario_logado)
            case 3:
                ver_historico_acesso(usuario_logado)
            case 4:
                desempenho_temporadas_func(usuario_logado)
            case 5:
                pontuacao_conquistas_func(usuario_logado)
            case 6:
                adicionar_comentarios(usuario_logado)
            case 7:
                alterar_tema(usuario_logado)
            case 8:
                print("\nLogout realizado com sucesso.\n")
                return
            case _:
                print("\nOpção inválida.\n")

# Execução do programa
if __name__ == "__main__":
    boas_vindas()
    usuario_logado = pagina_inicial(usuarios)
    if usuario_logado:
        pagina_usuario(usuario_logado)
