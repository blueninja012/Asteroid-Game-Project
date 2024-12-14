import pygame
import math

pygame.init
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
rotation = 0
angle = 0
rotationMomLeft = 0
rotationMomRight = 0
projectiles = 0
projectileVelocity = pygame.Vector2(0, 0)
i = 0
asteroidMom = 0
asteroidVelocity = pygame.Vector2(0, 0)
asteroids = 1


playerSize = 20
crosshairToggle = True
crosshairDistance = 250
friction = 150
rotFriction = 250
speed = 150
rotSpeed = 150
projectileSpeed = playerSize + 1
asteroidPos = pygame.Vector2(1000, 200)


center = 1280 / 2, 720 / 2
playerPos = pygame.Vector2(center)
projectilePos = pygame.Vector2(0, 0)

vert1 = pygame.Vector2((playerSize * math.cos(angle)) + playerPos.x, (playerSize * math.sin(angle)) + playerPos.y)
vert2 = pygame.Vector2((playerSize * math.cos(angle+2.1)) + playerPos.x, (playerSize * math.sin(angle+2.1)) + playerPos.y)
vert3 = pygame.Vector2((playerSize * math.cos(angle+4.2)) + playerPos.x, (playerSize * math.sin(angle+4.2)) + playerPos.y)
    

momentumW = 0
momentumA = 0
momentumS = 0
momentumD = 0

while running:
    if i > 0:
        i -= 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
    
    screen.fill("black")
    
    pygame.draw.polygon(screen, "white", (vert1, vert2, vert3), 1)
    
    angle = math.radians(rotation)
    
    #note to future me, inevitably here to figure out
    #how to rotate a triangle again or something: it's
    #the angle. Everything else stays the same. The stuff
    #besides the angle determines the point the triangle
    #rotates around.
    vert1 = pygame.Vector2((playerSize * math.cos(angle)) + playerPos.x, (playerSize * math.sin(angle)) + playerPos.y)
    vert2 = pygame.Vector2((playerSize * math.cos(angle+2.1)) + playerPos.x, (playerSize * math.sin(angle+2.1)) + playerPos.y)
    vert3 = pygame.Vector2((playerSize * math.cos(angle+4.2)) + playerPos.x, (playerSize * math.sin(angle+4.2)) + playerPos.y)    
   
   
    if momentumW > 0:
        playerPos.y -= momentumW * dt
        if keys[pygame.K_w] == False:
            momentumW -= friction * dt
    if momentumW < 0:
        momentumW == 0
        
    if momentumA > 0:
        playerPos.x -= momentumA * dt
        if keys[pygame.K_a] == False:
            momentumA -= friction * dt
    if momentumA < 0:
        momentumA == 0
        
    if momentumS > 0:
        playerPos.y += momentumS * dt
        if keys[pygame.K_s] == False:
            momentumS -= friction * dt
    if momentumS < 0:
        momentumS == 0
        
    if momentumD > 0:
        playerPos.x += momentumD * dt
        if keys[pygame.K_d] == False:
            momentumD -= friction * dt
    if momentumD < 0:
        momentumD == 0
        
    if rotationMomLeft > 0:
        rotation -= rotationMomLeft * dt
        if keys[pygame.K_LEFT] == False:
            rotationMomLeft -= rotFriction * dt
    if rotationMomLeft < 0:
        rotationMomLeft == 0

    if rotationMomRight > 0:
        rotation += rotationMomRight * dt
        if keys[pygame.K_RIGHT] == False:
            rotationMomRight -= rotFriction * dt
    if rotationMomRight < 0:
        rotationMomRight == 0
    

    if keys[pygame.K_w]:
        momentumW += speed * dt
    if keys[pygame.K_a]:
        momentumA += speed * dt
    if keys[pygame.K_s]:
        momentumS += speed * dt
    if keys[pygame.K_d]:
        momentumD += speed * dt
    if keys[pygame.K_r]:
        playerPos = pygame.Vector2(center)
        rotation = 0
        projectiles = 0
        asteroids = 1


    if playerPos.x < 0:
        playerPos.x = 1280
    if playerPos.x > 1280:
        playerPos.x = 0
    if playerPos.y < 0:
        playerPos.y = 720
    if playerPos.y > 720:
        playerPos.y = 0
    
    if keys[pygame.K_LEFT]:
        rotationMomLeft += rotSpeed * dt
    if keys[pygame.K_RIGHT]:
        rotationMomRight += rotSpeed * dt
        
    if rotation >= 360:
        rotation = 0
    if rotation < 0:
        rotation = 359.99
        
        
    if keys[pygame.K_SPACE]:
        if projectiles == 0:
            projectileVelocity.x = imaginaryPoint.x - playerPos.x
            projectileVelocity.y = imaginaryPoint.y - playerPos.y
        projectiles = 1
        
        
    if projectilePos.x < 0 or projectilePos.x > 1280 or projectilePos.y < 0 or projectilePos.y > 720:
        projectiles = 0
        
    if projectiles == 0:
            projectilePos.x = playerPos.x
            projectilePos.y = playerPos.y
            
            
    
    if projectiles == 1:      
        pygame.draw.circle(screen, "white", projectilePos, 3, 1)
        projectilePos.x += projectileVelocity.x
        projectilePos.y += projectileVelocity.y
        
        #figure out how to fire projectiles in the
        #direction of the angle
        
        #create imaginary point, some distance from
        #playerPos. Math from that point to playerPos.
        #that should be the direction for x and y
        
    imaginaryPoint = pygame.Vector2(((projectileSpeed) * math.cos(angle)) + playerPos.x, ((projectileSpeed) * math.sin(angle)) + playerPos.y)
    
    if crosshairToggle == True and i == 0:
        if keys[pygame.K_f]:
            crosshairToggle = False
            i = 25
            
    if crosshairToggle == False and i == 0:
        if keys[pygame.K_f]:
            crosshairToggle = True
            i = 25
    
    if crosshairToggle == True:
        crosshair = pygame.Vector2(((crosshairDistance) * math.cos(angle)) + playerPos.x, ((crosshairDistance) * math.sin(angle)) + playerPos.y)
        pygame.draw.circle(screen, "white", crosshair, 6, 1)
    
    if asteroids == 1:
        pygame.draw.circle(screen, "white", asteroidPos, 80, 1)
    
        if abs(projectilePos.x - asteroidPos.x) < 80 and abs(projectilePos.y - asteroidPos.y) < 80:
            #asteroidMom += 200
            #asteroidVelocity.x = projectilePos.x - asteroidPos.x
            #asteroidVelocity.y = projectilePos.y - asteroidPos.y
            projectiles = 0
            asteroids = 0
            
        if abs(playerPos.x - asteroidPos.x) < 80 and abs(playerPos.y - asteroidPos.y) < 80:
            playerPos = pygame.Vector2(center)
            rotation = 0
            projectiles = 0
            asteroids = 1
    
#    if asteroidVelocity.x > 0:
 #       asteroidPos.x += (asteroidVelocity.x) * dt
  #  if asteroidVelocity.y > 0:
   #     asteroidPos.y += (asteroidVelocity.y) * dt

#    print(asteroidVelocity)    
    
    pygame.display.flip()    

    dt = clock.tick(60) / 1000
    
pygame.quit()