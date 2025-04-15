import numpy as np

# inputs
a=float(input("a:"))
b=float(input("b:"))
sn=int(input("sn:"))
t = np.arange(np.pi, 2*np.pi,0.0001); # pi=<t=<2pi
x=np.cos(t);
y=np.sin(t);
theth_direction_x = -np.sin(t);
thetha_direction_y=np.cos(t);
dx=-np.sin(t);
dy=np.cos(t);
F1_x=a*np.cos(np.pi/6);
F1_y=a*np.sin(np.pi/6);

#sn1
# integral (pi,2pi)F1_x*-sin(t)dt + integral (pi,2pi) F1_y*cos(t)dt # be awre if F = xx^ + yy^ for exmpale we have to change F to F = cos(t)x^ + sin(t)y^ becuase we do intragle by dt
w1_x_integral =F1_x*dx;
w1_y_integral = F1_y*dy;
w1_x=np.sum(0.0001*w1_x_integral);
w1_y=np.sum(0.0001*w1_y_integral);
W1=w1_x+w1_y;

#sn2
#calcualte F2 the opposite directrion of theta^ opposite to the vector of velocity v
F2_x=b*(-theth_direction_x);
F2_y=b*(-thetha_direction_y);
#calculate the numerial integral of Fx-sin(t) +Fycos(t)  t0=pi to t1=2pi 
w2_x = np.sum(0.0001*F2_x*dx);
w2_y=np.sum(0.0001*F2_y*dy);
W2= w2_x+w2_y;

#sn3
#F3_x=-ay^2 --> F3_x = -a(sin(t))^2 , F3_y = bx^3y --> F3_y = b(cos(t))^3*sin(t)
F3_x=-a*y**2;
F3_y=b*(x**3)*y;
#calcualte numerial integral Fxdx + Fydy t0=pi to t1=2pi
w3_x=np.sum(0.0001*F3_x*dx);
w3_y=np.sum(0.0001*F3_y*dy);
W3=w3_x+w3_y;

#sn4
# now the movment eqution is y=0 and x [-1,1] the object move in stright line form (-1,0) to (1,0)
# if y=0 we get Fx=-a*0^2 and Fy=b*x^3*0 in conclution F force dont affect on the object if he is moving only on the x-axis (no change in y)
W4=0;

#sn5 
# the answer is no the F force is not conservative force beacsue the work of a conservative force  is not depends on the eqution movment
# and here we did stright line movment and got Wf=0 and on the half circle movment Wf=!0 so this force does depende on the movment eqition there for not a conservative force 
ans5=2;

if sn==1:
    print(W1)
elif sn==2:
    print(W2)
elif sn==3:
    print(W3)
elif sn==4:
    print(W4)
elif sn==5:
    print(ans5)