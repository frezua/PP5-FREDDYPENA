"""
Freddy Enrique Peña Tejada 23-0943
Refinando Código
Refinacion de codigo y se publicara en GITHUB
"""


def costos_lista():
    archivo = open('gift_costs.txt', 'r')
    gift_costs = list(archivo)
    gift_costs = [int(c) for c in gift_costs]
    archivo.close()
    return gift_costs


def total(gift_costs):
    precio_final = 0
    for cost in gift_costs:
        if cost > 1000:
            precio_final += cost * 1.16
        else:
            precio_final += cost

    return precio_final


def main():
    print(total(costos_lista()))
    

if __name__ == '_main_':
    main()