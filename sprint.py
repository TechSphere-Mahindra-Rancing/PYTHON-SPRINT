# Integrantes da TechSphere

# Ianny Raquel Ferreira de Souza - 559096
# Jean Matheus Mohamed de Oliveira - 555519
# João Victor Soave - 557595
# Maria Alice Freitas Araújo - 557516
# Thiago de Barros Oliveira - 555485


# Importações de bibliotecas
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
    try:
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(padrao_email, email))
    except Exception as e:
        print(f"Erro ao validar email: {e}")
        return False

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
            if not usuarios[login_usuario].get('primeiro_login', True):  # Verifica se é o primeiro login
                pontuacao_conquistas[login_usuario] += 100  # Adiciona 100 pontos
                usuarios[login_usuario]['primeiro_login'] = False
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

        try:
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
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número.\n")

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

def exibir_mensagem_parabens(usuario, pontos, acao):
    print(f"\nParabéns, {usuario}! Você ganhou {pontos} pontos por {acao}!")

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
        pontuacao_conquistas[usuario_logado] += 50
        exibir_mensagem_parabens(usuario_logado, 50, "favoritar uma equipe")
    else:
        print("\nOpção inválida.\n")

# Função para ver histórico de acesso
def ver_historico_acesso(usuario_logado):
    """Exibe o histórico de acessos do usuário.""" 
    print(BARRA)
    print("\nHISTÓRICO DE ACESSO\n")
    try:
        acessos = historico_acesso.get(usuario_logado, [])
        if acessos:
            for i, acesso in enumerate(acessos, 1):
                print(f"{i} - {acesso}")
        else:
            print("Nenhum histórico de acesso disponível.")
    except Exception as e:
        print(f"Erro ao exibir histórico de acesso: {e}")

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

    opcao = input("\nEscolha o número da equipe que deseja comentar: ").strip()

    if opcao.isdigit() and 1 <= int(opcao) <= len(equipes_lista):
        equipe_comentada = equipes_lista[int(opcao) - 1]
        comentario = input("Digite seu comentário: ").strip()
        comentarios_equipes[usuario_logado].append({"equipe": equipe_comentada, "comentario": comentario})
        pontuacao_conquistas[usuario_logado] += 20  # Adiciona 20 pontos
        exibir_mensagem_parabens(usuario_logado, 20, "adicionar um comentário")
        print("\nComentário adicionado com sucesso!\n")
    else:
        print("\nOpção inválida.\n")

# Função para ver comentários feitos
def ver_comentarios(usuario_logado):
    """Exibe os comentários feitos pelo usuário.""" 
    print(BARRA)
    print("\nCOMENTÁRIOS FEITOS\n")
    comentarios = comentarios_equipes.get(usuario_logado, [])
    if comentarios:
        for i, comentario in enumerate(comentarios, 1):
            print(f"{i} - {comentario['equipe']}: {comentario['comentario']}")
    else:
        print("Nenhum comentário registrado.")

# Função principal do programa
def main():
    """Executa o programa."""
    boas_vindas()
    usuario_logado = pagina_inicial(usuarios)

    while True:
        print(BARRA)
        print("\nPÁGINA DO USUÁRIO\n")
        print("1 - Editar Perfil")
        print("2 - Favoritar Equipe")
        print("3 - Ver Favoritos")
        print("4 - Ver Histórico de Acesso")
        print("5 - Desempenho nas Temporadas")
        print("6 - Pontuação e Conquistas")
        print("7 - Adicionar Comentários")
        print("8 - Ver Comentários Feitos")
        print("9 - Sair")

        opcao_usuario = input("\nEscolha a opção desejada: ").strip()

        if not opcao_usuario.isdigit():
            print("\nOpção inválida. Por favor, insira um número.\n")
            continue

        try:
            match int(opcao_usuario):
                case 1:
                    editar_perfil(usuario_logado)
                case 2:
                    favoritar_equipe(usuario_logado)
                case 3:
                    print(f"Equipes favoritas: {favoritos[usuario_logado]}")
                case 4:
                    ver_historico_acesso(usuario_logado)
                case 5:
                    desempenho_temporadas_func(usuario_logado)
                case 6:
                    pontuacao_conquistas_func(usuario_logado)
                case 7:
                    adicionar_comentarios(usuario_logado)
                case 8:
                    ver_comentarios(usuario_logado)
                case 9:
                    print("Saindo...")
                    exit()
                case _:
                    print("\nOpção inválida.\n")
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número.\n")

if __name__ == "__main__":
    main()
