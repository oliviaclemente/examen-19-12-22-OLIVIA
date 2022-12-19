x=y=i=0
n=100

while (i<n):
  aleatorio=random.randrange(1,9)
  print(aleatorio)
  if(aleatorio==1):
    x=x+1
    y=y+2
    print("primera posicion caballo(",x,",",y,")")
  if(aleatorio==2):
    if(x+2<9 and y+1<9):
      x= x+2
      y= y+1
      print("segunda posicion caballo(",x,",",y,")")
  if(aleatorio==3):
    if(x+2<9 and y-1<9):
      x= x+2
      y= y-1
      print("tercera posicion caballo(",x,",",y,")")
  if(aleatorio==4):
    if(x+1<9 and y-2>0):
      x= x+1
      y= y-2
      print("cuarta posicion caballo(",x,",",y,")")
  if(aleatorio==5):
    if(x-1>0 and y+2<9):
      x= x-1
      y= y+2
      print("quinta posicion caballo(",x,",",y,")")
  if(aleatorio==6):
     if(x-2>0 and y+1<9):
      x= x-2
      y= y+1
      print("sexta posicion caballo(",x,",",y,")")
  if(aleatorio==7):
     if(x-2>0 and y-1>0):
      x= x-2
      y= y-1
      print("septima posicion caballo(",x,",",y,")")
  if(aleatorio==8):
     if(x-1>0 and y-2>0):
      x= x-1
      y= y-2
      print("octava posicion caballo(",x,",",y,")")
i += 1
