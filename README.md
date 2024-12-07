# The N-Body Simulator
<p align="center">
  <a>
    <img width = 800, src = "https://github.com/cfelipesandoval/N-Body_Simulator/blob/de6ad6de566236adcec073c5a103c80398c33889/images/Front_image3.png"
  </a>
</p>

This tool sets out to create a framework to easily create simulations for planetary motion.

## Using the Tool
### Creating Instances
Each body is created as an instance of the class CelestialBody, which can be initialized as
```python
planet = CelestialBody(mass, positionVector, velocityVector)
```
You can look at the class definition and its parameters in definitions.py.

The position and velocity vectors are expected to be numpy arrays which you can initialize as
```python
import numpy as np
positionVector = np.array([x,y,z])
velocityVector = np.array([vx,vy,vz])
```
Creating an instance automatically adds that body to the list of bodies in the scene. 

I recommend initializing by first setting all the parameters and initializing by
```python
M = [mass1, mass2 ... , massN]
pos = [pos1, pos2, ... , posN]
vel = [ve1, vel2, ... , velN]

for i in range(len(M)):
  CelestialBody(M[i], pos[i], vel[i], radius = rad[i], color = col[i])
```
You can also access individual instances with CelestialBody.bodies[instanceNumber] 

### Simulating
After initializing all bodies, you can run by using the createSim class method of the CelestialBody class

```python
sim_time = 10 # Example Simulation time
dt = 0.01 # Example Time Step
CelestialBody.createSim(sim_time, dt)
```




You can take a look at the example function in the main.py file.
