import pygame
import numpy as np

# Fungsi Matrix Translasi
def translation(tx, ty):
  return np.array([
      [1, 0, tx],
      [0, 1, ty],
      [0, 0, 1]
  ], dtype = float)
# Fungsi Matrix Scaling
def scaling(sx, sy):
  return np.array([
      [sx, 0, 0],
      [0, sy, 0],
      [0, 0, 1]
  ], dtype = float)

#skrip untuk Midpoint circle
def midpoint_crl(surface, color, center, radius, filled = True):
  xc, yc = int(center[0]), int(center[1])
  x = 0
  y = radius
  p = 1 - radius
  while x <= y:
    if filled:
      # bagian dalam circle
      spans = [
          (yc + y, xc - x, xc + x),
          (yc - y, xc - x, xc + x),
          (yc + x, xc - y, xc + y),
          (yc - x, xc - y, xc + y)
      ]
      for py, x1, x2 in spans:
        if 0 <= py < height:
          for px in range(x1, x2 + 1):
            if 0 <=px < width:
              surface.set_at((px, py), color)
    else:
    #Draw garis tepi linckaran
      points = [
          (xc + x, yc + y),
          (xc - x, yc + y),
          (xc + x, yc - y),
          (xc - x, yc - y),
          (xc + y, yc + x),
          (xc - y, yc + x),
          (xc + y, yc - x),
          (xc - y, yc - x)
      ]
      for px, py in points:
        if 0 <= px < width and 0 <= py < height:
          surface.set_at((px, py), color)
    # Perhitungan midpoint
    x += 1
    if p < 0:
      p += 2 * x + 1
    else:
      y -= 1
      p += 2 * (x - y) + 1


# Skrip untuk pygame
pygame.init()
#membuat display window
width = 800
height = 500
screen = pygame.display.set_mode((width, height))

#coloring bg
BACKGROUND = (255, 255, 255)
RED = (200, 40, 40)

# posisi dan ukuran bola
center = np.array([400, 250])
position = center #posisi default
radius = 50 #jari jari default
scale = 1.0 # skala default

# program running game
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #User dapat exit dari game dan running stop
      running = False
    if event.type == pygame.KEYDOWN: # kontrol keyboaard w, a, s, d, + dan -
      if event.key == pygame.K_a: 
        T = translation(-10, 0)
        position = (T @ np.append(position, 1))[:2] #sesuai panjang array
      if event.key == pygame.K_d:
        T = translation(10, 0)
        position = (T @ np.append(position, 1))[:2]
      if event.key == pygame.K_w:
        T = translation(0, -10)
        position = (T @ np.append(position, 1))[:2]
      if event.key == pygame.K_s:
        T = translation(0, 10)
        position = (T @ np.append(position, 1))[:2]
      # Scaling
      if event.key in (pygame.K_PLUS, pygame.K_EQUALS): 
        scale = min(scale * 1.2, 3.0) # bigger
      if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
        scale = max(scale / 1.2, 0.2) # smaller
      # Reset position
      if event.key == pygame.K_SPACE:
        position = np.array([400, 250])
        scale = 1.0
  screen.fill(BACKGROUND)
  s = scaling(scale, scale)

  # transformasi radius menggambar matrix
  radius_vector = np.array([radius, 0, 1])
  scaled_vector = s @ radius_vector # @ untuk perkalian matrix
  new_radius = max(1, int(scaled_vector[0]))


  # Midpoint circle untuk menggambar bola
  midpoint_crl(screen, RED, position, new_radius)

  # info panel
  font = pygame.font.SysFont(None, 26)
  info = font.render(f"Scale: {scale: 2f} | Radius: {new_radius} | x : {position}", True, "black") # menampilkam label ukuran skala, jari-jari circle, dan position (x, y)
  screen.blit(info, (10, 10))
  pygame.display.flip()

pygame.quit()