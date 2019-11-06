lista_obiektow = ['dom', 'szkola', 'kosciol', 'bar', 'szpital', 'kino', 'teatr']

graph = [(0, 1), (0, 2), (0, 3), (1, 4), (2,3)]

for i in graph:
    b1, b2 = i
    print(lista_obiektow[b1], '------', lista_obiektow[b2])