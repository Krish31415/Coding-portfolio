def main():
    import pygame
    from time import sleep
    from random import choice, randint

    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Screen")
    end, clock = True, pygame.time.Clock()

    # Declaring/setting variables
    global bullets, targets, enemies, levels, alien_bullets
    global player, spaceship, start, frame, rows, level
    bullets, targets, enemies, levels, alien_bullets = [], [], [], [], []
    rows = 2
    level = score = frame = 0
    shoot = False

    spaceship = pygame.image.load("spaceship.png")
    spaceship = pygame.transform.scale(spaceship, (50, 75))

    # Base character class
    class character:
        def __init__(self, x, y, image, width, length):
            self.x = x
            self.y = y
            self.image = image
            self.width = width
            self.length = length

        def draw(self):
            self.self = screen.blit(self.image, (self.x, self.y))

    # Base alien
    class alien(character):
        lives = 1

        def __init__(self, x, y, image, width, length):
            super().__init__(x, y, image, width, length)
            self.min = x
            self.max = x + width + 18

        def move(self):
            x = choice([5, -5])
            self.x += x if self.min < self.x < self.max else -x

        def down(self):
            self.y += 50

    # Alien with 3 lives and different movement
    class super_alien(alien):
        lives = 3
        dx = 2

        def move(self):
            self.x += self.dx
            if self.x <= 0 or self.x >= 550:
                self.dx = -self.dx
                self.y += 50

    # Super alien with 5 lives and shoots
    class shooter_alien(super_alien):
        lives = 5
        dx = 3

    class Bullet(character):
        def move(self):
            self.y -= 10

    class Alien_bullet(Bullet):
        def move(self):
            self.y += 4

    # Spaceship controlled by player
    class Player(character):
        def move(self, x):
            if 0 < x < 550:
                self.x = x

    player = Player(275, 500, spaceship, 50, 75)

    # Draws aliens
    def draw_targets():
        global enemies, targets
        [a.draw() for a in targets]
        # Adds them to collision list
        enemies = [a.self for a in targets]

    def showtext(msg, x, y, color, size):
        fontobj = pygame.font.SysFont("freesans", size, bold=True)
        msgobj = fontobj.render(msg, False, color)
        screen.blit(msgobj, (x, y))

    # Start menu
    def x():
        global player, level, start

        player.draw()
        showtext("Space Invaders", 150, 50, (255, 0, 255), 60)
        start = screen.blit(pygame.image.load("start.png"), (200, 275))

    levels.append(x)

    # Level 1
    def x():
        global frame, rows, targets, enemies, level

        if frame % 180 == 0:
            # Creates aliens
            if frame < (rows * 200):
                for a in range(12):
                    targets.append(
                        alien(a * 40 + 69, -20, pygame.image.load("alien.png"), 22, 16)
                    )
            # Moves aliens
            for a in targets:
                a.down()
        if frame % 60 == 0:
            for a in targets:
                a.move()

        # Next level
        if frame > (rows * 200) and len(enemies) == 0:
            screen.blit(pygame.image.load("background.png"), (0, 0))
            showtext("Level 2", 250, 275, (0, 255, 0), 50)
            pygame.display.update()
            sleep(2)
            level += 1
            frame = 0
            rows = 3

    levels.append(x)

    # Level 2
    def x():
        global frame, plaer, rows, targets, enemies, level

        # Create aliens
        if frame % 200 == 0:
            if frame < (rows * 200):
                targets.append(
                    super_alien(50, 0, pygame.image.load("super alien.png"), 22, 16)
                )

        # Moves aliens
        if frame % 1 == 0:
            for a in targets:
                a.move()

        # Next level
        if frame > (rows * 200) and len(enemies) == 0:
            screen.blit(pygame.image.load("background.png"), (0, 0))
            showtext("Level 3", 250, 275, (0, 255, 0), 50)
            pygame.display.update()
            sleep(2)
            level += 1
            frame = 0
            rows = 3

    levels.append(x)

    # Level 3
    def x():
        global frame, player, rows, targets, enemies, level, end

        for a in alien_bullets:
            # Draw and move alien bullets
            a.draw()
            a.move()

            # Remove off screen bullets
            if a.y > 625:
                alien_bullets.remove(a)

            # Lose condition
            if player.self.colliderect(a.self):
                end = False
                screen.blit(pygame.image.load("background.png"), (0, 0))
                showtext("You lose", 250, 275, (200, 0, 0), 50)
                pygame.display.update()
                sleep(3)
                break

        # Create aliens
        if frame % 400 == 0:
            if frame < (rows * 400):
                targets.append(
                    shooter_alien(50, 0, pygame.image.load("shooter alien.png"), 22, 16)
                )

        for a in targets:
            # Move aliens
            a.move()

            # Shoot alien bullet
            if randint(0, 100) == 0:
                alien_bullets.append(
                    Alien_bullet(
                        a.x + 22, a.y + 40, pygame.image.load("alien bullet.png"), 0, 0
                    )
                )

        # Game over
        if frame > (rows * 400) and len(enemies) == 0:
            screen.blit(pygame.image.load("background.png"), (0, 0))
            showtext("You won!", 250, 275, (0, 255, 0), 50)
            pygame.display.update()
            sleep(2)
            level += 1
            frame = 0

    levels.append(x)

    # Main game loop
    while end:
        # Update game
        screen.blit(pygame.image.load("background.png"), (0, 0))
        player.draw()
        draw_targets()
        if len(levels) == level:
            break
        levels[level]()

        # Shoot bullets while mouse button held down
        if frame % 10 == 0 and shoot:
            bullets.append(
                Bullet(player.x + 20, player.y - 35, pygame.image.load("bullet.png"), 5, 18)
            )

        for a in bullets:

            # Draw and move bullets
            a.draw()
            a.move()

            # Delete off screen bullets
            if a.y < -25:
                bullets.remove(a)

            # Check if bullet hit an alien
            for b in enemies:
                if a.self.colliderect(b):
                    # Removes 1 life from alien
                    c = targets[enemies.index(b)]
                    c.lives -= 1

                    # Delete alien if lives equal to 0
                    if c.lives == 0:
                        targets.remove(c)
                        enemies.remove(b)
                        score += 1

                    # Delete bullet
                    bullets.remove(a)

        showtext(("Score: " + str(score)), 10, 550, (255, 255, 0), 50)

        pygame.display.update()
        clock.tick(60)
        frame += 1

        # Handle keyboard inputs
        for event in pygame.event.get():
            # Move spaceship to mouse position
            if event.type == 1024:
                player.move(event.pos[0] - 25)

            # Check if mouse clicked
            if event.type == 1025 and event.button == 1:
                # Checks if mouse clicked on start button
                if start and start.collidepoint(event.pos):
                    level += 1
                    start = False
                    break
                shoot = True
            if event.type == 1026 and event.button == 1:
                shoot = False

            if event.type == pygame.QUIT:
                end = False

        # Lose condition
        if player.self.collidelistall(enemies) or [a for a in enemies if a.y > 600]:
            screen.blit(pygame.image.load("background.png"), (0, 0))
            showtext("You lose", 250, 275, (200, 0, 0), 50)
            pygame.display.update()
            sleep(2)
            break
    pygame.quit()


if __name__ == '__main__':
    main()
