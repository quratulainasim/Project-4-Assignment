import pygame
import socket
import pickle
import select  # For non-blocking socket

WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")

client_number = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5555))  # Change to server IP if remote

RED = (255, 0, 0)
BLUE = (0, 0, 255)


pos = pickle.loads(s.recv(2048))


def redrawWindow(players):
    win.fill((255, 255, 255))
    pygame.draw.rect(win, RED, (players[0][0], players[0][1], 50, 50))
    pygame.draw.rect(win, BLUE, (players[1][0], players[1][1], 50, 50))
    pygame.display.update()


def main():
    global pos
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        read_sockets, _, _ = select.select([s], [], [], 0.1)

        if read_sockets:
            try:
                players = pickle.loads(s.recv(2048))
                redrawWindow(players)
            except:
                print("Disconnected from server")
                run = False
                breakpoint

        keys = pygame.key.get_pressed()
        x, y = pos
        speed = 5

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += speed

        pos = (x, y)
        try:
            s.send(pickle.dumps(pos))
        except:
            print("Disconnected from server")
            run = False
            break

    pygame.quit()


main()
