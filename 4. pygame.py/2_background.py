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

# 이벤트 루프
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0,100,255)) # RGB 값 넣어서 단색 채우기도 가능
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그려주기

# pygame 종료
pygame.quit()