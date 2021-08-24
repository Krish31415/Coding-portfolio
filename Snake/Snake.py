import pygame, sqlite3
from time import sleep
from random import randint

# Initialize SQL cursor
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Initialize pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Intro")


def showtext(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("m42flight721", size, bold=True)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


# Snake game
def run_snake():
    end, clock = True, pygame.time.Clock()
    up = down = right = left = False

    # Food
    class Food:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def draw(self):
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))

    food = Food(
        (randint(0, 790) // 20) * 20, (randint(0, 590) // 20) * 20
    )

    # Snake
    class Snake:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.coordinates = [[x, y]]

        def draw(self):
            [
                pygame.draw.rect(screen, (0, 255, 0), (a[0], a[1], 20, 20))
                for a in self.coordinates
            ]

        def move(self):
            # Teleports snake to other side when reaching border
            snake.x = 0 if snake.x > 790 else snake.x
            snake.x = 800 if snake.x < 0 else snake.x
            snake.y = 0 if snake.y > 590 else snake.y
            snake.y = 600 if snake.y < 0 else snake.y

            # Moves head
            snake.y -= 10 if up else 0
            snake.y += 10 if down else 0
            snake.x += 10 if right else 0
            snake.x -= 10 if left else 0

            # Adds new location of head and removes end
            snake.coordinates.insert(0, [snake.x, snake.y])
            snake.coordinates.pop()

    snake = Snake(
        (randint(0, 790) // 20) * 20, (randint(0, 590) // 20) * 20
    )

    # Game loop
    while end:
        # Update game
        screen.fill((0, 0, 0))
        food.draw()
        snake.draw()
        showtext("Score: " + str(len(snake.coordinates)), 10, 10, (0, 100, 255), 15)
        pygame.display.update()
        clock.tick(25)

        # Handles keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Keeps snake on grid when turning
                if snake.x % 20 == 10:
                    snake.x += 10 if right else 0
                    snake.x -= 10 if left else 0
                if snake.y % 20 == 10:
                    snake.y -= 10 if up else 0
                    snake.y += 10 if down else 0

                # Resets directions
                if ((event.key == pygame.K_UP and not down) and
                        (event.key == pygame.K_DOWN and not up) and
                        (event.key == pygame.K_RIGHT and not left) and
                        (event.key == pygame.K_RIGHT and not left)):
                    up = down = right = left = False
                # Changes snake direction
                up = True if event.key == pygame.K_UP and not down else up
                down = True if event.key == pygame.K_DOWN and not up else down
                right = True if event.key == pygame.K_RIGHT and not left else right
                left = True if event.key == pygame.K_LEFT and not right else left

                # # Up
                # if event.key == pygame.K_UP and not down:
                #     down = right = left = False
                #     up = True
                # # Down
                # if event.key == pygame.K_DOWN and not up:
                #     up = right = left = False
                #     down = True
                # # Right
                # if event.key == pygame.K_RIGHT and not left:
                #     up = down = left = False
                #     right = True
                # # Left
                # if event.key == pygame.K_RIGHT and not left:
                #     up = down = right = False
                #     left = True
            if event.type == pygame.QUIT:
                end = False
        # Checks if snake is eating food
        if snake.y == food.y and snake.x == food.x:
            snake.coordinates.append([food.x, food.y])
            food.x, food.y = (randint(0, 590) // 20) * 20, (
                    randint(0, 590) // 20
            ) * 20

        snake.move()

        if snake.coordinates[0] in snake.coordinates[1:]:
            showtext("Game over", 230, 275, (255, 0, 0), 30)
            c.execute(
                "insert into snake(highscore) values(" + str(len(snake.coordinates)) + ")"
            )
            conn.commit()
            pygame.display.update()
            sleep(2)
            break


# Menu/main loop
menu = True
while menu:
    # Draw options
    screen.fill((0, 0, 0))
    showtext("Snake", 260, 50, (0, 255, 0), 30)
    showtext("Select an option", 180, 200, (255, 255, 255), 20)
    showtext("1. Start game", 260, 300, (0, 100, 255), 15)
    showtext("2. Highscores", 260, 400, (0, 100, 255), 15)
    showtext("3. Exit", 260, 500, (0, 100, 255), 15)
    pygame.display.update()

    # Handle keyboard inputs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Play snake
            if chr(event.key) == "1":
                run_snake()
            # Check highscores
            if chr(event.key) == "2":
                # Get scores from database
                scores = list(
                    c.execute("select * from snake order by highscore desc limit 5")
                )
                print(list(scores))
                # Draw scores
                screen.fill((0, 0, 0))
                showtext("Highscores", 200, 30, (0, 255, 0), 30)
                for a in range(1, 6):
                    showtext(
                        "{0}: {1}".format(str(a), scores[a - 1][0]),
                        260,
                        30 + a * 100,
                        (0, 100, 255),
                        20,
                    )
                pygame.display.update()
                scoring = True
                # Wait for keyboard input
                while scoring:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            scoring = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                scoring = False
                break
            # Quit game
            if chr(event.key) == "3":
                menu = False
        if event.type == pygame.QUIT:
            menu = False
# Close everything
pygame.quit()
conn.commit()
c.close()
conn.close()
