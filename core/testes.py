from models.models import *

segmento = []
segmento.append(CampoFichaPersonagem("Força", 5, "Quão forte e resistente o personagem é!"))
segmento.append(CampoFichaPersonagem("Destreza", 3, "Quão rápido e ágil o personagem é!"))
ficha = Ficha(segmento)

# ficha = segmentos[]
# segmentos[camp
#campo index: 0
# campo = {nome:"Força", valor:5, descricao:"Quão forte e resistente o personagem é!"}

for i in range(len(ficha.segmentos)):
    print(ficha.segmentos[i])
for x in range(ficha):
    #para cada campo in ficha
    print(ficha[x].nome)
    print(ficha[x].valor)
    print(ficha[x].descricao)