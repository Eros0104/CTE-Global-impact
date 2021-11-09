def generate_user_tax_report(tax_value, kilometer, travel):
  print("| %50s | %10i | %20s |" % (travel, kilometer, tax_value))

def generate_user_tax_line():
  print("+" + "=" * 52 + "+" + "=" * 12 + "+"+ "=" * 22 +"+")

def generate_user_tax_header():
  generate_user_tax_line()
  print("| %50s | %10s | %20s |" % ("Trechos", "Km", "Tarifa ao passageiro"))
  generate_user_tax_line()