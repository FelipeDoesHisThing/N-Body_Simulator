# Scenes
from definitions import *
from init import *
from manimlib import *


# Manim scenes
class TwoBP(Scene):
  def construct(self, sim_time, dt, run_time, animate=True, savefile=None):
    CelestialBody.initBodies(twoBP)
    
    # Solving using RK4
    [positions, velocities] = CelestialBody.createSim(sim_time, dt)

    # Saving results
    if(savefile is not None):
      with open(savefile, 'wb') as f:
        np.save(f, positions)
    
    if(animate):
      axes = Axes(
                        x_range=[-2,2,1],
                        y_range=[-2,2,1]
      )
      
      curves = VGroup()
      for i in range(len(CelestialBody.bodies)):
        curve = VMobject().set_points_as_corners(positions[:,i])
        curve.set_stroke(CelestialBody.bodies[i].getColor())
        curves.add(curve)
      
      dots = Group(GlowDot(color = body.getColor(), radius = body.getRadius()) for body in CelestialBody.bodies)
      
      tail = VGroup(
          TracingTail(dot, time_traced=run_time/10).match_color(dot)
          for dot in dots)

      curves.set_opacity(0)
      
      frame = self.camera.frame
      
      def updateDots(dots):
        for dot, curve in zip(dots, curves):
          dot.move_to(curve.get_end())

      frame.set_height(dots[0].get_center() + 6)
      frame.move_to(dots.get_center_of_mass())
      dots.add_updater(updateDots)    
      
      self.play(FadeIn(dots),FadeIn(axes))
      self.add(tail)
      self.play(*(ShowCreation(curve, rate_func = linear, run_time = run_time) for curve in curves))
      self.play(*[FadeOut(mob) for mob in self.mobjects])

    CelestialBody.bodies.clear()

    return [positions, velocities]
    
class SolarSystem(Scene):
  def construct(self, sim_time, dt, run_time, animate=True, savefile=None):
    CelestialBody.initBodies(solarSystem)
    
    [positions, velocities] = CelestialBody.createSim(sim_time, dt)

    # Saving results
    if(savefile is not None):
      with open(savefile, 'wb') as f:
        np.save(f, positions)
    
    if(animate):
      curves = VGroup()
      for i in range(len(CelestialBody.bodies)):
        curve = VMobject().set_points_as_corners(positions[:,i])
        curve.set_stroke(CelestialBody.bodies[i].getColor())
        curves.add(curve)
      
      dots = Group(GlowDot(color = body.getColor(), radius = body.getRadius()) for body in CelestialBody.bodies)
      
      tail = VGroup(
          TracingTail(dot, time_traced=run_time/5).match_color(dot)
          for dot in dots)

      curves.set_opacity(0)
      
      frame = self.camera.frame
      
      def updateDots(dots):
        for dot, curve in zip(dots, curves):
          dot.move_to(curve.get_end())

      frame.set_height(dots[0].get_center() + 10)
      dots.add_updater(updateDots)          
      
      self.play(FadeIn(dots))
      self.add(tail)
      self.play(*(ShowCreation(curve, rate_func = linear, run_time = run_time) for curve in curves),
                frame.animate.set_height(dots[0].get_center() + 50).set_anim_args(run_time = run_time, rate_func = there_and_back))
      self.play(*[FadeOut(mob) for mob in self.mobjects])

    CelestialBody.bodies.clear()
    
    return [positions, velocities]
    
class Figure8(Scene):
  def construct(self, sim_time, dt, run_time, animate=True, savefile=None):
    CelestialBody.initBodies(figure8)
    
    [positions, velocities] = CelestialBody.createSim(sim_time, dt)

    # Saving results
    if(savefile is not None):
      with open(savefile, 'wb') as f:
        np.save(f, positions)
    
    if(animate):
      curves = VGroup()
      for i in range(len(CelestialBody.bodies)):
        curve = VMobject().set_points_as_corners(positions[:,i])
        curve.set_stroke(CelestialBody.bodies[i].getColor())
        curves.add(curve)
      
      dots = Group(Sphere(color = body.getColor(), radius = body.getRadius()) for body in CelestialBody.bodies)
      
      def updateDots(dots):
        for dot, curve in zip(dots, curves):
          dot.move_to(curve.get_end())
      
      self.add(dots)
      dots.add_updater(updateDots)
      
      tail = VGroup(
          TracingTail(dot, time_traced =  2).match_color(dot)
          for dot in dots
      )
      
      self.add(tail)
      
      frame = self.camera.frame

      frame.move_to(ORIGIN)
      frame.set_height(ORIGIN + 3)
      
      curves.set_opacity(0)
      
      self.play(*(ShowCreation(curve, run_time = run_time, rate_func = linear) for curve in curves))

    CelestialBody.bodies.clear()
    
    return [positions, velocities]
  
class OrbitingFig8(Scene):
  def construct(self, sim_time, dt, run_time, animate=True, savefile=None):
    CelestialBody.initBodies(orbitingFig8)
    
    [positions, velocities] = CelestialBody.createSim(sim_time, dt)
    
    # Saving results
    if(savefile is not None):
      with open(savefile, 'wb') as f:
        np.save(f, positions)
    
    if(animate):
      curves = VGroup()
      for i in range(len(CelestialBody.bodies)):
        curve = VMobject().set_points_as_corners(positions[:,i])
        curve.set_stroke(CelestialBody.bodies[i].getColor())
        curves.add(curve)
      
      dots = Group(Sphere(color = body.getColor(), radius = body.getRadius()) for body in CelestialBody.bodies)
      
      def updateDots(dots):
        for dot, curve in zip(dots, curves):
          dot.move_to(curve.get_end())
      
      self.add(dots)
      dots.add_updater(updateDots)
      
      tail = VGroup(
          TracingTail(dot, time_traced =  run_time/10).match_color(dot)
          for dot in dots
      )
      
      self.add(tail)
      
      frame = self.camera.frame

      frame.move_to(ORIGIN)
      frame.set_height(ORIGIN + 3)

      COM = Group(Sphere(color = GREEN, radius = dots[0].radius) for systems in dots[i:i+3] for i in [0,3,6,9,12])

      def updateCOM(COM):
        for com,i in zip(COM, [0,3,6,9,12]):
          com.move_to(dots[i:i+3].get_center_of_mass())
      
      self.add(COM)
      COM.add_updater(updateCOM) 
      
      tail2 = VGroup(
          TracingTail(COM, time_traced = run_time/2).match_color(COM)
          for COM in COM
      )
      
      self.add(tail2)
      COM.set_opacity(0)
      
      curves.set_opacity(0)
      
      self.play(*(ShowCreation(curve, run_time = run_time, rate_func = linear) for curve in curves),
                frame.animate.set_height(ORIGIN + 60).set_anim_args(run_time = run_time/2, rate_func = rush_into)
                )

    CelestialBody.bodies.clear()
    
    return [positions, velocities]
  