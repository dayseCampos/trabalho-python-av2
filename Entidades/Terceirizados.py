import string
from dataclasses import dataclass

from Entidades.Funcionario import Funcionario


@dataclass
class Terceirizado(Funcionario):
    funcao: string
    cnpj: string

    def __str__(self) -> str:
        return super().__str__() + f"\n- Função: {self.funcao}\n- CNPJ: {self.cnpj}"
