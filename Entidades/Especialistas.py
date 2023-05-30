from dataclasses import dataclass

from Entidades.Funcionario import Funcionario


@dataclass
class ClinicoGeral(Funcionario):
    pass


@dataclass
class Ortopedista(Funcionario):
    pass


@dataclass
class Pediatra(Funcionario):
    pass
