import random

print("Ingrese limite fila")
lim_fila = int(input())

fila = []
fila2 = []
aux = 0

for i in range(0,lim_fila):
  num =  random.randint(1,9)
  fila.append(num)


for i in range(len(fila)):
  for n in range(len(fila)):
      if i != n :
          if fila[i] != fila[n] and fila[i] not in fila2:
              fila2.append(fila[i])

print(fila)
print(fila2)

