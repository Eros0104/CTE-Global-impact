def render_row(route):
    row = ""
    keys = route
    for key in keys:
        row = row + "<td> %s </td>" % route.get(key)
    return row


def render_table(routes):
    if len(routes) <= 0:
        return ""

    header_keys = routes[0].keys()

    header = ""

    for header_key in header_keys:
        header = header + """<th scope="col">%s</th>""" % header_key

    body = ""

    for route in routes:
        body = (
            body
            + """
            <tr>
                %s
            </tr>
        """
            % (render_row(route))
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
                <h1>Relatório</h1>
                %s
                <h2>
                    <b>Conclusão da análise:</b>                    
                </h2>
                <h3>Com base nos dados emitidos conclui-se que, %s a construção da ferrovia. </h3>
            </body>
        </html>
    """ % (
        table,
        "é viável" if is_viable else "não é viável",
    )

    return body
