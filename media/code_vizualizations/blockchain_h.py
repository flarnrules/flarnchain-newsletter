import pygame
import time

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Window settings
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockchain Visualization")

# Font settings
font = pygame.font.Font(None, 36)

# Block settings
block_width, block_height = 50, 50
block_space = 10
start_x = 10
start_y = HEIGHT // 2 - block_height // 2

blocks = []

def draw_window():
    win.fill(WHITE)

    # Draw the blocks
    for i, block in enumerate(blocks):
        pygame.draw.rect(win, BLUE, block['rect'])
        if i > 0:  # To ensure we don't try to draw a line for the first block
            pygame.draw.line(win, BLACK, (block['rect'].x, block['rect'].y + block_height // 2), (block['rect'].x - block_space, block['rect'].y + block_height // 2), 3)

        # Draw the counter inside the block
        counter_text = font.render(str(block['counter']), True, BLACK)
        text_rect = counter_text.get_rect(center=(block['rect'].x + block_width // 2, block['rect'].y + block_height // 2))
        win.blit(counter_text, text_rect)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    counter = 0
    
    while run:
        clock.tick(10)
        draw_window()

        # Create a new block every 3 seconds
        if len(blocks) == 0 or (pygame.time.get_ticks() - blocks[-1]['timestamp']) >= 1000:
            counter += 1
            if len(blocks) == 0:
                new_rect = pygame.Rect(start_x, start_y, block_width, block_height)
            else:
                new_rect = pygame.Rect(blocks[-1]['rect'].x + block_width + block_space, start_y, block_width, block_height)

            block = {
                'rect': new_rect,
                'timestamp': pygame.time.get_ticks(),
                'counter': counter
            }

            blocks.append(block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
