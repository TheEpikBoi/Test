import math
print("For ax² + bx + x = 0")
print(" ")
a = input("a = ")
if a == str(0):
  print(" ")
  print("a≠0")
  quit()
try:
    a = float(a)
except ValueError:
      print("Please Type a Numeric Value")
      quit()
b = input("b = ")
try:
    b = float(b)
except ValueError:
      print("Please Type a Numeric Value")
      quit()
c = input("c = ")
try:
    c = float(c)
except ValueError:
      print("Please Type a Numeric Value")
      quit()
print(" ")
D = (b * b) - (4 * a * c)
xv = (-b)/(2*a)
yv = (-D)/(4*a)
if D < 0:
   D = -D
   print("No real roots")
   print(" ")
   xa = (-b) / (2*a)
   xb = D / (2*a)
   print("1st Imaginary Root=")
   print(str(xa) + " + " + str(xb) + "i")
   print("2nd Imaginary Root=")
   print(str(xa) + " - " + str(xb) + "i")
   print("                   {Where 'i' = √(-1)}")
   print(" ")
   print("Discriminant=", -D)
   print(" ")
   print("Vertex=")
   print("(" + str(xv) + "," + str(yv) + ")")
   print(" ")
   print("Range=")
   if a > 0:
     print("[" + str(yv) + ",∞" + ")")
   elif a < 0:
       print("(" + "-∞," + str(yv) + "]")
   quit()
else:
     x1 = ((-b) + math.sqrt(D)) / (2*a)
     x2 = ((-b) - math.sqrt(D)) / (2*a)
print("1st Root=")
print(x1)
print("2nd Root=")
print(x2)
print(" ")
print("Discriminant=")
print(D)
print(" ")
print("Square Root of Discriminant=")
print(math.sqrt(D))
print (" ")
print("Vertex=")
print("(" + str(xv) + "," + str(yv) + ")")
print(" ")
print("Range=")
if a > 0:
  print("[" + str(yv) + ",∞" + ")")
elif a < 0:
  print("(" + "-∞," + str(yv) + "]")
