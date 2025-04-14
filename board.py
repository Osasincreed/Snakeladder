import pygame

# Board constants
ROWS, COLS = 10, 10
TILE_SIZE = 60

# Colors
LIGHT_BEIGE = (244, 241, 222)
SOFT_GRAY = (217, 217, 217)
BLUE = (0, 119, 182)
LIGHT_BLUE = (202, 240, 248)
RED = (217, 4, 41)
DARK_RED = (106, 4, 15)
BLACK = (0, 0, 0)

# Define ladders and snakes
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

def get_square_number(row, col):
    """Calculate square number correctly starting from bottom-left to top-left."""
    actual_row = 9 - row  # Flip the row because Pygame's (0,0) is top-left
    if actual_row % 2 == 0:
        return actual_row * 10 + col + 1
    else:
        return actual_row * 10 + (9 - col) + 1



def draw_board(screen):
    """Draw the full board."""
    for row in range(ROWS-1, -1, -1):  # Start from bottom
        for col in range(COLS):
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            square_num = get_square_number(row, col)

            # Decide color
            if square_num in ladders:
                color = BLUE  # Beginning of ladder
            elif square_num in ladders.values():
                color = LIGHT_BLUE  # End of ladder
            elif square_num in snakes:
                color = RED  # Beginning (head) of snake
            elif square_num in snakes.values():
                color = DARK_RED  # End (tail) of snake
            else:
                # Normal chessboard coloring
                if (row + col) % 2 == 0:
                    color = LIGHT_BEIGE
                else:
                    color = SOFT_GRAY

            # Draw the square
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)

            # Draw square border
            pygame.draw.rect(screen, BLACK, rect, 1)

            # Draw square number
            font = pygame.font.SysFont(None, 20)
            text = font.render(str(square_num), True, BLACK)
            text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
            screen.blit(text, text_rect)

