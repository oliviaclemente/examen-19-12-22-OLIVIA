from datetime import date 
from dateutil.relativedelta import relatividelta


def edad(nac):
  hoy = datetime.date.today()
  if hoy<nac:
    print("No es prosibe!!")
  else:
    año=nac.year
    mes= nac.month
    dia= nac.day
    fecha= nac
    edad= 0
    while fecha< hoy:
      edad += 1
      fecha = datetime.date(año + edad, mes, dia)
    print("Tengo",(edad-1),"años")
  return edad
    
edad(datetime.date(10, 03, 2004))

def c_e(f_n):
  edad= date.today().year - f_n.year
  cumple= f_n + relativedelta    