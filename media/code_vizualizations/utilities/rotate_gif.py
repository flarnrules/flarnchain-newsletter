from PIL import Image, ImageSequence

# Open the GIF
img = Image.open('../blockchain_viz.gif')

# Rotate each frame
frames = [frame.rotate(-90, expand=True) for frame in ImageSequence.Iterator(img)]

# Save the rotated frames as a new GIF
frames[0].save('../rotated_blockchain_viz.gif', save_all=True, append_images=frames[1:], optimize=False, duration=img.info['duration'], loop=0)
