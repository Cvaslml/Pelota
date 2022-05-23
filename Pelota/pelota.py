"""Calcular h de una pelota que rebota"""

print("---------------------------------")
print("-------------Pelota--------------")
print("---------------------------------")

#Input
h = int(input("Ingrese su altura h: "))

#Processing
q = h/5
n = 0
while (h > q):
    h = h - (0.1*h)
    n = n + 1

#Output
print("La pelota lanzada no alcanza a subir a la quinta parte del rebote inicial, en el rebote: " + str(n) + " y su altura: " + str(h)) 