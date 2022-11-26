z=input("Input time in hh:mm (24 hours notation) format: ")
a=int(z[0]+z[1])
# a is position of hour hand
b=int(z[3]+z[4])
# b is position of minutes 
dh=0
dm=0
if a<25 and b<61:
    if a>12:
        a=a-12
        dm=b*6
        dh=(30*a)+(dm*(30/360))
    else:
        dm=b*6
        dh=(30*a)+(dm*30/360)
    if dm>dh:
        d=dm-dh
    else:
        d=dh-dm
    if d>180:
        print("Angle between minute hand and minutes :",(360-d),'°')
    else:
        print("Angle between minute hand and minutes :",d,'°')
else:
    print('Please enter valid time in hh:mm  format')
