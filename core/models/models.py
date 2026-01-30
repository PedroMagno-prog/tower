
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
"""
CampoFichaPersonagem tem 3 tipos:
    CampoTexto
    CampoAtributo
    CampoAcao
"""
class Ficha:
    def __init__(self, segmentos=None):
        if segmentos == None:
            self.segmentos = Segmento()
        else:
            self.segmentos = segmentos

    def __str__(self):
        return (f"\n{self.segmentos[segmento]}" for segmento in range(len(self.segmentos)))


class Segmento:
    def __init__(self, campos=None):
        if campos == None:
            self.campos = []
        else:
            self.campos = campos
    def __str__(self):
        return (f"\n{self.campos[campo]}" for campo in range(len(self.campos)))

class CampoFichaPersonagem:
    def __init__(self, nome, valor, descricao=None):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f"Campo {self.nome}, de Valor {self.valor}"

class Atributo(CampoFichaPersonagem):
    def __init__(self, nome, valor, descricao=None):
        super().__init__(nome, valor, descricao)
