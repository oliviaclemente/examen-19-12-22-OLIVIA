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
      
    