from vpython import *

my_canvas1 = canvas(title = "my New Canvas", width=600, height=400) #new canvas

M = 1 #1 solar mass
G = 4*pi**2 #G in solar masses, AU and years (rather than kg, meters and seconds)
v_use = 0.5*6.28 #speed (keeping equal to half the earths orbital speed) in AU/year
t = 0 #starting time
tfinal = 50 #run for 50 years
dt = 0.005 #a 100th of a year for the timestep

my_canvas1.range = 10

star1 = sphere(pos = vec(1.0,0,0), radius = 0.2, color = color.red, v=vec(0,v_use,0), m=M, Fsum = vec(0,0,0), make_trail = True) #star 1
star2 = sphere(pos = vec(-1.0,0,0), radius = 0.2, color = color.blue, v=vec(0,-v_use,0), m=M, Fsum = vec(0,0,0), make_trail = True) #star 2

objects = [] #list of all objects in the system for calculation of forces
objects.append(star1) #appending objects to the list
objects.append(star2)

NewStar = False #boolian flag telling us we haven't yet added the third star

while t<tfinal:
    rate(40)
    if NewStar==False and t>=1.5: #letting simulation run for a bit before adding third star
        print("please click location of 3rd star")
        loc = my_canvas1.waitfor('click')
        NewStar = True #changing variable to keep from running this if statement again
        objects.append(sphere(pos=loc.pos, radius = 0.2, color = color.yellow, v=vec(v_use,0,0), m=M, Fsum = vec(0,0,0), make_trail = True)) #3rd star!
    for i in range(len(objects)):
        for k in range(i+1,len(objects)):
            dist = mag(objects[i].pos-objects[k].pos) #distance between stars
            Force1 = -G * (objects[i].m*objects[k].m)*(objects[i].pos-objects[k].pos)/(pow(dist,3)) #calculating force pairs
            objects[k].Fsum += -Force1 #incrementing the sum of forces on each object
            objects[i].Fsum += Force1 #force pair
        objects[i].v += (objects[i].Fsum/objects[i].m)*dt #adjusting the velocity
        objects[i].pos += objects[i].v*dt #adjusting the position
        objects[i].Fsum = vec(0,0,0) #resetting the force
    t+=dt #incrementing the current time