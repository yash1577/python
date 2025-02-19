#use of AND and OR 

per = int(input("enter your percentage in integer: "))
if per>=0 and per<40:
    print("fail")
if per>=0 and per<50:
    print("third")
if per>=60 and per<=100:
    print("first")
if per>100 or per<0:
    print("error")
if per>=50 and per<60:
    print("second")