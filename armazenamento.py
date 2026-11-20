import json
import os


class Armazenamento:
    def __init__(self, caminho="dados/consultas.json"):
        self.caminho = caminho

    def carregar(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Aviso: ficheiro danificado. A começar com lista vazia.")
            return []

    def guardar(self, dados):
        try:
            pasta = os.path.dirname(self.caminho)
            if pasta:
                os.makedirs(pasta, exist_ok=True)
            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
        except OSError as erro:
            print(f"Erro ao guardar os dados: {erro}")
