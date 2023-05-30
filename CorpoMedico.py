from dataclasses import dataclass

from Entidades.Enfermeiro import Enfermeiro
from Entidades.Enfermeiro import TecnicoEnfermagem
from Entidades.Especialistas import ClinicoGeral
from Entidades.Especialistas import Ortopedista
from Entidades.Especialistas import Pediatra
from Entidades.Terceirizados import Terceirizado


@dataclass
class Enfermagem:
    enfermeiros: list[Enfermeiro]
    tecnicos_enfermagem: list[TecnicoEnfermagem]


@dataclass
class Especialistas:
    ortopedistas: list[Ortopedista]
    pediatras: list[Pediatra]
    clinicos_gerais: list[ClinicoGeral]


@dataclass
class MedicosTerceirizados:
    terceirizados: list[Terceirizado]


@dataclass
class CorpoMedico:
    enfermagem: Enfermagem
    medicos_terceirizados: MedicosTerceirizados
    especialistas: Especialistas
