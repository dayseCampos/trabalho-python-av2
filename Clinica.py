from dataclasses import dataclass

from CorpoMedico import CorpoMedico
from Entidades.ServicosGerais import Faxineiro
from Entidades.ServicosGerais import Recepcionista


@dataclass
class Clinica:
    recepcionistas: list[Recepcionista]
    faxineiros: list[Faxineiro]
    corpo_medico: CorpoMedico

    def buscarFuncionario(self, cpf):
        listaFuncionarios = self.recepcionistas + self.faxineiros + self.corpo_medico.enfermagem.enfermeiros + self.corpo_medico.enfermagem.tecnicos_enfermagem + self.corpo_medico.especialistas.ortopedistas + self.corpo_medico.especialistas.pediatras + self.corpo_medico.especialistas.clinicos_gerais + self.corpo_medico.medicos_terceirizados.terceirizados
        for funcionario in listaFuncionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None
