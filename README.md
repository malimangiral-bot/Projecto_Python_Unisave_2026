# Agenda de Consultas de Planeamento Familiar

Este projecto é uma agenda de consultas de planeamento familiar desenvolvida em Python com Programação Orientada a Objectos. Permite marcar consultas, consultar lembretes das próximas datas e guardar o histórico de consultas já realizadas. Resolve o problema do esquecimento de consultas e da falta de registo organizado, ajudando a manter o acompanhamento regular dos utilizadores.

## Elementos do Grupo

- Catarina Américo Cossa (americocatarina20-cmd)
- David Ângelo Mazive (davidmazive0-maker)
- Laerson Chiunda António Malimangira (malimangiral-bot)
- Nelton Armando Massingue (neltonmassingue39-blip)

## Funcionalidades

- Marcar, editar e cancelar consultas
- Lembretes das consultas próximas
- Histórico de consultas realizadas
- Pesquisa de consultas por data ou por paciente

## Stack Técnica

- Linguagem: Python 3.x
- Paradigma: Programação Orientada a Objectos (POO)
- Armazenamento: JSON
- Dependências: apenas bibliotecas padrão do Python (json, datetime)

## Arquitectura

O código está organizado em módulos:

- `main.py`: menu principal e interacção com o utilizador
- `modelos.py`: classes `Paciente`, `Consulta` e `Lembrete`
- `agenda.py`: classe `Agenda`, com a lógica de marcar, editar, cancelar e pesquisar
- `armazenamento.py`: leitura e gravação dos dados em JSON, com tratamento de erros
- `dados/consultas.json`: ficheiro onde os dados são guardados

## Requisitos

- Python 3.8 ou superior instalado no computador.

## Instalação e Execução

```bash
git clone https://github.com/malimangiral-bot/Projecto_Python_Unisave_2026.git
cd Projecto_Python_Unisave_2026
python main.py
```