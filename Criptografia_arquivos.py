from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
print(key)

arquivo = input("Digite o local do arquivo: ")

with open(f"{arquivo}", "rb") as f:
    conteúdo = f.read()

conteúdo_criptografado = fernet.encrypt(conteúdo)

with open(f"{arquivo}.enc", "wb") as f:
    f.write(conteúdo_criptografado)
