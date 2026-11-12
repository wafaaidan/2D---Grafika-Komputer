# tugas 3
import matplotlib.pyplot as plt
import numpy as np
vertex = np.array([[1, 1], [2, 1]])
xs = vertex[0]
ys = vertex[1]
plt.figure(figsize=(5, 5))
plt.plot(xs, ys, marker="o", color="blue")
plt.grid()
plt.axis("equal")
plt.title("Edge Origin")
plt.show()

#Perbandingan 1
print("Perbandingan 1")
print("vertex: ", vertex)
print()

# 1. Transalasi
Translation = vertex
point_t = 3
translation_pt = point_t + Translation
print("hasil translasi: ", translation_pt)

xs_after = translation_pt[0]
ys_after = translation_pt[1]
plt.figure(figsize=(5, 5))
plt.plot(xs, ys, marker="o", linestyle="--", color="grey")
plt.plot(xs_after, ys_after, marker="o", color="blue")
plt.grid()
plt.axis("equal")
plt.title("hasil Translasi Perbandingan 1")
plt.show()

# 2. Rotasi
xs = translation_pt[0]
ys = translation_pt[1]
angle = 180
theta = np.radians(angle)
xs_rotated = xs * np.cos(theta) - ys * np.sin(theta)
ys_rotated = xs * np.sin(theta) + ys * np.cos(theta)
#print(xs_rotated)
#print(ys_rotated)
rotated = np.array([xs_rotated, ys_rotated])
print("hasil rotasi: ", rotated)

#plot
xs_after = rotated[0]
ys_after = rotated[1]
plt.figure(figsize=(5, 5))
plt.plot(xs, ys, marker="o", linestyle="--", color="grey")
#print(xs)
#print(ys)
plt.plot(xs_after, ys_after, marker="o", color="blue")
plt.grid()
plt.axis("equal")
plt.title("hasil Rotasi Perbandingan 1")
plt.show()

# 3. Scaling
scale_factor = 1.5
scaled_points1 = rotated * scale_factor
print("hasil Scaling: ", scaled_points1)
xs_after = scaled_points1[0]
ys_after = scaled_points1[1]

# Plot
plt.figure(figsize=(5, 5))
plt.plot(rotated[0], rotated[1], marker="o", linestyle="--", color="grey")
plt.plot(xs_after, ys_after, marker="o", color="blue")

plt.grid()
plt.axis("equal")
plt.title("Hasil Scaling Perbandingan 1")
plt.show()


