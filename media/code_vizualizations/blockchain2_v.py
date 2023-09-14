import pygame
import time
from PIL import Image
import numpy as np

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Window settings
WIDTH, HEIGHT = 400, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockchain Visualization Vertical")

# Font settings
font = pygame.font.Font(None, 36)

# Block settings
block_width, block_height = 50, 50
block_space = 10
arrow_size = 5
start_x = WIDTH // 2 - block_width // 2
start_y = HEIGHT - 60

blocks = []
frames = []

def draw_arrow(x, y):
    pygame.draw.polygon(win, BLACK, [(x, y), (x - arrow_size, y - arrow_size), (x + arrow_size, y - arrow_size)])

def draw_window():
    win.fill(WHITE)

    # Draw the blocks
    for i, block in enumerate(blocks):
        pygame.draw.rect(win, BLUE, block['rect'])

        # Draw the connectors with arrows for all blocks after the genesis block
        if i > 0:
            pygame.draw.line(win, BLACK, (block['rect'].x + block_width // 2, block['rect'].y + block_height), (block['rect'].x + block_width // 2, block['rect'].y + block_height + block_space - arrow_size), 3)
            draw_arrow(block['rect'].x + block_width // 2, block['rect'].y + block_height + block_space)

        # Draw the counter inside the block
        counter_text = font.render(str(block['counter']), True, BLACK)
        text_rect = counter_text.get_rect(center=(block['rect'].x + block_width // 2, block['rect'].y + block_height // 2))
        win.blit(counter_text, text_rect)

    pygame.display.update()

    # Capture frame
    frames.append(pygame.surfarray.array3d(pygame.display.get_surface()))

def main():
    clock = pygame.time.Clock()
    run = True
    counter = 0
    
    while run:
        clock.tick(10)
        draw_window()

        # Create a new block every 3 seconds
        if len(blocks) == 0 or (pygame.time.get_ticks() - blocks[-1]['timestamp']) >= 500:
            counter += 1
            if len(blocks) == 0:
                new_rect = pygame.Rect(start_x, start_y, block_width, block_height)
            else:
                new_rect = pygame.Rect(start_x, blocks[-1]['rect'].y - block_height - block_space, block_width, block_height)

            block = {
                'rect': new_rect,
                'timestamp': pygame.time.get_ticks(),
                'counter': counter
            }

            blocks.append(block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Convert frames to GIF using Pillow
    imgs = [Image.fromarray(np.flipud(frame)) for frame in frames]  # Only flip vertically
    imgs[0].save('blockchain_viz.gif', save_all=True, append_images=imgs[1:], optimize=False, duration=100, loop=0)

    pygame.quit()

if __name__ == "__main__":
    main()
