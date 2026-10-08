mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print(mySet)
print(mySet2)

# 1. Qual é a diferença?
# set('ATGTGGG') transforma cada caractere da sequência em um elemento do conjunto, eliminando as repetições, enquanto {'ATGCCT'} cria um conjunto contendo uma única string como elemento.#

#2. Importa como você cria o conjunto?
# Sim. A forma de criação importa, principalmente quando queremos criar um conjunto vazio: set() cria um conjunto vazio, enquanto {} cria um dicionário vazio. Além disso, set('ATGTGGG') e {'ATGTGGG'} produzem conjuntos diferentes.
