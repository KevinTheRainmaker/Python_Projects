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

# 게시글 쓰기
def write_post():
    '''게시글 작성 함수'''
    print('\n\n')
    title = input('제목을 입력해주세요 >>\n')
    content = input('본문을 입력해주세요 >>\n')
    # 글 번호
    id = post_list[-1].getID() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print('# 게시글이 등록되었습니다')

# 게시글 상세 확인
def show_post_detail(id):
    '''게시글 상세 확인 함수'''
    global post_list
    for post in post_list:
        if post.getID() == id:
            # 조회수 1 증가
            post.addViewCount()
            print('번호: ', post.getID())
            print('제목: ', post.getTitle())
            print('본문: ', post.getContent())    
            print('조회수: ', post.getViewCount())
            target_post = post

    while True:
        print('Q) 수정(1) / 삭제(2) / 메뉴로 돌아가기(-1)')
        try:
            choice = int(input('>> '))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print('잘못 입력하셨습니다.')
        except ValueError:
            print('숫자를 입력해주세요.')

# 게시글 수정
def update_post(targetpost):
    '''게시글 수정 함수'''
    print('    - 게시글 수정 -    ')
    title = input('제목을 입력해주세요\n>>')
    content = input('본문을 입력해주세요\n>>')
    targetpost.setPost(targetpost.id, title, content, targetpost.view_count)
    print('수정이 완료되었습니다.')

# 게시글 삭제
def delete_post(targetpost):
    '''게시글 삭제 함수'''
    post_list.remove(targetpost)
    print('# 게시글이 삭제되었습니다.')

# 게시글 저장
def save():
    '''게시글 저장 함수'''
    f = open(file_path, 'w',encoding='utf8')
    writer = csv.writer(f)
    for post in post_list:
        row = [post.getID(), post.getTitle(), post.getContent(),post.getViewCount()]
        writer.writerow(row)
    f.close()
    print('# 저장이 완료되었습니다.')
    print('# 프로그램 종료')

# 게시글 목록
def list_post():
    '''게시글 목록 출력 함수'''
    print('\n\n')
    print('    - 게시글 목록 -    ')
    id_list = []
    for post in post_list:
        print(f'번호: {post.getID()}')
        print(f'제목: {post.getTitle()}')
        print(f'조회수: {post.getViewCount()}')
        print()
        id_list.append(post.getID())

    while True:
        print('Q) 글 번호를 선택해주세요. (메뉴로 돌아가려면 -1)')
        try:
            choice = int(input('>> '))
            if choice in id_list:
                show_post_detail(choice)
                break
            elif choice == -1:
                break
            else:
                print('없는 글 번호입니다.')
        except ValueError:
            print('숫자를 입력해주세요.')
            

# 메뉴 출력
while True:
    print('\n\n')
    print('    -메뉴를 선택해 주세요-    ')
    print('1. 게시글 작성')
    print('2. 게시글 목록')
    print('3. 프로그램 종료')
    try:
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력해주세요.')
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print('프로그램 종료')
            save()
            break
        # else:

# print(post_list)
# print(post_list[0].getTitle())