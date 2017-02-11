m1=int(input("enter the marks of sub1= "))
m2=int(input("enter the marks of sub2= "))
m3=int(input("enter the marks of sub3= "))
m4=int(input("enter the marks of sub4= "))
m5=int(input("enter the marks of sub5= "))
su=m1+m2+m3+m4+m5
mean=su/5
perc=(su/500)*100
print(mean)
if perc>35:
  print("pass")
else:
  print("fail")
