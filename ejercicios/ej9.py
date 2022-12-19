from datetime import date 

def c_e(f_n):
  today= date.today()
  try:
    cumple= naci.replace(año= today.year)
  except ValueError:
    cumple= naci.replace( año = today.year)
  if cumple > today:
    return today.yaer - naci.year -1
  else:
    return today.year - naci.year
print(calculateAge(date(2004, 10, 2)), "years")