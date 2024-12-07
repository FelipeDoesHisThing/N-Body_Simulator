from definitions import *

# Initialization Functions
def twoBP():
  G = 4 * (np.pi ** 2)
  
  M0 = 1
  M1 = 1
  
  m = (M0 * M1) / (M0 + M1)
  
  loc = 1
    
  v0 = np.sqrt(G * m / (2*loc))
  
  # Body 0
  pos0 = np.array([loc, 0, 0]) 
  vel0 = np.array([0, v0, 0])
  
  
  # Body 1
  pos1 = np.array([-loc, 0, 0]) 
  vel1 = np.array([0, -v0, 0])
  
  
  pos = np.array([pos0, pos1])
  vel = np.array([vel0, vel1])
  M = np.array([M0, M1])
  col = np.array(["#FC6255", "#58C4DD"])
  rad = np.array([0.05, 0.05])
  
  CelestialBody.setGravConst(G)
  
  return M,pos,vel,col,rad

def solarSystem():
  ## Initializing Initial Conditions
  G = 4 * np.pi**2 
  
  # Sun
  pos0 = np.array([0, 0, 0]) 
  vel0 = np.array([0, 0, 0])
  M0 = 1
  
  # Mercury
  pos1 = np.array([0.3877005348 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / 0.3877005348)
  vel1 = np.array([0, v , 0]) # in AU/year
  M1 = 1.652e-7 # In solar masses
  
  # Venus
  pos2 = np.array([0.7279411765 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / 0.7279411765)
  vel2 = np.array([0, v , 0]) # in AU/year
  M2 = 2.447e-6 # In solar masses
  
  # Earth
  pos3 = np.array([1, 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos3[0])
  # vel3 = np.array([0, 6.27777651918 , 0]) # in AU/year
  vel3 = np.array([0,v,0])
  M3 = 0.000003 # In solar masses
  
  # Mars
  pos4 = np.array([1.524064171 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos4[0])
  vel4 = np.array([0, v , 0]) # in AU/year
  M4 = 3.213e-7 # In solar masses
  
  # Jupiter
  pos5 = np.array([5.063770053 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos5[0])
  vel5 = np.array([0, v , 0]) # in AU/year
  M5 = 9.543e-4 # In solar masses

  # Saturn
  pos6 = np.array([9.639037433 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos6[0])
  vel6 = np.array([0, v , 0]) # in AU/year
  M6 = 2.857e-4 # In solar masses
  
  # Uranus
  pos7 = np.array([19.1909893 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos7[0])
  vel7 = np.array([0, v , 0]) # in AU/year
  M7 = 4.365e-5 # In solar masses
  
  # Neptune
  pos8 = np.array([29.88970588 , 0, 0]) # In AU
  v = np.sqrt(G * M0 / pos8[0])
  vel8 = np.array([0, v , 0]) # in AU/year
  M8 = 5.149e-5 # In solar masses
  
  # Adding all to arrays
  pos = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]
  vel = [vel0, vel1, vel2, vel3, vel4, vel5, vel6, vel7, vel8]
  M = [M0,M1,M2,M3,M4,M5,M6,M7,M8]
  col = ["#FFFF00", "#888888", "#FF862F", "#58C4DD", "#FC6255", "#8B4513", "#CD853F", "#9CDCEB", "#1C758A"]
  rad = np.array([0.05, 0.001, 0.001, 0.001, 0.0001, 0.001, 0.001, 0.001, 0.001, 0.001]) / 4
  
  CelestialBody.setGravConst(G)
  
  return M,pos,vel,col,rad

def figure8():
  G = 1

  v = np.array([0.3471128135672417, 0.532726851767674, 0])
  
  pos1 = np.array([1, 0, 0])
  pos2 = np.array([-1, 0, 0])
  pos3 = np.array([0, 0, 0])
  
  vel1 = v
  vel2 = v
  vel3 = -2 * v
  
  M = np.array([1,1,1])
  
  pos = [pos1,pos2,pos3]
  vel = [vel1,vel2,vel3]
  col = ["#FFFFFF", "#58C4DD", "#FC6255"]
  
  rad = [0.05/2, 0.05/2, 0.05/2]

  CelestialBody.setGravConst(G)
  
  return M, pos, vel,  col, rad
  
def orbitingFig8():
  G = 1
  
  r = 25
  
  v = np.array([0.3471128135672417, 0.532726851767674, 0])
  
  pos1 = np.array([1, 0, 0])
  pos2 = np.array([-1, 0, 0])
  pos3 = np.array([0, 0, 0])
  
  pos4 = np.array([1, 0, 0]) + np.array([1,0,0]) * r
  pos5 = np.array([-1, 0, 0]) + np.array([1,0,0]) * r
  pos6 = np.array([0, 0, 0]) + np.array([1,0,0]) * r
  
  pos7 = np.array([1, 0, 0]) - np.array([1,0,0]) * r
  pos8 = np.array([-1, 0, 0]) - np.array([1,0,0]) * r
  pos9 = np.array([0, 0, 0]) - np.array([1,0,0]) * r
  
  pos10 = np.array([1, 0, 0]) + np.array([0,1,0]) * r
  pos11 = np.array([-1, 0, 0]) + np.array([0,1,0]) * r
  pos12 = np.array([0, 0, 0]) + np.array([0,1,0]) * r
  
  pos13 = np.array([1, 0, 0]) + np.array([0,-1,0]) * r
  pos14 = np.array([-1, 0, 0]) + np.array([0,-1,0]) * r
  pos15 = np.array([0, 0, 0]) + np.array([0,-1,0]) * r

  vel1 = v
  vel2 = v
  vel3 = -2 * v
  
  v2 = np.sqrt(G * 3  / r) 
    
  vel4 = v + v2 * np.array([0,1,0]) 
  vel5 = v + v2 * np.array([0,1,0]) 
  vel6 = -2 * v + v2 * np.array([0,1,0]) 
  
  vel7 = v - v2 * np.array([0,1,0]) 
  vel8 = v - v2 * np.array([0,1,0]) 
  vel9 = -2 * v - v2 * np.array([0,1,0]) 
  
  vel10 = v + v2 * np.array([-1,0,0]) 
  vel11 = v + v2 * np.array([-1,0,0]) 
  vel12 = -2 * v + v2 * np.array([-1,0,0]) 
  
  vel13 = v + v2 * np.array([1,0,0]) 
  vel14 = v + v2 * np.array([1,0,0]) 
  vel15 = -2 * v + v2 * np.array([1,0,0]) 
  
  M = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
  
  pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9, pos10, pos11, pos12, pos13, pos14, pos15]
  vel = [vel1,vel2,vel3,vel4,vel5,vel6,vel7,vel8,vel9, vel10, vel11, vel12, vel13, vel14, vel15]
  col = ["#FFFFFF", "#58C4DD", "#FC6255"] * 5
  
  rad = [0.05/2, 0.05/2, 0.05/2] * 5
  
  CelestialBody.setGravConst(G)
  
  return M, pos, vel, col, rad
