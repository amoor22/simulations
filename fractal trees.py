import pygame
import math
pygame.init()
pygame.display.set_caption("Fractal Tree")

screen_width = 800
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

a = 20
b = 0
lengs = 100
len_red = 1.15
angle = math.pi / 8
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def draws(x1, y1, ang, leng):
    x2 = x1 + (leng * math.cos(ang))
    y2 = y1 - (leng * math.sin(ang))
    pygame.draw.line(win, (255, 255, 255), (x1, y1), (x2, y2))

    x3 = x1 + (leng * math.cos(ang + (math.pi / 2)))
    y3 = y1 - (leng * math.sin(ang + (math.pi / 2)))
    pygame.draw.line(win, (255, 255, 255), (x1, y1), (x3, y3))

    if leng > 2:
        draws(x2, y2, ang - angle, leng / 2)
        draws(x3, y3, ang + angle, leng / 2)


def RedrawGameWindow():
    global angle
    win.fill(0)
    mx, my = pygame.mouse.get_pos()
    angle = translate(mx, 0, screen_width, 0, 2 * math.pi)
    pygame.draw.line(win, (255, 255, 255), (400, 500), (400, 400))
    draws(400, 400, math.pi / 4, 200)
    pygame.display.update()


running = True

while running:
    clock.tick(27)
    RedrawGameWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False