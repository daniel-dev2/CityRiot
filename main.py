import pygame
from zombie import Zombie
from player import Player

pygame.init()

# window configuration
RESOLUTION = (800, 600)
window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("ZombieCity")

# image configuration
coin_sprite = pygame.image.load("assets/sprites/coin.png")
bullet_sprite = pygame.image.load("assets/sprites/bullet.png")
zombie_sprite = pygame.image.load("assets/sprites/zombie.png")
heavy_sprite = pygame.image.load("assets/sprites/heavy_zombie.png")
background_image = pygame.image.load("assets/sprites/city_background.png")
icon = pygame.image.load("assets/sprites/icon.png")
pygame.display.set_icon(icon)

player = Player()
player.last_time_hit = pygame.time.get_ticks()

zombie1 = Zombie(0.3)
zombie2 = Zombie(0.4)
zombie3 = Zombie(0.5)
zombie4 = Zombie(0.6)
zombie5 = Zombie(0.5)
zombie6 = Zombie(0.3)
zombie7 = Zombie(0.2)

wave1 = [zombie1, zombie2, zombie3, zombie4, zombie5, zombie6, zombie7]

for zombie in wave1:
    zombie.spawn()

# main game loop
game_running = True
# TODO further refactoring
while game_running:
    window.blit(background_image, (0, 0))
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # player movement
    keys = pygame.key.get_pressed()
    # UP and DOWN
    if keys[pygame.K_w]:
        player.direction.y = -1

    elif keys[pygame.K_s]:
        player.direction.y = 1

    else:
        player.direction.y = 0

    # LEFT and RIGHT
    if keys[pygame.K_a]:
        player.facing_left = True
        player.direction.x = -1

    elif keys[pygame.K_d]:
        player.facing_right = True
        player.direction.x = 1

    else:
        player.direction.x = 0

    # flipping the player horizontally
    if player.facing_left:
        player.sprite = player.sprite_flipped
        player.bullet_sprite = player.bullet_sprite_flipped
        player.set_bullet_direction(True, False)
        player.facing_left = False

    if player.facing_right:
        player.sprite = player.sprite_unflipped
        player.bullet_sprite = player.bullet_sprite_unflipped
        player.set_bullet_direction(False, True)
        player.facing_right = False

    # blitting the bullet
    if player.bullet_active:
        player.move_bullet(zombie1)
        window.blit(player.bullet_sprite, (player.bullet_pos.x, player.bullet_pos.y))

    for zombie in wave1:
        if zombie.hp > 0:
            window.blit(zombie.sprite, zombie.pos)
        zombie.move(player.position)
        # zombie.collision(player)

    if player.health <= 0:
        game_running = False

    # print(f'Zombie1 position: {zombie1.pos.x}, {zombie1.pos.y}')
    # print(f'Zombie2 position: {zombie2.pos.x}, {zombie2.pos.y}')
    window.blit(player.sprite, player.position)
    pygame.display.flip()

pygame.quit()
