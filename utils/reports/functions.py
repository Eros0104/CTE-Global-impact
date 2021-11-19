from utils.format.currency import to_currency
from utils.format.number import beautify_number


def is_railroad_viable(routes):
    viable_routes = list(filter(lambda route: route.get("is_viable"), routes))
    viable_routes_quantity = len(viable_routes)
    routes_quantity = len(routes)
    minimal_required_routes = routes_quantity * 0.8
    return viable_routes_quantity >= minimal_required_routes


def convertRouteToRow(route):
    row = {
        "Cidade A": route.get("cityA"),
        "Cidade B": route.get("cityB"),
        "Distância (km)": beautify_number(route.get("distance")),
        "Passageiros anuais": beautify_number(route.get("anualPassengers")),
        "Tarifa ao passageiro": to_currency(route.get("user_tax")),
        "Custo Operacional Anual": to_currency(route.get("anual_cost")),
        "Projeção anual com 30% dos passageiros": to_currency(
            route.get("anual_projection_30")
        ),
        "Projeção anual com 40% dos passageiros": to_currency(
            route.get("anual_projection_40")
        ),
        "Projeção anual com 50% dos passageiros": to_currency(
            route.get("anual_projection_50")
        ),
        "Projeção anual com 60% dos passageiros": to_currency(
            route.get("anual_projection_60")
        ),
        "Quantidade mínima de passageiros para lucrar 10%": beautify_number(
            round(route.get("minimal_passengers_to_profit"))
        ),
        "É viável?": "Sim" if route.get("is_viable") else "Não",
        "Observações": ""
        if route.get("is_viable")
        else "Realizar estudo para verificar se é viável incluindo as estações opcionais que fazem parte da rota",
    }
    return row
