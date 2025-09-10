import atexit, socket, pygame, time, threading

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Server")
end = 1


def showtext(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size, bold=True)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


def handle_exit():
    global running
    running = 0
    print("Stopping program")
    pygame.quit()
    recieving.join()
    s.close()


atexit.register(handle_exit)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.27"
port = 80

s.bind((host, port))
s.listen(5)
print("Socket is listening")
conn, addr = s.accept()
print("Connection established")

score = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
mark1, mark2 = "x", "o"


def cross(x, y):
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + 200, y + 200), 2)
    pygame.draw.line(screen, (255, 255, 255), (x, y + 200), (x + 200, y), 2)


def circle(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x + 100, y + 100), 99, 2)


def draw(score):
    screen.fill((0, 0, 0))
    for a in range(3):
        for b in range(3):
            if score[b + (a * 3)] == "x":
                cross(b * 200, a * 200)
            elif score[b + (a * 3)] == "o":
                circle(b * 200, a * 200)
            pygame.draw.rect(screen, (255, 255, 255), (b * 200, a * 200, 200, 200), 2)
    pygame.display.update()
    if (
        (score[0] == score[1] == score[2] != " ")
        or (score[3] == score[4] == score[5] != " ")
        or (score[6] == score[7] == score[8] != " ")
        or (score[0] == score[3] == score[6] != " ")
        or (score[4] == score[1] == score[7] != " ")
        or (score[8] == score[5] == score[2] != " ")
        or (score[0] == score[4] == score[8] != " ")
        or (score[6] == score[4] == score[2] != " ")
    ):
        screen.fill((0, 0, 0))
        showtext((mark1.upper() + " wins"), 114, 164, (0, 144, 0), 40)
        pygame.display.update()
        time.sleep(1)
        handle_exit()


draw(score)


def box(x, y):
    if 0 < x < 200:
        if 0 < y < 200:
            return 0
        if 200 < y < 400:
            return 3
        if 400 < y < 600:
            return 6
    if 200 < x < 400:
        if 0 < y < 200:
            return 1
        if 200 < y < 400:
            return 4
        if 400 < y < 600:
            return 7
    if 400 < x < 600:
        if 0 < y < 200:
            return 2
        if 200 < y < 400:
            return 5
        if 400 < y < 600:
            return 8


def recieve():
    global mark1, mark2, running, score
    running = 1
    while running:
        try:
            score = list(conn.recv(128).decode())
        except:
            print("client broke")
            handle_exit()
        draw(score)
        mark1, mark2 = mark2, mark1


recieving = threading.Thread(target=recieve)
recieving.start()

while end:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mark1 == "o":
                break
            score[box(event.pos[0], event.pos[1])] = mark1
            mark1, mark2 = mark2, mark1
            draw(score)
            conn.sendall(("".join(score)).encode())
        if event.type == pygame.QUIT:
            handle_exit()
            break
