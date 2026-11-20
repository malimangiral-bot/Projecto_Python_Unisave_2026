"""
Agenda de Consultas de Planeamento Familiar
Sistema em Python (POO) que marca consultas, lembra datas
e guarda o histórico em ficheiro JSON.
Projecto_Python_Unisave_2026 - UNISAVE
"""
from agenda import Agenda


def mostrar(c):
    print(f"[{c.id}] {c.data_hora} | Paciente {c.paciente.codigo} "
          f"({c.paciente.idade} anos) | {c.motivo} | {c.estado}")


def listar(consultas):
    if not consultas:
        print("Nenhuma consulta encontrada.")
    for c in consultas:
        mostrar(c)


def ler_inteiro(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Digite um número válido.")


def ler_texto(texto):
    while True:
        valor = input(texto).strip()
        if valor:
            return valor
        print("O campo não pode estar vazio.")


def marcar(agenda):
    codigo = ler_texto("Código do paciente (ex.: P001): ")
    idade = ler_inteiro("Idade: ")
    data_hora = ler_texto("Data e hora (dd/mm/aaaa hh:mm): ")
    motivo = ler_texto("Motivo: ")
    try:
        c = agenda.marcar(codigo, idade, data_hora, motivo)
        print("Consulta marcada com sucesso!")
        mostrar(c)
    except ValueError as erro:
        print(erro)


def remarcar(agenda):
    id = ler_inteiro("ID da consulta: ")
    nova = ler_texto("Nova data e hora (dd/mm/aaaa hh:mm): ")
    try:
        ok = agenda.remarcar(id, nova)
        print("Consulta remarcada." if ok else
              "Consulta não encontrada ou já não está marcada.")
    except ValueError as erro:
        print(erro)


def accao_simples(funcao, mensagem):
    id = ler_inteiro("ID da consulta: ")
    print(mensagem if funcao(id) else
          "Consulta não encontrada ou já não está marcada.")


def main():
    agenda = Agenda()
    while True:
        print("\n=== AGENDA DE PLANEAMENTO FAMILIAR ===")
        print("1. Marcar consulta")
        print("2. Remarcar consulta")
        print("3. Cancelar consulta")
        print("4. Concluir consulta")
        print("5. Lembretes (próximos 3 dias)")
        print("6. Histórico de consultas realizadas")
        print("7. Pesquisar por paciente")
        print("8. Pesquisar por data")
        print("0. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            marcar(agenda)
        elif opcao == "2":
            remarcar(agenda)
        elif opcao == "3":
            accao_simples(agenda.cancelar, "Consulta cancelada.")
        elif opcao == "4":
            accao_simples(agenda.concluir, "Consulta concluída.")
        elif opcao == "5":
            listar(agenda.lembretes())
        elif opcao == "6":
            listar(agenda.historico())
        elif opcao == "7":
            listar(agenda.pesquisar_por_paciente(
                ler_texto("Código do paciente: ")))
        elif opcao == "8":
            listar(agenda.pesquisar_por_data(
                ler_texto("Data (dd/mm/aaaa): ")))
        elif opcao == "0":
            print("Até breve!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
