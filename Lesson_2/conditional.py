import math
# a=10
# b=20
# print("a>b",a>b)
# print("a<b",a<b)
# print("a=b",a==b)
# a=500
# b=600
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is not greater than b")
# print("Done")
# c=int(input("How old are you?"))
# if c<=20:
#     print("You can be discounted up to 10%")
# elif 20<c<=30:
#     print("You can be discountd up to 20%")
# elif 30<c<=40:
#     print("You can be discounted up to 30%")
# else:
#     print("You can be discounted up to 50%")
Weight=input("How much do you weigh? (in kg)")
Height=input("How tall are you (in m)")
BMI= int(Weight)/(float(Height)**2)
print("Your BMI is",BMI)
# if BMI<=18.5:
if not(BMI>18.5):
    print("Gay")
# elif 18>BMI and BMI<=22.9:
elif not (BMI<18 and BMI>22.9))
    print("Binh thuong")
else:
    print("Thua can")
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# Delta=float(b**2-4*a*c)
# if Delta>0:
#     x1=(-b+sqrt(Delta))/2*a
#     x2=(-b-sqrt(Delta))/2*a
#     print("x1=",x1)
#     print("x2=",x2)
# elif Delta==0:
#     x=-b/(2*a)
# else:
#     print("Khong co nghiem thuc")