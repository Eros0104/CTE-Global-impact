from utils.calculations.user_tax import calculate_user_tax_by_kilometer


def calculate_anual_projection_by_percentage(
    percentage, kilometers, anual_total_passengers
):
    formated_percentage = percentage * 0.01
    estimated_passengers = anual_total_passengers * formated_percentage
    user_tax = calculate_user_tax_by_kilometer(kilometers)
    return user_tax * estimated_passengers
