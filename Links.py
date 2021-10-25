# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:42:10 2021

@author: Martín Tobar
"""
import math
import matplotlib.pyplot as plt
def coseno(angulo):
    return math.cos(math.radians(angulo))

#Initialize arrays that hold constants for each angle.
A = [0.0]*360
B = [0.0]*360
C = [0.0]*360
D = [0.0]*360
E = [0.0]*360
F = [0.0]*360
A4O = [0.0]*360
A4C = [0.0]*360
A3O = [0.0]*360
A3C = [0.0]*360

#Length of the links in meters
a = 0.04
b = 0.120
c = 0.08 
d = 0.1

#Constants calculation 
k1 = d/a
k2 = d/c
k3 = (pow(a,2)-pow(b,2)+pow(c,2)+pow(d,2))/(2*a*c)

k4 = d/b
k5 = (-pow(a,2)-pow(b,2)+pow(c,2)-pow(d,2))/(2*a*b)

#print(k1,k2,k3,k4,k5)

#Obtain each constant and auxiliar value for each angle.
for angle in range (360):
    A[angle] = coseno(angle) -k1 - k2*coseno(angle)+k3
    B[angle] = -2*math.sin(math.radians(angle))
    C[angle] = k1- (k2+1)*coseno(angle) + k3 
    #Open theta4
    A4O[angle] = math.degrees(2*math.atan( (-B[angle]-math.sqrt(pow(B[angle],2)-4*A[angle]*C[angle]))/(2*A[angle])   ))
    #Crossed theta 4
    A4C[angle] = math.degrees(2*math.atan( (-B[angle]+math.sqrt(pow(B[angle],2)-4*A[angle]*C[angle]))/(2*A[angle])   ))
    
    
    D[angle] = coseno(angle) - k1 + k4*coseno(angle) + k5
    E[angle] = -2*math.sin(math.radians(angle))
    F[angle] = k1 + (k4-1)*coseno(angle) +k5
     #Open theta3
    A3O[angle] = math.degrees(2*math.atan( (-E[angle]-math.sqrt(pow(E[angle],2)-4*D[angle]*F[angle]))/(2*D[angle])   ))
     #Crossed theta3
    A3C[angle] = math.degrees(2*math.atan( (-E[angle]+math.sqrt(pow(E[angle],2)-4*D[angle]*F[angle]))/(2*D[angle])   ))



#animation

for m_angle in range (0,360,1):

    #For each angle plot each link depending on the position of the angle m_angle which is theta 2.
    L1X = [0,d*1000]
    L1Y = [0,0]
    
    L2X = [L1X[0],L1X[0]+math.cos(math.radians(m_angle))*a*1000]
    L2Y = [L1Y[0],L1Y[0]+math.sin(math.radians(m_angle))*a*1000]
    
    L3X = [L2X[1],L2X[1]+math.cos(math.radians(A3O[m_angle])) *b*1000]
    L3Y = [L2Y[1],L2Y[1]+math.sin(math.radians(A3O[m_angle])) *b*1000]
    
    L4X = [L1X[1],L1X[1]-math.cos(math.radians(180-A4O[m_angle])) *c*1000]
    L4Y = [L1Y[1],L1Y[1]+math.sin(math.radians(180-A4O[m_angle])) *c*1000]
    
   
    plt.title("Movement in function of $\\theta 2$")
    
    #Plot lines aka LINKS
    plt.plot(L1X,L1Y,label =("L1 "+str(d*1000)+" mm"))
    plt.plot(L2X,L2Y,label =("L2 "+str(a*1000)+" mm"))
    plt.plot(L3X,L3Y,label =("L3 "+str(b*1000)+" mm"))
    plt.plot(L4X,L4Y,label =("L4 "+str(c*1000)+" mm"))
    
   
   #Plot angles values
    plt.text(L2X[1]/10,1,"$\\theta_2 = $"+str(m_angle))
    plt.text(L2X[1]+5,L2Y[1]+1,"$\\theta_3 = $"+str(format(A3O[m_angle],".3f")))
    plt.text(L1X[1]+1,L1Y[1]+5,"$\\theta_4 = $"+str(format(A4O[m_angle],".3f")))
    
    #Plot reference lines for angles theta 3 and 4
    plt.plot([L2X[1],L2X[1]+10],[L2Y[1],L2Y[1]],color="black")
    plt.plot([L1X[1],L1X[1]+20],[0,0],color="black")
  
    
    #Add a legend to see which color is each link.
    leg = plt.legend(loc='upper left')
    #Add a grid
    plt.grid()
    #Save the plot on animation folder with the name of the theta2, dpi is for resoultion
    plt.savefig('animation/'+str(m_angle),dpi=300)
    #Show the plot
    plt.show()
