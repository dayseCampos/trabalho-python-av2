from dataclasses import dataclass

from Entidades.Funcionario import Funcionario


@dataclass
class Faxineiro(Funcionario):
    pass


@dataclass
class Recepcionista(Funcionario):
    pass
