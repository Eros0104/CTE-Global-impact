from utils.format.currency import to_currency
from utils.calculations.user_tax import calculate_user_tax_by_kilometer
from utils.calculations.anual_cost import calculate_anual_cost_by_kilometer
from utils.calculations.anual_projection import calculate_anual_projection_by_percentage
from utils.reports.table_generator import (
    render_row,
    render_header,
    render_line,
)
import json

km = 27
routes = json.load(open("data/routes.json"))


render_header()
for route in routes:
    distance = route.get("distance")
    anual_passengers = route.get("anualPassengers")
    # 1 Cálculo da tarifa ao passageiro por trecho
    route["user_tax"] = calculate_user_tax_by_kilometer(distance)
    # 2) Cálculo do custo operacional anual por trecho
    route["anual_cost"] = calculate_anual_cost_by_kilometer(distance)
    # 3) Cálculo  da  projeção  anual  de  receitas
    route["anual_projection_30"] = calculate_anual_projection_by_percentage(
        30, distance, anual_passengers
    )
    route["anual_projection_40"] = calculate_anual_projection_by_percentage(
        40, distance, anual_passengers
    )
    route["anual_projection_50"] = calculate_anual_projection_by_percentage(
        50, distance, anual_passengers
    )
    route["anual_projection_60"] = calculate_anual_projection_by_percentage(
        60, distance, anual_passengers
    )

    render_row(route)
render_line()
