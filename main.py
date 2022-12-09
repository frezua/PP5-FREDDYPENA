"""
Freddy Enrique Peña Tejada 23-0943
Refinando Código
Refinacion de codigo y se publicara en GITHUB
"""


def costos_lista():
    archivo = open('gift_costs.txt', 'r')
    gift_costs = list(archivo)
    gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
    archivo.close()  # cerrar el archivo después de usarlo y no ser necesario
    return gift_costs


def total(gift_costs):
    precio_final = 0
    for cost in gift_costs:
        if cost > 1000:
            precio_final += cost * 1.16  # agrega impuestos
        else:
            precio_final += cost  # los costos menores a 1000 no se le agrega impuesto

    return precio_final


def main():
    print(total(costos_lista()))
    # llama a los dos funciones y luego imprime el resultado

if __name__ == '_main_':
    main()
