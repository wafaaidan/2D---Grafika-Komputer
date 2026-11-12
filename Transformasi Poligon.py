import matplotlib.pyplot as plt
import numpy as np

xs = np.array([0, 1, 1, 0, 0])
ys = np.array([0, 0, 1, 1, 0])
angle = 90
theta = np.radians(angle)

center_x = np.mean(xs)
center_y = np.mean(ys)
xs_modif = xs - center_x
ys_modif = ys - center_y
xs_rotated_modif = xs_modif * np.cos(theta) - ys_modif * np.sin(theta)
ys_rotated_modif = xs_modif * np.sin(theta) + ys_modif * np.cos(theta)
xs_rotated = xs_rotated_modif + center_x
ys_rotated = ys_rotated_modif + center_y
print("bentuk asal")
print(xs)
print(ys)
print("dirotasi")
print(xs_rotated)
print(ys_rotated)
# Plotting
plt.figure(figsize=(5, 5))
plt.plot(xs, ys, marker="o", linestyle="--", color="gray")
plt.fill(xs, ys, color="lightgray", alpha=0.4)
plt.plot(xs_rotated, ys_rotated, marker="o", color="blue")
plt.fill(xs_rotated, ys_rotated, color="lightblue", alpha=0.75)

plt.grid()
plt.axis("equal")
plt.title(f"Rotasi Polygon {angle}deg pada Titik Pusatnya")
plt.show()





