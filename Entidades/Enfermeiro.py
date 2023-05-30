from dataclasses import dataclass

from Entidades.Funcionario import Funcionario


@dataclass
class TecnicoEnfermagem(Funcionario):
    pass


@dataclass
class Enfermeiro(Funcionario):
    pass
