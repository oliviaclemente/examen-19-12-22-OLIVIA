max_num=999
unidades= ("cero","uno";"dos","tres","cuatro","cinco","seis","siete","ocho","nueve")

def num(numero):
  ne=int(numero)
  if ne>max_num:
    raise OverflowError("Numero muy alto")
  if ne<0:
    raise OverflowError("Numero demasiado bajo")
  if ne>9:
    
    
    
