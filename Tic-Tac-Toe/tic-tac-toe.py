import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
LINE_COLOR = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def draw_lines():

    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 0), (WIDTH, 0), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (0, 0), (0, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def marking():
    return "done"


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((100, 100, 100))
        draw_lines()
        pygame.display.flip()

        

    pygame.quit()


if __name__ == "__main__":
    main()
