import fechanac

def edad(nac):
  hoy = fechanac.date.today()
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
      fecha = fechanac.date(año + edad, mes, dia)
    print("Tengo",(edad-1),"años")
edad(fechanac.date(10,03,2004))
    