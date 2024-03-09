import re

def formata_nome():
    nome_completo = input("Digite o seu nome completo: ")
    nomes = nome_completo.split()
    iniciais_maiusculas = [nome.capitalize() for nome in nomes]
    return ' '.join(iniciais_maiusculas)





def valida_data_nascimento():
    while True:
        data_nascimento = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
        if re.match(r'^\d{2}/\d{2}/\d{4}$', data_nascimento):
            return data_nascimento
        else:
            print("Formato invalido. Digite a data de nascimento no formato dd/mm/aaaa:\n")

def valida_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

def retorna_cpf():
    while True:
        cpf = input("Digite o seu cpf no formato XXX.XXX.XXX-XX: ")
        if re.match(r'^\d{3}.\d{3}.\d{3}-\d{2}', cpf):
            if valida_cpf(cpf):
                return cpf
            print("CPF inválido. Tente novamente.")
        else:
            print("Formato invalido. Digite a cpf no formato XXX.XXX.XXX-XX")

def valida_email():
    while True:
        email: str = input("Digite o seu e-mail: ")
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return email
        else:
            print("E-mail inválido. Digite novamente.")
