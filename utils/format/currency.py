def to_currency(value):
  currency_format = 'R$ {:,.2f}'
  return currency_format.format(value)