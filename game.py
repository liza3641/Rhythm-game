#! /usr/bin/python
# -*- coding: utf-8 -*-

import pygame, time
from random import *

size = width, height = 1200, 600
win = pygame.display.set_mode(size)
bg = pygame.transform.rotozoom(
    pygame.image.load('image/background/background.png'), 0, 1)
character_Stop_Right = pygame.transform.rotozoom(
    pygame.image.load('image/character/Walk (1).png'), 0, 0.35)
character_Stop_Left = pygame.transform.rotozoom(pygame.transform.flip(
    pygame.image.load('image/character/Walk (1).png'), True, False), 0, 0.35)


#win.fill((255,255,255))
win.blit(bg, (0, 0))
pygame.display.update()
pygame.init()
clock = pygame.time.Clock()

# Load an image
walkRight = [pygame.transform.rotozoom(pygame.image.load('image/character/Walk (1).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (2).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (3).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (4).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (5).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (6).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (7).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Walk (8).png'), -5, 0.35)]

walkLeft = [pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (1).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (2).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (3).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (4).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (5).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (6).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (7).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Walk (8).png'), True, False), 1, 0.35)]

runRight = [pygame.transform.rotozoom(pygame.image.load('image/character/Run (1).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (2).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (3).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (4).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (5).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (6).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (7).png'), -5, 0.35),
             pygame.transform.rotozoom(pygame.image.load('image/character/Run (8).png'), -5, 0.35)]

runLeft = [pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (1).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (2).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (3).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (4).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (5).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (6).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (7).png'), True, False), 1, 0.35),
            pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/character/Run (8).png'), True, False), 1, 0.35)]

# 스킬 이미지
image_background_skill = pygame.transform.rotozoom(pygame.image.load('image/skill/background_run.png'), 0, 0.6)
image_skill = pygame.transform.rotozoom(pygame.image.load('image/skill/run.png'), 0, 0.6)

# 메테오 이미지
meteor = pygame.image.load("image/enemy/meteor.png")
meteor_size = meteor.get_rect().size # 이미지의 크기를 구헤옴
meteor_width = meteor_size[0] # 캐릭터의 가로 크기
meteor_height = meteor_size[1] # 캐릭터의 세로 크기
meteor_x_pos = (width / 2)  - (meteor_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
meteor_y_pos = 0 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 체력바 이미지
staminabar_background = pygame.image.load("image/stamina/staminabar_background.png")
staminabar_background = pygame.transform.scale(staminabar_background, (1000, 37))
staminabar = pygame.image.load("image/stamina/staminabar.png")
staminabar = pygame.transform.scale(staminabar, (990, 28))

# 죽었을 시 이미지
died = pygame.image.load("image/background/youdied.png")
died = pygame.transform.scale(died, (1200, 600))

# 공격 시 이미지
missile = pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('image/skill/attack.png'), True, False), 1, 0.35)
missileXY = []
# 공격 가능 상태인가? 0.5초간격
missile_state = True
missile_cooltime = 0

# speed
character_speed = 7
meteor_speed = 1
character_x_pos = 50
character_y_pos = 380
left = False
right = False
walkcount = 0
stopd = True

# 스킬 전용 변수
start_time = 0
skill_state = "OFF"

# 체력바 길이
character_stamina = 990

# 게임 계속 실행 
run = True

# 게임 점수
myFont = pygame.font.Font( None, 30)
clear_Font = pygame.font.Font( None, 100)
BLACK = ( 0, 0, 0 )
WHITE = ( 255, 255, 255 )
score = 0

# 게임 시작 시간
gamestart_time = 0

# 배경 이동 
background_x_pos = 0
background_speed = 15
background_count = 0

def redrawG():
    global walkcount, skill_state, character_stamina, staminabar, run, score, background_x_pos, missileXY, missile
    win.blit(bg, (background_x_pos, 0))
    #win.fill((255, 255, 255))
    if walkcount >= 32:
        walkcount = 0

    if skill_state == "OFF":
        # walk right
        if right:
            win.blit(walkRight[walkcount//4], (character_x_pos, character_y_pos))
            walkcount += 1
        #walk left
        elif left:
            win.blit(walkLeft[walkcount//4], (character_x_pos, character_y_pos))
            walkcount += 1
        elif stopd:
            win.blit(character_Stop_Right, (character_x_pos, character_y_pos))
        else:
            win.blit(character_Stop_Left, (character_x_pos, character_y_pos))
            pass
    elif skill_state == "ON":
        # run right
        if right:
            win.blit(runRight[walkcount//4], (character_x_pos, character_y_pos))
            walkcount += 1
        #run left
        elif left:
            win.blit(runLeft[walkcount//4], (character_x_pos, character_y_pos))
            walkcount += 1
        elif stopd:
            win.blit(character_Stop_Right, (character_x_pos, character_y_pos))
        else:
            win.blit(character_Stop_Left, (character_x_pos, character_y_pos))
            pass
    
    #region 스킬 투명도 조절

    # 스킬 사용하고 지난시간을 쿨타임으로 나눈다
    skill_alpha =(time.time() - start_time) / 20
    # 쿨타임이지나 값이 1이상일 시 1로 고정 
    if skill_alpha > 1:
        skill_alpha = 1
    # 투명도을 0~255사이로 하고 정수형으로
    alpha = int(skill_alpha * 255)

    # 이미지의 투명도 조절
    image_background_skill.set_alpha(alpha)
    
    # 스킬 쿨이 다 돌지 않을 경우 투명도 조절하는 이미지 
    if alpha != 255:
        win.blit(image_background_skill, (20, 520))
    # 스킬 쿨이 다 돌았을 경우 사용 가능 이미지
    else:
        win.blit(image_skill, (20, 520))
    #endregion
    
    win.blit(meteor, (meteor_x_pos, meteor_y_pos)) # 메테오 그리기
    if character_stamina <= 0:
        win.blit(died, (0, 0))
        run = False
        pygame.display.update()
        time.sleep(3)
    else:
        staminabar = pygame.transform.scale(staminabar, (character_stamina, 28))
        win.blit(staminabar_background, (30, 20)) # 체력바 그리기
        win.blit(staminabar, (35, 24)) # 체력바 그리기

        text_score= myFont.render(str(score), True, BLACK)
        win.blit(text_score,(1050, 30))

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[0] += 10
                missileXY[i][0] = bxy[0]

                if bxy[0] >= 1200:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                win.blit(missile, (bx, by))


    pygame.display.update()

# 스킬 함수
def skill():
    global start_time, character_speed, skill_state, background_speed
    if start_time == 0:
        start_time = time.time()
        character_speed = 20
        background_speed = 40
        skill_state = "ON"

cool = True
def attack():
    global cool, missile_cooltime
    if cool:
        missile_cooltime = time.time()
        cool = False

    
start_state = True
bgm_start_time = 0
def bgm():
    global start_state, bgm_start_time
    if start_state :
        bgm_start_time = time.time()
        start_state = False
        pygame.mixer.music.load( "image/bgm/bgm.mp3" )
        pygame.mixer.music.play(-1)

while run:
    dt = clock.tick(30)
    
    if gamestart_time == 0:
        gamestart_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if right:
                right = False
                stopd = True
            if left:
                left = False
                stopd = False
            pass

    keys = pygame.key.get_pressed()
    # D키 또는 오른쪽 화살표키 누룰시 오른쪽으로 이동
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if character_x_pos > width - 120:
            character_x_pos = width - 120
        character_x_pos += character_speed 
        right = True
        left = False
        background_x_pos -= background_speed * 2
        # 배경을 계속 이동하여 움직이는 화면처럼 보이기
        if(background_x_pos <= -1200):
            background_x_pos = 0
            # 몇번 돌았는지 카운트
            background_count += 1

        # 정해진 바퀴를 돌았을 시 
        if background_count > 200:
            gametime = int(time.time() - gamestart_time)
            mm = gametime // 60
            ss = gametime % 60
            score += character_stamina * 100
            redrawG()
            clear_text = clear_Font.render("Clear" , True, WHITE)
            clear_score = clear_Font.render("time:  " + str(mm) + ":" + str(ss) + "   score: " + str(score) , True, WHITE)
            win.blit(clear_text,(500, 150))
            win.blit(clear_score,(250, 250))
            pygame.display.update()
            run = False
            time.sleep(5)

    # A키 또는 왼쪽 화살표키 누룰시 오른쪽으로 이동
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if character_x_pos < 0:
            character_x_pos = 0
        character_x_pos -= character_speed 
        right = False
        left = True
        background_x_pos += background_speed * 2
        if(background_x_pos >= 0):
            background_x_pos = -1200
            
    bgm()

    if keys[pygame.K_SPACE]:
            if ((time.time() - bgm_start_time)+0.4) % 0.5 < 0.1:

                attack()
                
                if time.time()-missile_cooltime >= 0.4:
                    print("good")
                    score += 100
                    missileX = character_x_pos + 50
                    missileY = character_y_pos + 50
                    missileXY.append([missileX, missileY])
                    cool = True
            else:
                character_stamina -= 10

    # region 스킬
    # Z 키 클릭시 스킬 사용
    if keys[pygame.K_z]:
        # 쿨타임일 시 실행 안함
        if (time.time() - start_time) > 20:
            start_time = 0
            skill()

    # 스킬 유지시간을 설정하고 스킬 유지시간이 끝났을 시 실행 코드
    if (time.time() - start_time) > 5:
        character_speed = 7
        background_speed = 15
        skill_state = "OFF"
    # endregion

    # region 메테오
    meteor_y_pos += meteor_speed * dt

    # 세로 경계값 처리 (meteor)
    if meteor_y_pos > height - meteor_height:
         meteor_x_pos = randint(0, width - meteor_width) 
         meteor_y_pos = 0
    
    # 4. 충돌 처리
    character_rect = walkRight[0].get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    meteor_rect = meteor.get_rect()
    meteor_rect.left = meteor_x_pos
    meteor_rect.top = meteor_y_pos

    # 충돌 체크
    if character_rect.colliderect(meteor_rect):
        character_stamina -= 5
    else:
        score += 1
    # endregion



    redrawG()

pygame.quit()
