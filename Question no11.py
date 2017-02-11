def intr(p,r,t):
  n=r/t
  d=t*t
  i=(p*((1+n)**(d)))-p
  print(n)
  print(d)
  print(i)
a=float(input("Principle="))
b=float(input("Rate="))
c=int(input("Time(in year)="))
intr(a,b,c)
