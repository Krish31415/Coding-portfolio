def main():
    import random, time, pygame

    # Initialize pygame window
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Intro")
    end, clock = True, pygame.time.Clock()
    # Setup variables
    x, y = 300, 500
    enemies = []
    count = score = 0

    def showtext(msg, x, y, color, size):
        screen.fill((0, 0, 0))
        fontobj = pygame.font.SysFont("freesans", size, bold=True)
        msgobj = fontobj.render(msg, False, color)
        screen.blit(msgobj, (x, y))

    # Draw the balls
    def draw_enemies(enemies, score):
        baddies = []
        for a in enemies:
            a[1] += 1
            baddies.append(pygame.draw.circle(screen, (255, 0, 0), (a[0], a[1]), a[2]))
            if a[1] > 620:
                score += 1
                enemies.remove(a)
        return enemies, baddies, score

    # Pause game
    def pause():
        paused = True
        while paused:
            for e in pygame.event.get():
                if e.type == 1025:
                    if e.button == 1 and dodger.collidepoint(e.pos):
                        paused = False
                if event.type == pygame.QUIT:
                    pygame.quit()

    # Main game loop
    while end:

        # Draw stuff
        screen.fill((0, 0, 0))
        dodger = screen.blit(pygame.image.load("dodger guy.png"), (x, y))
        enemies, baddies, score = draw_enemies(enemies, score)
        pygame.display.update()
        clock.tick(500 + score // 2)
        # Adds an enemy every set interval
        count += 1
        if count % 90 == 0:
            enemies.append([random.randint(0, 600), -10, random.randint(12, 15)])

        # Checks for pause and updates location of player
        for event in pygame.event.get():
            if event.type == 1024:
                x, y = event.pos[0] - 16, event.pos[1] - 12
            if event.type == 1025:
                if event.button == 1:
                    pause()
            if event.type == pygame.QUIT:
                end = False

        # Lose condition
        if dodger.collidelistall(baddies):
            screen.fill((0, 0, 0))
            showtext(("Game over. Your score was " + str(score)), 40, 280, (200, 0, 0), 40)
            pygame.display.update()
            end = False
            time.sleep(3)

        # Win condition
        if score == 500:
            screen.fill((0, 0, 0))
            showtext("Game over. You win", 200, 280, (0, 200, 0), 40)
            pygame.display.update()
            end = False
            time.sleep(3)
    pygame.quit()


if __name__ == '__main__':
    main()
