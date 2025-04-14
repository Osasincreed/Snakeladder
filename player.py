import pygame

class Player:
    def __init__(self, color, start_pos):
        self.color = color
        self.position = start_pos  # position is a number between 1 and 100

    def get_coordinates(self):
        """Convert position number to (x, y) pixel coordinates based on corrected board."""
        pos = self.position - 1  # Position 1 should be index 0
        row = pos // 10
        col = pos % 10

        actual_row = 9 - row  # Flip the row

        if (actual_row % 2 == 0):
            x = col * 60 + 30  # Center of tile
        else:
            x = (9 - col) * 60 + 30

        y = actual_row * 60 + 30  # Center of tile
        return (x, y)

    def move(self, steps):
        """Move player by dice steps."""
        self.position += steps
        if self.position > 100:
            self.position = 100

    def draw(self, screen):
        """Draw the player as a circle."""
        x, y = self.get_coordinates()
        pygame.draw.circle(screen, self.color, (x, y), 15)

