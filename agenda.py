from datetime import datetime, timedelta
from modelos import Paciente, Consulta, FORMATO
from armazenamento import Armazenamento


class Agenda:
    def __init__(self):
        self.armazenamento = Armazenamento()
        dados = self.armazenamento.carregar()
        self.consultas = [Consulta.from_dict(d) for d in dados]

    def _guardar(self):
        self.armazenamento.guardar([c.to_dict() for c in self.consultas])

    def _novo_id(self):
        return max((c.id for c in self.consultas), default=0) + 1

    def _validar_data(self, data_hora):
        try:
            datetime.strptime(data_hora, FORMATO)
        except ValueError:
            raise ValueError("Data inválida. Use dd/mm/aaaa hh:mm.")

    def marcar(self, codigo, idade, data_hora, motivo):
        if not 0 < idade < 120:
            raise ValueError("Idade inválida.")
        self._validar_data(data_hora)
        c = Consulta(self._novo_id(), Paciente(codigo, idade),
                     data_hora, motivo)
        self.consultas.append(c)
        self._guardar()
        return c

    def procurar(self, id):
        for c in self.consultas:
            if c.id == id:
                return c
        return None

    def remarcar(self, id, nova_data):
        c = self.procurar(id)
        if c is None or c.estado != "Marcada":
            return False
        self._validar_data(nova_data)
        c.data_hora = nova_data
        self._guardar()
        return True

    def cancelar(self, id):
        c = self.procurar(id)
        if c is None or c.estado != "Marcada":
            return False
        c.estado = "Cancelada"
        self._guardar()
        return True

    def concluir(self, id):
        c = self.procurar(id)
        if c is None or c.estado != "Marcada":
            return False
        c.estado = "Realizada"
        self._guardar()
        return True

    def lembretes(self, dias=3):
        agora = datetime.now()
        limite = agora + timedelta(days=dias)
        return [c for c in self.consultas
                if c.estado == "Marcada"
                and agora <= c.data_como_objecto() <= limite]

    def historico(self):
        return [c for c in self.consultas if c.estado == "Realizada"]

    def pesquisar_por_paciente(self, codigo):
        return [c for c in self.consultas
                if c.paciente.codigo.lower() == codigo.lower()]

    def pesquisar_por_data(self, data):
        return [c for c in self.consultas
                if c.data_hora.startswith(data)]
