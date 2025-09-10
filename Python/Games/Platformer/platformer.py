def main():
    import pygame
    from time import sleep

    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Screen")
    end, clock = True, pygame.time.Clock()

    def showtext(msg, x, y, color, size):
        screen.fill((0, 0, 0))
        fontobj = pygame.font.SysFont("freesans", size, bold=True)
        msgobj = fontobj.render(msg, False, color)
        screen.blit(msgobj, (x, y))

    # Setup images and variables
    tile_image = pygame.image.load("tile.png")
    coin_image = pygame.image.load("coin.png")
    chest_image = pygame.image.load("chest.png")
    score = frame = 0
    tilecheck = []

    # Level design
    tiles = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Player class
    class Player:
        def __init__(self, x, y, image):
            self.x, self.y = x, y
            self.image = image
            self.dx = self.dy = 0
            self.jumping = self.falling = False

        def draw(self):
            self.self = screen.blit(self.image, (self.x, self.y))

        def move(self):
            self.x += self.dx
            self.x, self.x = 570 if self.x > 570 else self.x, 0 if self.x < 0 else self.x
            self.y -= self.dy
            self.dy -= 1 if self.dy > -10 else 0

        def jump(self):
            self.dy = 15
            self.jumping = True

    player = Player(40, 521, pygame.image.load("Run (12).png"))

    # Checks if player is next to or on top of a tile
    def intile():
        global player, tilecheck
        for a in tilecheck:
            if player.self.colliderect(a):
                # Tile above
                if a.top + 19 >= player.self.bottom >= a.top + 1 and player.dy <= 0:
                    player.jumping = player.falling = False
                    player.y = a.top - 39
                    player.dy = 0

                # Tile on right
                elif a.left <= player.self.right <= a.left + 16:
                    player.x = a.left - 29
                    player.x -= 0

                # Tile on left
                elif a.right >= player.self.left >= a.right - 16:
                    player.x = a.right - 5
                    player.x -= 0

                # Standing on a tile
                elif a.bottom >= player.self.top > a.bottom - 20:
                    player.jumping = player.falling = False
                    player.y = a.bottom
                    player.dy = -10

    player.draw()

    # Draw the level
    def drawlevel():
        coins = 0
        global tiles, tilecheck, score, end
        for a in range(20):
            for b in range(15):
                if tiles[b][a] == 1:
                    tilecheck.append(screen.blit(tile_image, (a * 40, b * 40)))
                if tiles[b][a] == 2:
                    if player.self.colliderect(screen.blit(coin_image, (a * 40, b * 40))):
                        tiles[b][a] = 0
                        score += 1
                    coins += 1
                # Win condition
                if tiles[b][a] == 3:
                    if (
                            player.self.colliderect(
                                screen.blit(chest_image, (a * 40, b * 40 + 15))
                            )
                            and coins == 0
                    ):
                        screen.fill((0, 0, 0))
                        showtext("Level Complete", 300, 275, (0, 255, 0), 50)
                        pygame.display.update()
                        sleep(1)
                        end = False
                        return

    # Main game loop
    while end:
        # Update level
        screen.fill((0, 0, 0))
        drawlevel()
        player.draw()
        pygame.display.update()
        clock.tick(30)
        frame += 1

        intile()

        # Handle keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Jump
                if event.key == pygame.K_SPACE and not (player.jumping or player.falling):
                    player.jump()
                # Right and left
                player.dx += 5 if event.key == pygame.K_d else 0
                player.dx -= 5 if event.key == pygame.K_a else 0

            if event.type == pygame.KEYUP:
                # Right and left
                player.dx -= 5 if event.key == pygame.K_d else 0
                player.dx += 5 if event.key == pygame.K_a else 0
            if event.type == pygame.QUIT:
                end = False

        player.move()
    pygame.quit()


if __name__ == '__main__':
    main()
