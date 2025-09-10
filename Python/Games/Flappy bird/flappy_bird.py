def main():
    import random, time, pygame

    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Flappy Bird")
    # Setup variables
    score, start_menu, end, clock = 0, 1, 1, pygame.time.Clock()
    bg, start = pygame.image.load("bg.png"), pygame.image.load("start.png")

    # Bird
    class Bird:
        def __init__(self, x, y, image):
            self.x, self.y, self.image = x, y, image
            self.dy = -1

        def flap(self):
            self.dy = 10

        def move(self):
            self.y -= self.dy
            self.dy -= 1 if self.dy > -1 else 0

        def draw(self, x=None, y=None):
            x, y = x if x else self.x, y if y else self.y
            self.self = screen.blit(self.image, (x, y - 60))

    bird = Bird(270, 300, pygame.image.load("flappybird.png"))

    # Pipes
    class Pipe:
        def __init__(self, x, y, height, width):
            self.x, self.y = x, y
            self.height, self.width = height, width

        def move(self):
            self.x -= 1
            if self.x < -40:
                self.x = 600
                self.height = random.randint(100, 400)

        def draw(self):
            self.self = [
                pygame.draw.rect(
                    screen, (0, 200, 0), (self.x, self.y, self.width, self.height)
                ),
                pygame.draw.rect(
                    screen,
                    (0, 200, 0),
                    (self.x, self.height + 150, self.width, 600 - (self.height + 150)),
                ),
            ]

    pipes = [Pipe((a * 300) + 550, 0, random.randint(100, 400), 40) for a in range(2)]

    def showtext(msg, x, y, color, size):
        fontobj = pygame.font.SysFont("m42flight721", size, bold=True)
        msgobj = fontobj.render(msg, False, color)
        screen.blit(msgobj, (x, y))

    # Start menu
    screen.blit(bg, (0, 0))
    bird.draw(270, 300)
    showtext("Flappy Bird", 30, 100, (0, 0, 0), 35)
    start_btn = screen.blit(start, (192, 420))
    pygame.display.update()

    # Start menu
    while start_menu:
        for event in pygame.event.get():
            if event.type == 1025:
                if event.button == 1:
                    if start_btn.collidepoint(event.pos):
                        start_menu = 0
            if event.type == pygame.QUIT:
                end = start_menu = 0

    # Game loop
    while end:
        # Draw game
        screen.blit(bg, (0, 0))
        bird.draw()
        [pipe.draw() for pipe in pipes]
        showtext(str(score), 275, 10, (0, 120, 255), 30)
        pygame.display.update()
        clock.tick(60)

        # Check for input
        for event in pygame.event.get():
            if event.type == 1025:
                if event.button == 1:
                    bird.flap()
            if event.type == pygame.QUIT:
                end = 0

        # Win/lose conditions
        if (
                bird.self.collidelistall(
                    [pipe.self[0] for pipe in pipes] + [pipe.self[1] for pipe in pipes]
                )
                or bird.y > 600
                or bird.y < 0
        ):
            time.sleep(0.5)
            showtext("Game over", 30, 275, (255, 0, 0), 40)
            pygame.display.update()
            time.sleep(2)
            break
        if 240 in [a.x for a in pipes]:
            score += 1

        # Move bird and pipes
        bird.move()
        [pipe.move() for pipe in pipes]
    pygame.quit()


if __name__ == '__main__':
    main()
