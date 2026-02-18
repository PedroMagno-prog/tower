class Monstro:

    def __init__(self, nome, tipo, familia, nivel, descricao=None):

        self.nome = nome
        self.tipo = tipo
        self.familia = familia
        self.nivel = nivel
        self.descricao = descricao

    def __str__(self):
        # Isso ajuda a identificar o objeto no admin do Django
        return f"{self.nome} (Nível {self.nivel})"


class Loot:

    def __init__(self, nome, raridade, valor, descricao=None):

        self.nome = nome
        self.raridade = raridade
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f"Loot: {self.nome}, Raridade: {self.raridade}, Valor: {self.valor}"