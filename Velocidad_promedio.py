# Roberto Emmanuel González Muñoz A01376803
# Obtiene la velocidad promedio de caje
# si se conoce el tiempo y la distancia recorrida.


def main():
    tiempo = int(input("Teclee el tiempo que llevó el último viaje en horas: "))
    distancia = int(input("Teclea la distancia recorrida en km: "))
    velocidadPromedio = distancia/tiempo
    print("La velocidad promedio es de: ", velocidadPromedio, "km/h")

main()