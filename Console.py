import os
from enum import Enum


class Operacao(Enum):
    CADASTRAR = 1
    BUSCAR = 2
    EXCLUIR = 3
    LISTAR = 4
    SAIR = 0


class Entidade(Enum):
    ORTOPEDISTA = 1
    PEDIATRA = 2
    CLINICO_GERAL = 3
    MEDICO_TERCEIRIZADO = 4
    TECNICO_ENFERMAGEM = 5
    ENFERMEIRO = 6
    RECEPCIONISTA = 7
    FAXINEIRO = 8


def exibir_menu():
    print("\n")
    print("[Sistema de Gerenciamento de Funcionários]")
    print("1. Cadastrar")
    print("2. Buscar")
    print("3. Excluir")
    print("4. Listar")
    print("0. Sair")
    print("\n")


def exibir_cargos():
    print("\n")
    print("[Cargos]")
    print("1. Ortopedista")
    print("2. Pediatra")
    print("3. Clínico Geral")
    print("4. Medico terceirizado")
    print("5. Técnico de Enfermagem")
    print("6. Enfermeiro")
    print("7. Recepcionista")
    print("8. Faxineiro")
    print("\n")


def mostrar_funcionario(funcionario):
    print("\n")
    print("[Funcionário]")
    print(funcionario)
    print("\n")


def mostrar_funcionarios(funcionarios):
    for funcionario in funcionarios:
        mostrar_funcionario(funcionario)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
