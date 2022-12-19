from datetime import date 
from dateutil.relativedelta import relativedelta

def c_e(f_n):
  edad= date.today().year - f_n.year
  cumple= f_n + relativedelta(years=edad)
  if cumple > date.today():
    edad= edad -1
  return edad

c_e(date(2004,10,10))

def c_e(f_n):
  today= fecha.today()
  try:
    cumple= naci.replace(año= today.year)
  excepy ValueError:
    cumple= naci.replace( año = today.year)
  if cumple > today:
    return today.yaer - naci.year -1
  else:
    returm today.year