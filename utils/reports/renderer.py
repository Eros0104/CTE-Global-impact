def render_body(routes):
    return ""


def render_table(routes):
    if len(routes) <= 0:
        return ""

    header_keys = routes[0].keys()

    header = ""

    for header_key in header_keys:
        header = header + """<th scope="col">%s</th>""" % header_key

    body = ""

    for route in routes:
        body = body + """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
        """ % (
            route.get("Cidade A"),
            route.get("Cidade B"),
            route.get("Distância (km)"),
            route.get("Passageiros anuais"),
        )

    table = """
    <table class="table">
        <thead>
            <tr>
                %s
            </tr>
        </thead>
        <tbody>
            %s
        </tbody>
    </table>
    """ % (
        header,
        body,
    )

    return table


def render_html(routes, is_viable):
    table = render_table(routes)

    body = """
        <html>
            <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            </head>
            <body>
                %s
            </body>
        </html>
    """ % (
        table
    )

    return body
