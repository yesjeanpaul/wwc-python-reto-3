import pandas as pd


def analizar_peliculas():
    """
    Escribe tu codigo aquí
    """
    return result


if __name__ == '__main__':
    peliculas_resultantes = analizar_peliculas()
    assert isinstance(peliculas_resultantes, pd.DataFrame), "Tu función aun no devuelve un Dataframe!"
    assert peliculas_resultantes.shape[1] == 5, "Verifica que tu Dataframe solo contenga las columnas mencionadas"
    assert peliculas_resultantes.shape[
               0] == 3, "Creo que debes verificar los filtros, la cantidad de películas que cumple las condiciones no es correcta"
    print("Excelente, has aprendido a leer CSV's con python y como filtrarlos!")
