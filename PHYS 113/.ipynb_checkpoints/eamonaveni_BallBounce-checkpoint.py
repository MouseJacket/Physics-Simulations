from vpython import *
#Web VPython 3.2

R=0.3 
L = 10  
H = 0.2
dt=0.01  #Time.deltaTime
tmax=10. #Time max
t=0. #Current Time
g=9.8 #Gravitational accelaration
v0=8. #Initial velocity
theta=pi/3 

Xaxis=box(pos=vector(L/2.,-H/2.,0), length=L, height=H, width=L/3., texture=textures.wood)
#these next couple of lines point the “camera” inside of vpython
scene.autoscale=0 
scene.center=vector(L/2., 0.4*L, 0)
scene.forward=vector(0, -0.2, -0.9)
scene.scale=0.7*L 
ball = sphere(pos = vector(0,0,0), radius = R, color=color.blue)
ball.pos.y=H+R
ball.pos.x=L/4
ball.v=vector(v0*cos(theta),v0*sin(theta),0)
trail=curve(color=color.red)

a = -g * vector(0, 1, 0) 

while (t < tmax): 
    rate(1./dt) 
    ball.v+=a*dt
    ball.pos=ball.pos+ball.v*dt 
    trail.append(ball.pos) 
    t=t+dt  
    if ((ball.pos.y < ball.radius) & (ball.v.y  < 0) & (ball.pos.x<L)): 
        print('BOUNCE')
        ball.v.y*=-1
    print(t) 
print('Now I am done.') 