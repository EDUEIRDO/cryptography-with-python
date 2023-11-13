from cryptography.fernet import Fernet

pergunta = int(input("Digite 1 para criptografar algo, digite 2 para descriptografar: "))
if pergunta ==1:
    key = Fernet.generate_key()

    fernet = Fernet(key)

    msg = input("Escreva algo para ser criptografado:")
    msg_byte = msg.encode('utf-8')

    msg_encriptada = fernet.encrypt(msg_byte)
    print("A key é: ", key)
    print("Mensagem criptografada: ", msg_encriptada)

    msg_descrip = fernet.decrypt(msg_encriptada)

elif pergunta ==2:
    key = input("Coloque aqui a key para decifrar: ")

    fernet = Fernet(key)

    texto_cifrado = input("Coloque aqui o texto cifrado: ")

    decifrar = fernet.decrypt(texto_cifrado)

    print("Texto decifrado: ", decifrar.decode())

else:
    print("Erro")

