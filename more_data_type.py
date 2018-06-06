a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d = b**2-4*a*c
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        else:
             print("Phuong trinh vo nghiem")
    else:
         print("Phuong trinh co nghiem duy nhat la:",-c/b)
else:
    if d<0:
        print("Phuong trinh vo nghiem")
    if d==0:
        print("Phuong trinh co nghiem kep la: x=", -b/2/a)
    if d > 0:
        print("Phuong trinh co 2 nghiem phan biet la: x1=", -b/2/a+d**0.5/2/a,", x2=",-b/2-d**0.5/2/a)
