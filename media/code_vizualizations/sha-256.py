import matplotlib.pyplot as plt
import numpy as np
import hashlib

def string_to_sha256(input_string):
    """Hashes the string with SHA-256 and returns the hash."""
    return hashlib.sha256(input_string.encode()).digest()

def visualize_sha256(hash_bytes):
    """Visualizes the SHA-256 hash as an 8x4 grid of colored squares."""
    
    # Convert hash bytes to colors (R, G, B). We'll use 32 bytes (256 bits) to produce 10.66 RGB colors.
    # For visualization, we'll use only the first 10 groups, discarding the remaining two-thirds of the last color.
    colors = [tuple(hash_bytes[i:i+3]) for i in range(0, 30, 3)]
    
    # Create an 8x4 grid to display the colors. To fill in the remaining slots, duplicate some of the previous colors.
    while len(colors) < 32:
        colors.append(colors[-1])

    image = np.array(colors).reshape(4, 8, 3)
    
    # Plotting
    fig, ax = plt.subplots(1, figsize=(8,4))
    ax.imshow(image, interpolation='nearest')
    
    # Remove axis labels and ticks
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    user_input = input("Enter a string to visualize its SHA-256 hash: ")
    hashed = string_to_sha256(user_input)
    visualize_sha256(hashed)
