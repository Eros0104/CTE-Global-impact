from utils.format.currency import to_currency
from utils.calculations.user_tax import calculate_user_tax_by_kilometer
from utils.calculations.anual_cost import calculate_anual_cost_by_kilometer
from utils.calculations.anual_projection import calculate_anual_projection_by_percentage
from utils.reports.user_tax import generate_user_tax_report, generate_user_tax_header, generate_user_tax_line
from utils.reports.anual_projection import generate_anual_projection_report
import json

km = 27
travels = json.load(open("data/distances.json"))

# 1 Cálculo da tarifa ao passageiro por trecho
generate_user_tax_header()
for travel in travels:
  distance = travel.get("distance")
  cityA = travel.get("cityA")
  cityB = travel.get("cityB")
  user_tax = calculate_user_tax_by_kilometer(distance)
  generate_user_tax_report(to_currency(user_tax), distance, cityA + " - " + cityB)
generate_user_tax_line()

# 2) Cálculo do custo operacional anual por trecho

generate_anual_projection_report(to_currency(calculate_anual_cost_by_kilometer(km)), km)

# 3) Cálculo  da  projeção  anual  de  receitas

print(to_currency(calculate_anual_projection_by_percentage(30, km)))
print(to_currency(calculate_anual_projection_by_percentage(40, km)))
print(to_currency(calculate_anual_projection_by_percentage(50, km)))
print(to_currency(calculate_anual_projection_by_percentage(60, km)))