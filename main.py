import Console
from Clinica import Clinica
from Console import Operacao, Entidade
from CorpoMedico import CorpoMedico, Enfermagem, Especialistas, MedicosTerceirizados
from Entidades.Enfermeiro import Enfermeiro, TecnicoEnfermagem
from Entidades.Especialistas import Ortopedista, Pediatra, ClinicoGeral
from Entidades.ServicosGerais import Faxineiro, Recepcionista
from Entidades.Terceirizados import Terceirizado


def executar_opcao(opcao, clinica):
    match opcao:
        case Operacao.CADASTRAR.value:
            nome = input("-> Informe o nome: ")

            while True:
                cpf = input("-> Informe o CPF: ")
                funcionario = clinica.buscarFuncionario(cpf)
                if funcionario is not None:
                    print("[X] Já existe um funcionário com esse CPF, por favor, realize o procedimento novamente!")
                    continue
                break

            salario = float(input("-> Informe o salário: "))

            Console.exibir_cargos()
            cargo = int(input("-> Informe o cargo: "))

            match cargo:
                case Entidade.ORTOPEDISTA.value:
                    clinica.corpo_medico.especialistas.ortopedistas.append(
                        Ortopedista(nome, cpf, salario, Entidade.ORTOPEDISTA.value))

                case Entidade.PEDIATRA.value:
                    clinica.corpo_medico.especialistas.pediatras.append(
                        Pediatra(nome, cpf, salario, Entidade.PEDIATRA.value))

                case Entidade.CLINICO_GERAL.value:
                    clinica.corpo_medico.especialistas.clinicos_gerais.append(
                        ClinicoGeral(nome, cpf, salario, Entidade.CLINICO_GERAL.value))

                case Entidade.ENFERMEIRO.value:
                    clinica.corpo_medico.enfermagem.enfermeiros.append(
                        Enfermeiro(nome, cpf, salario, Entidade.ENFERMEIRO.value))

                case Entidade.TECNICO_ENFERMAGEM.value:
                    clinica.corpo_medico.enfermagem.tecnicos_enfermagem.append(
                        TecnicoEnfermagem(nome, cpf, salario, Entidade.TECNICO_ENFERMAGEM.value))

                case Entidade.MEDICO_TERCEIRIZADO.value:
                    cnpj = input("-> Informe o CPNJ: ")
                    funcao = input("-> Informe a função: ")
                    clinica.corpo_medico.medicos_terceirizados.terceirizados.append(
                        Terceirizado(nome, cpf, salario, Entidade.MEDICO_TERCEIRIZADO.value, cnpj, funcao))

                case Entidade.RECEPCIONISTA.value:
                    clinica.recepcionistas.append(Recepcionista(nome, cpf, salario, Entidade.RECEPCIONISTA.value))

                case Entidade.FAXINEIRO.value:
                    clinica.faxineiros.append(Faxineiro(nome, cpf, salario, Entidade.FAXINEIRO.value))
        case Operacao.BUSCAR.value:
            while True:
                cpf = input("-> Informe o CPF do funcionário: ")
                funcionario = clinica.buscarFuncionario(cpf)
                if funcionario is None:
                    print("[X] Não existe funcionário para esse CPF.")
                    continue
                break
            Console.mostrar_funcionario(funcionario)
        case 3:
            while True:
                cpf = input("-> Informe o CPF do funcionário: ")
                funcionario = clinica.buscarFuncionario(cpf)
                if funcionario is None:
                    print("[X] Não existe funcionário para esse CPF.")
                    continue
                break
            print(f"\n[+] Excluindo funcionário {funcionario.nome}")

            match funcionario.id_cargo:
                case Entidade.ORTOPEDISTA.value:
                    clinica.corpo_medico.especialistas.ortopedistas.remove(funcionario)

                case Entidade.PEDIATRA.value:
                    clinica.corpo_medico.especialistas.pediatras.remove(funcionario)

                case Entidade.CLINICO_GERAL.value:
                    clinica.corpo_medico.especialistas.clinicos_gerais.remove(funcionario)

                case Entidade.ENFERMEIRO.value:
                    clinica.corpo_medico.enfermagem.enfermeiros.remove(funcionario)

                case Entidade.TECNICO_ENFERMAGEM.value:
                    clinica.corpo_medico.enfermagem.tecnicos_enfermagem.remove(funcionario)

                case Entidade.MEDICO_TERCEIRIZADO.value:
                    clinica.corpo_medico.medicos_terceirizados.terceirizados.remove(funcionario)

                case Entidade.RECEPCIONISTA.value:
                    clinica.recepcionistas.remove(funcionario)

                case Entidade.FAXINEIRO.value:
                    clinica.faxineiros.remove(funcionario)

        case 4:
            Console.exibir_cargos()
            cargo = int(input("-> Informe o cargo para obter a lista de funcionários: "))

            match cargo:
                case Entidade.ORTOPEDISTA.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.especialistas.ortopedistas)

                case Entidade.PEDIATRA.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.especialistas.pediatras)

                case Entidade.CLINICO_GERAL.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.especialistas.clinicos_gerais)

                case Entidade.ENFERMEIRO.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.enfermagem.enfermeiros)

                case Entidade.TECNICO_ENFERMAGEM.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.enfermagem.tecnicos_enfermagem)

                case Entidade.MEDICO_TERCEIRIZADO.value:
                    Console.mostrar_funcionarios(clinica.corpo_medico.medicos_terceirizados.terceirizados)

                case Entidade.RECEPCIONISTA.value:
                    Console.mostrar_funcionarios(clinica.recepcionistas)

                case Entidade.FAXINEIRO.value:
                    Console.mostrar_funcionarios(clinica.faxineiros)

        case Operacao.SAIR.value:
            return False
    return True


def main():
    clinica = Clinica([], [], CorpoMedico(Enfermagem([], []), MedicosTerceirizados([]), Especialistas([], [], [])))
    executando = True

    while executando:
        Console.limpar_tela()
        Console.exibir_menu()
        opcao = int(input("-> Digite a opção desejada: "))
        executando = executar_opcao(opcao, clinica)


if __name__ == "__main__":
    main()
