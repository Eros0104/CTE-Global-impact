from utils.calculations.anual_projection import calculate_anual_projection_by_percentage


def calculate_minimal_passengers_to_profit_10_percent(
    user_tax, operational_cost, passengers
):
    receita = user_tax * passengers
    ten_percent_profit = receita * 0.1
    minimal_passengers = (ten_percent_profit + operational_cost) / user_tax
    return minimal_passengers
