def main():
    import pygame
    import random as ra

    pygame.init()

    # variables
    m_mov = 0
    left = False
    x = 130
    x_moon = 1270
    run = True
    FPS = 60
    width = 1500
    height = 800
    # rects
    ground = pygame.Rect(0, 600, 300, 200)
    mountains = pygame.Rect(0, 200, 1500, 500)

    # pics
    shelter = pygame.image.load("shelter.png")
    icon = pygame.transform.scale(shelter, (700, 700))
    shelter = pygame.transform.scale(shelter, (200, 200))
    ground_img = pygame.image.load("ground.png")
    ground_img = pygame.transform.scale(ground_img, (ground.width, ground.height))
    mountains_img = pygame.image.load("mountains.png")
    mountains_img = pygame.transform.scale(mountains_img, (mountains.width, mountains.height))
    cloud_img = pygame.image.load("cloud.png")
    moon_img = pygame.image.load("moon.png")
    moon_img = pygame.transform.scale(moon_img, (250, 150))
    # music

    # basic
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Zholter")
    pygame.display.set_icon(icon)
    win.fill((15, 0, 60))
    win.blit(mountains_img, (mountains.x, mountains.y))
    for i in range(width // ground.width):
        win.blit(ground_img, (ground.x, ground.y))
        ground.x += ground.width
    win.blit(shelter, (600, 441))
    for i in range((width // 150)):
        y = ra.randint(160, 200)
        cloud_w_h = ra.randint(80, 180)
        cloud_img = pygame.transform.scale(cloud_img, (cloud_w_h, cloud_w_h))
        win.blit(cloud_img, (x, y))
        x += 200

    # loop
    while run:
        # animation for back
        win.blit(moon_img, (x_moon, 0))
        if x_moon > 10 and left is False:
            m_mov += 1
            if m_mov == 100:
                x_moon -= 1
                m_mov = 0
            if x_moon <= 11:
                left = True
        if x_moon < 1270 and left:
            m_mov += 1
            if m_mov == 100:
                x_moon += 1
                m_mov = 0
            if x_moon >= 1269:
                left = False

        clock = pygame.time.Clock()
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


    # game type: infinite
    # zombie apocalypse ande people go to shelter and soldier (main character) has to protect them
    # every zombie when dies drops teeth and body
    # with teeth you can create traps that slow zombies and increase heath/durability of shelter
    # with body you can increase character speed and strength
    # with body and teeth combined you can upgrade your weapon from bat to knife to shot gun to machine gun to rocket launcher
    # game goal: don't die and keep shelter safe

if __name__ == "__main__":
    main()




