
def tri(num):
  if(num==0):
    return 0
  elif(num==1):
    return 1
  elif(num==2):
    return 2
  else:
    return (tri(num-3)+tri(num-2)+ tri(num-1))
n=int(input("Tribonacci:"))
for n in range (0,n):
  print(tri(n))

#he creado una funcion de fibonacci pero añadiendo mas para que fuese de tribonacci