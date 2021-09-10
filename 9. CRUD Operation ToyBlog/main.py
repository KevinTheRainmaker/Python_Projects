import os
import csv
from post import Post

# 파일 경로
file_path = "./data/data.csv"

# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print('게시글 로딩 중...')
    f = open(file_path, 'r', encoding='utf8')
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # 파일 생성
    f = open(file_path, 'w', encoding='utf8')
    f.close()

while True:
    print('\n\n')
    print('    -메뉴를 선택해 주세요-    ')
    print('1. 게시글 작성')
    print('2. 게시글 목록')
    print('3. 프로그램 종료')
    try:
        choice = int(input('>>>'))
    except:
        print('숫자를 입력해주세요.')
    else:
        if choice == 1:
            print('게시글 작성')
        elif choice == 2:
            print('게시글 목록')
        elif choice == 3:
            print('프로그램 종료')
            break
        # else:

# print(post_list)
# print(post_list[0].getTitle())