from manimlib import *
import numpy as np
import matplotlib.pyplot as plt

# Class Definition
class CelestialBody:
  bodies = [] # List contains all instances of object CelestialBody
  G = 6.6743e-11
  
  # NEED TO FIX INPUT G PARAMETER OR SOMETHING
  def initBodies(initFunc):
    pos, vel, M, col, rad = initFunc()
    
    # Initializing bodies in scene with initial conditions
    for i in range(len(M)):
      CelestialBody(M[i], pos[i], vel[i], radius = rad[i], color = col[i])
  
  def setGravConst(G):
    CelestialBody.G = G
  
  def __init__(self, mass, pos, vel, radius = 0.1, color = "#FFFFFF"):
    CelestialBody.bodies.append(self)
    # Initializing
    self.__pos = np.array(pos, dtype='d') # Initializing initial position
    self.__vel = np.array(vel, dtype='d') # Initializing initial velocity
    self.__mass = mass # Storing mass
    self.__radius = radius # Storing radius for animation
    self.__color = color # Storing color for animation
    
    self.bodyNum = len(CelestialBody.bodies) # Setting body number in array containing all bodies

  # Getters
  def getPos(self):
    return self.__pos
  
  def getVel(self):
    return self.__vel
  
  def getMass(self):
    return self.__mass
  
  def getRadius(self):
    return self.__radius
  
  def getColor(self):
    return self.__color
  
  # Setters
  def setPos(self, pos):
    self.__pos = pos
  
  def setVel(self, vel):
    self.__vel = vel
  
  def addPos(self, pos):
    self.__pos += pos
  
  def addVel(self, vel):
    self.__vel += vel
  
  def setMass(self, mass):
    self.__mass = mass
  
  def setRadius(self, radius):
    self.__radius = radius
  
  def setColor(self, color):
    self.__color = color
  
  # RK4 Functions
  def getK(poss, vels, mass):
    # Initializing variables
    accs = np.zeros((len(CelestialBody.bodies),3))
    
    # Turning into numpy array
    poss = np.array(poss)
    vels = np.array(vels)
    
    # Loop through the contribution of every "other" body
    for i in range(len(CelestialBody.bodies)):
      # np.delete makes sure the contributions from other bodies are taken into account
      possCurr = np.delete(poss, i, axis = 0) # Positions of "other" bodies
      massCurr = np.delete(mass, i, axis = 0) # Mass of "other" bodies
      
      for j in range(len(CelestialBody.bodies) - 1):
        # Add contributions to the acceleration due to every "other" body
        accs[i] -= CelestialBody.G * massCurr[j] * ((poss[i] - possCurr[j]) / np.linalg.norm(poss[i] - possCurr[j]) ** 3)
    
    return [vels, accs]
    
  def RK4_step(dt):
    # Initializing empty arrays to store "K" values for Runge-Kutta algorithm 
    # for position and velocity independently
    KR = np.zeros((4,len(CelestialBody.bodies),3))
    KV = np.zeros((4,len(CelestialBody.bodies),3))
    
    # Initializing empty arrays to store "K" values for the current step for the Runge-Kutta algorithm
    KRcurr = np.zeros((len(CelestialBody.bodies),3))
    KVcurr = np.zeros((len(CelestialBody.bodies),3))
    
    div = np.array([1,2,2,1]) # This is the constants for each iteration of "K"
    
    # Loop four times as it is RK4 and there are 4 "K's"
    for i in range(4):
      poss = []
      vels = []
      mass = []
      
      # Find input values to calculate the respective "K"
      for body, kr, kv in zip(CelestialBody.bodies, KRcurr, KVcurr):
        poss.append(body.getPos() + kr * dt / div[i])
        vels.append(body.getVel() + kv * dt / div[i])
        mass.append(body.getMass())

      KRcurr, KVcurr = CelestialBody.getK(poss, vels, mass) # Get value of current "K"
      KR[i], KV[i] = KRcurr, KVcurr # Set current K for position and velocity Independently
    
    for i in range(len(CelestialBody.bodies)):
      CelestialBody.bodies[i].addPos((1/6) * div @ KR[:,i] * dt) # Add step
      CelestialBody.bodies[i].addVel((1/6) * div @ KV[:,i] * dt) # Add step

  def solve_RK4(sim_time, dt):
    """Get positions of bodies over a given time interval using RK4 algorithm
    
    Inputs: 
      time: Time interval to simulate over    
      dt: Time step
      G: Gravitational constant, default = 1
    
    Outputs:
      positions: Position of bodies at times t * dt of format
      [[[x1,y1,z1], t],
      [[x2,y2,z2], t],
      ...
      [[xN,yN,zN], t]]
      
    """
    # Initialize empty array for position over time
    positions = np.zeros((len(CelestialBody.bodies), 3, int(sim_time/dt)))
    velocities = np.zeros((len(CelestialBody.bodies), 3, int(sim_time/dt)))
    
    for t in range(int(sim_time/dt)):
      currPos = [] # Current position
      currVel = [] # Current velocity
      
      for body in CelestialBody.bodies:
        currPos.append(body.getPos()) # Append current position to index of body
        currVel.append(body.getVel()) # Append current velocity to index of body

      positions[:,:,t] = currPos # Set position at time t of each body
      velocities[:,:,t] = currVel # Set position at time t of each body
      
      CelestialBody.RK4_step(dt) # Take a RK step
    
    return np.array(positions).T, np.array(velocities).T

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
  col = np.array([RED, BLUE])
  rad = np.array([0.05, 0.05])
  
  CelestialBody.setGravConst(G)
  
  return [pos,vel,M,col,rad]

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
  col = [YELLOW, GREY, ORANGE, BLUE, RED, DARK_BROWN, LIGHT_BROWN, BLUE_B, BLUE_E]
  rad = np.array([0.05, 0.001, 0.001, 0.001, 0.0001, 0.001, 0.001, 0.001, 0.001, 0.001]) / 4
  
  CelestialBody.setGravConst(G)
  
  return [pos,vel,M,col,rad]

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
  col = [WHITE, BLUE, RED]
  
  rad = [0.05/2, 0.05/2, 0.05/2]

  CelestialBody.setGravConst(G)
  
  return pos, vel, M, col, rad
  
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
  col = [WHITE, BLUE, RED] * 5
  
  rad = [0.05/2, 0.05/2, 0.05/2] * 5
  
  CelestialBody.setGravConst(G)
  
  return pos, vel, M, col, rad
