# main.py
import pygame
import sys

from board import draw_board
from player import Player
from game import check_snakes_and_ladders, next_turn
from dice import roll_dice

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Clock
clock = pygame.time.Clock()

# Players
players = [Player((255, 0, 0), 1)]  # Red player starting at 0
current_player = 0

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    draw_board(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_result = roll_dice()
                players[current_player].move(dice_result)
                players[current_player].position = check_snakes_and_ladders(players[current_player].position)
                current_player = next_turn(current_player, len(players))

    # Draw players (will implement real drawing later)
    for player in players:
        player.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
