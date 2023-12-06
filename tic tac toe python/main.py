import pygame 
import sys

# Initialize Pygame
pygame.init()

width, height = 300, 300
cell_size = width // 3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def draw_grid():
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, black, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
            if grid[row][col] == 1:
                pygame.draw.line(screen, red, (col * cell_size, row * cell_size), ((col + 1) * cell_size, (row + 1) * cell_size), 2)
                pygame.draw.line(screen, red, ((col + 1) * cell_size, row * cell_size), (col * cell_size, (row + 1) * cell_size), 2)

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0 or grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != 0 or grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return True
    return False

def check_draw():
    # Check for a draw
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                return False
    return True

current_player = 1  # Player 1 starts
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size

            if grid[row][col] == 0:
                grid[row][col] = current_player

                if check_winner():
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    # Switch players
                    current_player = 2 if current_player == 1 else 1

    screen.fill(white)
    draw_grid()
    pygame.display.flip()
