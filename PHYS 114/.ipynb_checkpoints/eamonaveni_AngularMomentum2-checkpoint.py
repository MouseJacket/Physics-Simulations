from vpython import *
#Web VPython 3.2

M = 2 
Lrod = 1 
R = 0.1 
Laxle = 4*R 
I = (1/12.)*M*Lrod**2 + (1/4.)*M*R**2 #moment of intertia for thick rod about middle
t = 0 
theta = 0
dtheta = 0
L = vector(0,0,0) 
torque = vec(0,0,2)
dt = 0.00001
AOR = vector(0,0,1) #Axis of Rotation 
tmax = 7
omega = vec(0,0,0)
omegaDot = 0
dtheta = 0
KErot=0
axleF = vec(0.1,0,0)
axleP = vec(0,0,0)
axleV = vec(0,0,0)
dTorque = 0

g1 = graph(xmin=0,xmax = tmax) 
thetaPlot=gcurve(graph=g1,color = color.red)
omegaPlot=gcurve(graph=g1, color = color.blue)
KEPlot = gcurve(graph=g1,color = color.yellow)
torquePlot = gcurve(graph=g1, color = color.green)
dTorquePlot = gcurve(graph=g1,color=color.orange)

rod = cylinder(pos=vector(-1,0,0), radius=R, color=color.orange, axis=vector(Lrod,0,0))
axle = cylinder(pos=vector(-1+Lrod/2,0,-Laxle/2.), radius=R/6., color=color.red, axis=vector(0,0,Laxle))



# Final part
drag = False
position = vec(0,0,0)
newPos=vec(0,0,0)

def down(evt):
    global drag
    drag = True
    scene.bind('mousemove',move)
    scene.bind('mouseup',up)

def move(evt):
    global drag
    if drag:
        axle.pos.x= scene.mouse.pos.x

def up(evt):
    global drag
    global position
    if drag:
        position = scene.mouse.pos
        scene.unbind('mousedown',down)
        scene.unbind('mousemove',move)
        scene.unbind('mouseup',up)
        
print("Drag axle left or right to set initial position")
scene.bind('mousedown',down)
scene.waitfor('mouseup')
newPos=position
print(f"{newPos=}")
if newPos.x < -2*Laxle: 
    axle.pos.x= -2*Laxle 
elif newPos.x>2*Laxle:
    axle.pos.x=2*Laxle 
else:
    axle.pos.x=newPos.x

while t<tmax:
    rate(10000)
    #Added for 11.87, not certain I understand what is being asked of me here, my apologies if I misinterpretted instructions.
    axleP += axleF*dt
    axleV = axleP/M
    axle.pos += axleV*dt
    rod.pos += axleV*dt#= axle.pos.x-(Lrod/2)
    
    
    #11.86
    dTorque = ((3 * cos(5*t))-torque.z)*1000
    torque = vec(0,0,3 * cos(5*t))
    L += torque*dt
    omega = L/I
    omegaDot = dot(omega, norm(AOR))
    dtheta = omegaDot * dt
    rod.rotate(angle = dtheta, axis=AOR, origin=axle.pos)
    theta += dtheta
    KErot = 0.5*(I*(omegaDot**2))
    thetaPlot.plot(pos=(t,theta))
    omegaPlot.plot(pos=(t,mag(omega)))
    torquePlot.plot(pos=(t,mag(torque)))
    KEPlot.plot(pos=(t,KErot))
    if t > 0: #Avoiding initial value spike
        dTorquePlot.plot(pos=(t,dTorque))
    t+=dt
    
print(f'{mag(omega)=:.2f}\n{theta=:.2f}')