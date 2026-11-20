from datetime import datetime

FORMATO = "%d/%m/%Y %H:%M"


class Paciente:
    def __init__(self, codigo, idade):
        self.codigo = codigo  # código anónimo, ex.: P001
        self.idade = idade

    def to_dict(self):
        return {"codigo": self.codigo, "idade": self.idade}

    @staticmethod
    def from_dict(d):
        return Paciente(d["codigo"], d["idade"])


class Consulta:
    def __init__(self, id, paciente, data_hora, motivo, estado="Marcada"):
        self.id = id
        self.paciente = paciente
        self.data_hora = data_hora  # texto: "25/11/2026 09:30"
        self.motivo = motivo
        self.estado = estado  # Marcada, Realizada ou Cancelada

    def data_como_objecto(self):
        return datetime.strptime(self.data_hora, FORMATO)

    def to_dict(self):
        return {
            "id": self.id,
            "paciente": self.paciente.to_dict(),
            "data_hora": self.data_hora,
            "motivo": self.motivo,
            "estado": self.estado,
        }

    @staticmethod
    def from_dict(d):
        return Consulta(
            d["id"],
            Paciente.from_dict(d["paciente"]),
            d["data_hora"],
            d["motivo"],
            d["estado"],
        )
