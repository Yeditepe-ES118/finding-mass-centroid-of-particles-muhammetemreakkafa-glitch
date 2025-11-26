#np.array for vec def
#np.sum for summation   
#return tot_mass cx cy
import numpy as np

def centroid(p1x,p1y,p2x,p2y,p3x,p3y,m1,m2,m3):
    positions=np.array([[p1x,p2x,p3x],[p1y,p2y,p3y]])
    mass=np.array([m1,m2,m3])
    cx=np.sum(positions[0,:]*mass)/np.sum(mass)
    cy=np.sum(positions[1,:]*mass)/np.sum(mass)
    tot_mass=np.sum(mass)

    return tot_mass,cx,cy

   
