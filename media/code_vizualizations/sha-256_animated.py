import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_scale(i):
    if i < frames/2:
        # First half of the animation: log scale transitioning to linear scale
        scale_factor = i/(frames/2)
        ax.set_xlim(1, 10 ** (1 + scale_factor * 76))
    else:
        # Second half of the animation: purely linear scale
        ax.set_xlim(1, 2 ** 255)
    fig.canvas.draw_idle()

grains_on_earth = 7.5e18
two_to_255 = 2 ** 255

fig, ax = plt.subplots(figsize=(10, 6))

# Initial bars
ax.barh('One Earth', grains_on_earth, color='blue', label=f'Grains on One Earth: {grains_on_earth:.2e}')
ax.barh('2^255', two_to_255, color='red', label=f'2^255: {two_to_255:.2e}')

ax.set_xscale('log')
ax.set_xlabel('Number of Grains of Sand')
ax.set_title('Visualizing 2^255 vs Grains of Sand on Earth')
ax.legend()

frames = 100
ani = FuncAnimation(fig, animate_scale, frames=frames, repeat=False)

plt.tight_layout()
plt.show()
