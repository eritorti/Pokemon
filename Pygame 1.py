import pygame
#import Tilemap

def loadImage(universum,colorkey=None):
    image=pygame.image.load("universum.jpg")
    screen.blit(image,(0,10))
    if image.get_alpha() is None:
        image=image.convert()
    else:
        image=image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey=image.get_at((0,0))
        image.set_colorkey(colorkey,pygame.RLEACCEL)
    return image

def main():
    
    pygame.init()

    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Mein erstes Spiel!")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1,30)
    clock=pygame.time.Clock()
    running=1
    while running:
        clock.tick(30)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    map.handle_input(event.key)
        map.render(screen)
        pygame.display.flip()


main()
