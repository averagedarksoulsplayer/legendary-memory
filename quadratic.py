import cmath
print("\033[4mbasic quadrtratic solver\033[0m")
print("ax^2+bx+c=0")
a = float(input("enter value of a :"))
b = float(input("enter value of b :"))
c = float(input("enter value of c :"))
disc = float(b)* float(b)-4*float(a)*float(c)
if float(disc)< 0:
    print("no real root")
else:
      sol1 = (-b+cmath.sqrt(disc))/(2*a)
      sol2 =  (-b-cmath.sqrt(disc))/(2*a)

      print(str("slolution 1 : "),   sol1)
      print(str("solution 2  : ") ,  sol2)
