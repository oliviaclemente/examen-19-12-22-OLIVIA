x=y=i=0
n=100

while (i<n):
  aleatorio=random.randrange(1,9)
  print(aleatorio)
  if(aleatorio==1):
    x=x+1
    y=y+2
    print("primera pos caballo:(",x,",","")
  if(aleatorio==2):
    if(x+1<9 and y+2<9):
      x= x+2
      y= y+1
      print()