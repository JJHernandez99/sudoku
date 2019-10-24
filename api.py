import requests


def api(tamaño):
    resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(tamaño))
    if tamaño == 9:
        tablero = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]
    elif tamaño == 4:
        tablero = [["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"]]
    for item in resp.json()["squares"]:
        tablero[item["y"]][item["x"]] = str(item["value"])

    return tablero