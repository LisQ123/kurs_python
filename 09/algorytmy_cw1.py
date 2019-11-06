lista_obiektow = ['dom', 'szkola', 'kosciol', 'bar', 'szpital', 'kino', 'teatr']

graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

for row in range(7):
    print(graph[row])
    for col in range(6):
        if graph[row][col] == 1:
            print(lista_obiektow[row], '----', lista_obiektow[col])

# print("Dom z kinem", graph[0][6])
# print("Bar z kosciolem", graph[4][3])