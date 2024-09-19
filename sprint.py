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