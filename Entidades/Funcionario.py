import string
from dataclasses import dataclass


@dataclass
class Funcionario:
    nome: string
    cpf: string
    salario: float
    id_cargo: int

    def __str__(self) -> str:
        return f"- Nome: {self.nome}\n- CPF: {self.cpf}\n- Salário: {self.salario}\n- Identificador do cargo: {self.id_cargo}"
