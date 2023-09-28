import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Constants
EARTH_RADIUS = 1
NUMBER_OF_EARTHS = int(2**255 / 7.5e18)  # Using the previous estimation of 7.5e18 grains of sand per Earth
EARTHS_PER_ROW = 10

def draw_earth(ax, x, y):
    """Draw an 'Earth' circle."""
    earth_circle = patches.Circle((x, y), EARTH_RADIUS, fc='blue', ec='black', zorder=5)
    ax.add_patch(earth_circle)

def visualize_large_number_comparison():
    fig, ax = plt.subplots(figsize=(15, 15))
    
    rows_needed = NUMBER_OF_EARTHS // EARTHS_PER_ROW + 1

    for row in range(rows_needed):
        for col in range(EARTHS_PER_ROW):
            if (row * EARTHS_PER_ROW + col) < NUMBER_OF_EARTHS:
                draw_earth(ax, col * (EARTH_RADIUS * 2.5), -row * (EARTH_RADIUS * 2.5))

    ax.set_xlim(-EARTH_RADIUS, EARTHS_PER_ROW * EARTH_RADIUS * 2.5)
    ax.set_ylim(-rows_needed * EARTH_RADIUS * 2.5, EARTH_RADIUS)
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    plt.tight_layout()
    plt.show()

visualize_large_number_comparison()
