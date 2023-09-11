import random

def lin():
    print("-"*30)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'

lin()
print()
print("      GERADOR DE SENHAS")
print()
lin()

print("1 - GERAR SENHAS \n2- SAIR")

r = int(input("DIGITE SUA OPÇÃO:\n"))
def func():
    if r == 1:
        q = input("DIGITE A QUANTIDADE DE SENHAS DESEJADAS:\n")
        q = int(q)

        l = input("DIGITE A QUANTIDADE DE CARACTERES DE CADA SENHA:\n")
        l = int(l)

        print("\nAQUI ESTÃO SUAS SENHAS:")

        for psw in range(q):
            passwords = ""
            for c in range(l):
                passwords += random.choice(chars)
            print(passwords)

        print("\nVOLTE SEMPRE!")

    if r == 2:
        print("OK, FECHANDO O PROGRAMA")
        exit()
func()
