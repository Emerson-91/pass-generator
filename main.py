import random
import string


def generate_password():
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numerais = "123456789"
    symbols = "[]{}*#$@%!&?/.,-="

    combine = letras_maiusculas
    combine += letras_minusculas
    combine += numerais
    combine += symbols

    tamanho = 10

    password = "".join(random.sample(combine, tamanho))
    print(password)


generate_password()
