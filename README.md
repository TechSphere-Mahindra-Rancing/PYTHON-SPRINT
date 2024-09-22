# Sistema de Cadastro e Autenticação de Usuários

## Visão Geral

O **Sistema de Cadastro e Autenticação de Usuários** é uma aplicação desenvolvida em Python, focada na gestão de usuários em um contexto esportivo, especificamente relacionado à Fórmula E. O sistema oferece funcionalidades robustas para registro, autenticação e personalização de perfis de usuários, garantindo a segurança e a integridade dos dados.

## Funcionalidades Principais

- **Cadastro de Usuários:** Permite a criação de contas com validação de email e controle de unicidade de nomes de usuário.
- **Login Seguro:** Implementa autenticação com criptografia de senhas e autenticação de dois fatores (2FA) para proteger as contas.
- **Edição de Perfil:** Usuários podem atualizar informações pessoais, como nome e email.
- **Favoritar Equipes:** Usuários têm a opção de favoritar suas equipes preferidas, promovendo uma experiência personalizada.
- **Histórico de Acesso:** Registra as entradas de login dos usuários para que possam acompanhar suas atividades.
- **Desempenho nas Temporadas:** Exibe o desempenho do usuário em diversas temporadas, permitindo a visualização do progresso.
- **Pontuação e Conquistas:** Mantém um registro da pontuação acumulada e das conquistas do usuário.
- **Comentários sobre Equipes:** Usuários podem adicionar comentários e interagir com suas equipes favoritas.
- **Alteração de Tema:** Permite ao usuário escolher entre um tema claro ou escuro, personalizando a interface da aplicação.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal utilizada para o desenvolvimento do sistema.
- **Regex:** Utilizado para a validação de formatos de email, garantindo entradas corretas.
- **Hashlib:** Biblioteca para a geração de hashes de senha usando o algoritmo SHA-256, reforçando a segurança.
- **Random:** Usada para a geração de códigos aleatórios na autenticação de dois fatores.

## Estrutura do Código

O código está modularizado em funções, facilitando a manutenção e a legibilidade. As principais funções incluem:

- `boas_vindas()`: Apresenta uma mensagem de boas-vindas ao usuário.
- `validar_email(email)`: Valida o formato de um endereço de email utilizando expressões regulares.
- `hash_senha(senha)`: Cria um hash da senha fornecida para armazenamento seguro.
- `autenticar_2fa()`: Realiza a autenticação de dois fatores, aumentando a segurança no login.
- `cadastrar_usuario(usuarios)`: Gerencia o processo de cadastro de novos usuários, incluindo validações.
- `login_usuario(usuarios)`: Trata o login dos usuários, integrando a autenticação de dois fatores.
- `pagina_usuario(usuario_logado)`: Exibe as opções disponíveis para o usuário após o login.

## Integrantes do Projeto

Este projeto é uma colaboração entre estudantes da FIAP, cada um contribuindo com suas habilidades:

- **Ianny Raquel Ferreira de Souza** - 559096
- **Jean Matheus Mohamed de Oliveira** - 555519
- **João Victor Soave** - 557595
- **Maria Alice Freitas Araújo** - 557516
- **Thiago de Barros Oliveira** - 555485

## Como Executar o Projeto

Para executar o projeto em sua máquina local, siga os passos abaixo:

1. **Pré-requisitos:**
   - Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em seu sistema.

2. **Clone o Repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/PYTHON-SPRINT.git](https://github.com/TechSphere-Mahindra-Rancing/PYTHON-SPRINT.git)
   cd PYTHON-SPRINT
