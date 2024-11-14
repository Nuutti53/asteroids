import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt
    
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      angle = random.uniform(20, 50)
      temp1 = self.velocity.rotate(angle)
      temp2 = self.velocity.rotate(-angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      
      new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
      new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
      
      new_ast1.velocity = temp1 * 1.2
      new_ast2.velocity = temp2 * 1.2
      