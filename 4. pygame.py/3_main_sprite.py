import pygame

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("GiAsMEt") # 게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/kgbko/Desktop/My GitHub repo/Python_Playground/4. pygame.py/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/kgbko/Desktop/My GitHub repo/Python_Playground/4. pygame.py/character.png")
character_size = character.get_rect().size # 이비지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) # 화면 가로 길이의 절반 위치
character_y_pos = screen_height - character_height  # 화면 세로 가장 아래

# 이벤트 루프
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그려주기

# pygame 종료
pygame.quit()