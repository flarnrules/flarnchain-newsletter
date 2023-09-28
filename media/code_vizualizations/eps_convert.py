import os
from PIL import Image

# Find all files that end with .eps
eps_files = [f for f in os.listdir() if f.endswith('.eps')]

total_frames = len(eps_files)

for frame_number in range(0, total_frames):
    img = Image.open(f"frame_{frame_number}.eps")
    img.save(f"frame_{frame_number}.png")
