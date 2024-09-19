# Integrantes:
# Ianny Raquel Ferreira de Souza - 559096
# Jean Matheus Mohamed de Oliveira - 555519
# Maria Alice Freitas Araújo - 557516
# Thiago de Barros Oliveira - 555485

# Constante para separação visual
BARRA = "-" * 100

# Armazenamento de dados (listas para usuários, emails e senhas)
usuarios = []
emails = []
senhas = []

# Função para exibir mensagem de boas-vindas
def boas_vindas():
    """Exibe mensagem de boas-vindas."""
    print(BARRA)
    print("\nMahindra")
    print("Seja bem vindo(a)!\n")

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios, emails, senhas):
    """Realiza o cadastro de um novo usuário."""
    while True:
        print(BARRA)
        print("\nPÁGINA DE CADASTRO\n")
        nome = input("Nome completo: ")
        cadastro_usuario = input("Nome de Usuário (deve ser único): ")
        
        # Verifica se o nome de usuário já está em uso
        if cadastro_usuario in usuarios:
            print(f"O nome de usuário '{cadastro_usuario}' já está em uso.")
            continue
        
        email = input("Email (deve ser único): ")
        
        # Verifica se o email já está em uso
        if email in emails:
            print(f"O email '{email}' já está em uso.")
            continue
        
        cadastro_senha = input("Senha: ")

        # Armazena as informações do novo usuário
        usuarios.append(cadastro_usuario)
        emails.append(email)
        senhas.append(cadastro_senha)

        print(f"\n✅ Usuário '{cadastro_usuario}' cadastrado com sucesso!\n")

        return True

# Função para realizar o login do usuário
def login_usuario(usuarios, senhas):
    """Realiza o login do usuário."""
    print(BARRA)
    print("\nPÁGINA DE LOGIN\n")
    login_usuario = input("Usuário: ")
    login_senha = input("Senha: ")

    # Verifica se o nome de usuário e senha correspondem aos armazenados
    if login_usuario in usuarios and senhas[usuarios.index(login_usuario)] == login_senha:
        print(f"\n✅ Usuário '{login_usuario}' logado com sucesso!\n")
        return True
    else: 
        print("\nUsuário ou senha incorretos. Tente Novamente.")
        return False

# Função para exibir a página inicial com opções de cadastro ou login
def pagina_inicial(usuarios, emails, senhas):
    """Exibe a página de cadastro com opções de cadastrar ou logar."""
    while True:
        print(BARRA)
        print("\nPÁGINA INCIAL\n")
        print("1 - Cadastrar")
        print("2 - Login")
        
        codigo_cadastro = input("\nEscolha a opção desejada (1 para cadastrar, 2 para login): ")
        print()
        
        if not codigo_cadastro.isdigit():
            print(BARRA)
            print("\nOpção inválida.\n")
            continue
        
        codigo_cadastro = int(codigo_cadastro)
        
        if codigo_cadastro == 1:
            if not cadastrar_usuario(usuarios, emails, senhas):
                continue
        elif codigo_cadastro == 2:
            if login_usuario(usuarios, senhas):
                break
        else:
            print(BARRA)
            print("\nOpção inválida.\n")

# Função para exibir informações sobre equipes da Fórmula E
def equipes():
    """Exibe a lista de equipes e suas descrições."""
    print(BARRA)
    print("\nEQUIPES\n")
    print("1 - DS Techeetah")
    print("2 - Mercedes-Benz EQ")
    print("3 - Nissan e.dams")
    print("4 - Audi Sport ABT Schaeffler")
    print("5 - Jaguar Racing")
    print("6 - BMW i Andretti Motorsport")
    print("7 - Mahindra Racing")
    print("8 - Venturi")
    print("9 - ROKiT Venturi Racing")
    print("10 - NIO 333")
    print("11 - Porsche")

    opcao_equipes = input("\nEscolha o número da equipe desejada: ")
    print()
    
    if not opcao_equipes.isdigit():
        print(BARRA)
        print("\nOpção inválida.\n")
        return
    
    opcao_equipes = int(opcao_equipes)
    
    # Dicionário com descrições das equipes
    equipes_dict = {
        1: "DS Techeetah é uma equipe dominante com uma parceria sino-francesa, liderada por Jean-Éric Vergne e António Félix da Costa.",
        2: "Uma entrada relativamente nova na Fórmula E, a equipe da Mercedes tem mostrado forte desempenho com Stoffel Vandoorne e Nyck de Vries como seus pilotos.",
        3: "Uma parceria entre a Nissan e a equipe e.dams, eles têm uma história de sucesso na categoria. Sébastien Buemi e Oliver Rowland lideram a equipe.",
        4: "Uma das equipes mais estabelecidas na Fórmula E, a Audi Sport ABT Schaeffler tem uma reputação de excelência. Lucas di Grassi e René Rast estão no comando dos seus carros.",
        5: "Com Mitch Evans e Sam Bird, a Jaguar Racing está buscando estabelecer-se como uma força competitiva na Fórmula E, representando a lendária marca britânica.",
        6: "Uma parceria entre a BMW e a Andretti Autosport, esta equipe tem sido consistente na Fórmula E. Maximilian Günther e Jake Dennis são os pilotos.",
        7: "A equipe indiana Mahindra Racing tem sido uma presença constante na Fórmula E. Com Alex Lynn e Alexander Sims, eles estão buscando melhorar seu desempenho.",
        8: "A equipe de Mônaco tem Edoardo Mortara e Norman Nato como seus pilotos, buscando alcançar resultados sólidos na Fórmula E.",
        9: "Uma nova parceria para a temporada, com a Venturi e a ROKiT, eles competem com os pilotos Jake Hughes e Norman Nato.",
        10: "A NIO 333 está sempre em busca de melhorar seu desempenho com Oliver Turvey e Tom Blomqvist como seus pilotos.",
        11: "A Porsche entrou na Fórmula E em 2019 e rapidamente mostrou sua competência. André Lotterer e Pascal Wehrlein são os pilotos da equipe, que busca regularmente vitórias e pódios."
    }

    # Exibe a descrição da equipe escolhida pelo usuário
    print(f"\n{equipes_dict.get(opcao_equipes, 'Opção inválida.')}\n")

# Função para exibir a página de conteúdos
def conteudo():
    """Exibe a página de conteúdos."""
    print(BARRA)
    print("\nPÁGINA DE CONTEÚDOS\n")
    print("1 - Equipes\n")

    opcao_entrada = input("Escolha o número do conteúdo desejado: ")
    print()
    
    if not opcao_entrada.isdigit():
        print(BARRA)
        print("\nOpção inválida.\n")
        return
    
    opcao_entrada = int(opcao_entrada)
    
    if opcao_entrada == 1:
        equipes()
    else:
        print(BARRA)
        print("\nOpção inválida.\n")

# Função para exibir a página de usuário logado
def pagina_usuario():
    """Exibe a página inicial com opções de ver conteúdo ou logout."""
    while True:
        print(BARRA)
        print("\nPÁGINA DE USUÁRIO\n")
        print("Olá!\n")
        print("1 - Ver conteúdo")
        print("2 - Logout")

        codigo_inicio = input("\nEscolha a opção desejada (1 para ver conteúdo, 2 para logout): ")
        print()
        
        if not codigo_inicio.isdigit():
            print(BARRA)
            print("\nOpção inválida.\n")
            continue
        
        codigo_inicio = int(codigo_inicio)

        if codigo_inicio == 1:
            conteudo()
        elif codigo_inicio == 2:
            pagina_inicial(usuarios, emails, senhas)
        else:
            print(BARRA)
            print("\nOpção inválida.\n")

# Execução do programa
boas_vindas()
pagina_inicial(usuarios, emails, senhas)
pagina_usuario()