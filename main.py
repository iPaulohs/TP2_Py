import re
import uuid
import validations

exec = True

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, email):
        self.id = uuid.uuid4()
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.email = email


pessoas = []


def main():
    while exec:
        print("Selecione uma opção abaixo:\n")
        opc = int(input("1 - Criar um registro\n"
                        "2 - Consultar um registro pelo ID\n"
                        "3 - Listar os registros\n"
                        "4 - Modificar um registro\n"
                        "5 - Apagar um registro\n"
                        "6 - Sair do programa\n"))
        match opc:
            case 1:
                criar()
            case 2:
                consultar()
            case 3:
                listar()
            case 4:
                modificar()
            case 5:
                apagar()
            case 6:
                sair()
            case _:
                print("Digite um valor válido.\n")


def criar():
    _pessoa = Pessoa(validations.formata_nome(), validations.valida_data_nascimento(), validations.retorna_cpf(), validations.valida_email())
    pessoas.append(_pessoa)
    print(f"O objeto {_pessoa.nome} foi criado e adicionado à lista.\n")


def consultar():
    _id = input("Digite o ID do registro que deseja consultar: ")
    if(re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', _id)):
        _id = uuid.UUID(_id)
        for pessoa in pessoas:
            if pessoa.id == _id:
                print(f"Id: {pessoa.id}\n"
                      f"Nome: {pessoa.nome}\n"
                      f"Data de nascimento: {pessoa.data_nascimento}\n"
                      f"CPF: {pessoa.cpf}\n"
                      f"E-mail: {pessoa.email}")
            else:
                print("Nenhum registro encontrado com o Id informado.\n")
    else:
        print("Nenhum registro encontrado com o Id informado.\n")


def listar():
    if len(pessoas) > 0:
        for pessoa in pessoas:
            print(f"Id: {pessoa.id}\n"
                  f"Nome: {pessoa.nome}\n"
                  f"Data de nascimento: {pessoa.data_nascimento}\n"
                  f"CPF: {pessoa.cpf}\n"
                  f"E-mail: {pessoa.email}\n")
    else:
        print("Nenhum registro na lista.\n")


def apagar():
    _id = input("Digite o Id do registro que deseja apagar: \n")
    for pessoa in pessoas:
        if pessoa:
            pessoas.remove(pessoa)
            print(f"Objeto com o id {pessoa.id} removido da lista.\n")
        else:
            print("Nenhum registro encontrado com o Id informado.\n")


def modificar():
    _id = input("Digite o ID do registro que deseja editar: \n")
    if (re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', _id)):
        _id = uuid.UUID(_id)
        for pessoa in pessoas:
            if pessoa.id == _id:
                nome = validations.formata_nome()
                cpf = validations.retorna_cpf()
                data_nascimento = validations.valida_data_nascimento()
                email = validations.valida_email()

                pessoa.nome = nome
                pessoa.cpf = cpf
                pessoa.data_nascimento = data_nascimento
                pessoa.email = email

                print(f"Registro editado:\n"
                      f"Id: {pessoa.id}\n"
                      f"Nome: {pessoa.nome}\n"
                      f"Data de nascimento: {pessoa.data_nascimento}\n"
                      f"CPF: {pessoa.cpf}\n"
                      f"E-mail: {pessoa.email}\n")

    else:
        print("Nenhum registro encontrado com o Id informado.\n")


def sair():
    global exec
    exec = False


main()
