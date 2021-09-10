# What is CRUD?
## C: CREATE
## R: READ
## U: Update
## D: DELETE

# Project Description
## 1) 프로그램 기능 파악하기
- 게시글 로딩
    ~~~
    if data.csv 파일이 있으면
        게시글 로딩
            > data.csv 읽기
            > 데이터 한 줄마다
                >> Post 인스턴스 생성
                >> Post 리스트에 인스턴스 저장
    else data.csv 파일이 없으면
        data.csv 생성
    ~~~
- 게시글 저장
- 메뉴 츌력
- 게시글 쓰기 (C)
- 게시글 목록 확인 (R)
- 게시글 상세 확인 (R)
- 게시글 수정 (U)
- 게시글 삭제 (D)

## 2) 클래스 설계
### 게시글 클래스 (Post)
> 속성
> - 글번호
> - 제목
> - 본문
> - 조회수

> 메서드
> - 게시물 수정
> - 조회수 증가
> - 속성 로딩