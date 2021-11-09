from utils.format.currency import to_currency


def render_row(travel):
    print(
        "| %36s | %3i | %20s | %23s | %20s | %20s | %20s | %20s |"
        % (
            travel.get("cityA") + " - " + travel.get("cityB"),
            travel.get("distance"),
            to_currency(travel.get("user_tax")),
            to_currency(travel.get("anual_cost")),
            to_currency(travel.get("anual_projection_30")),
            to_currency(travel.get("anual_projection_40")),
            to_currency(travel.get("anual_projection_50")),
            to_currency(travel.get("anual_projection_60")),
        )
    )


def render_line():
    print("+" + "=" * 38 + "+" + "=" * 5 + "+" + "=" * 22 + "+" + "=" * 25 + "+")


def render_header():
    render_line()
    print(
        "| %36s | %3s | %20s | %23s |"
        % ("Trechos", "Km", "Tarifa ao passageiro", "Custo operacional anual")
    )
    render_line()
