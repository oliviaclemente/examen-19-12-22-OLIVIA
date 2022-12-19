max_num=999
unidades= ("cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve")
numero= int(input("Introduce un numero:"))

def num(numero):
  ne=int(numero)
  if ne>max_num:
    raise OverflowError("Numero muy alto")
  if ne<0:
    raise na(abs(numero))
  le=''
  pd= int(round((abs(numero)-abs(ne)) *100))
  if ne>9:
    ne= na(pd)
  elif pd >0:
    ld= na(pd)
  if (ne <= 999):
    res= unidades
  return num


def num(numero):
  ne=int(numero)
  if ne>max_num:
    raise OverflowError("Numero muy alto")
  if ne<0:
    raise OverflowError("Numero muy alto")
  if n<9:
    unidades = pos -1
  else:
    n1= numero.split()
    unidades = pos(n1)
  return num(numero)