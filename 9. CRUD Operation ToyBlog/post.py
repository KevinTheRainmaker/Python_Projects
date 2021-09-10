class Post:
    # dot String
    '''
    게시물 클래스
    param id: 게시물 아이디
    param title: 글제목 
    param content: 글내용
    param view_count: 조회수
    '''
    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def setPost(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def addViewCount(self):
        self.view_count += 1

    def getID(self):
        return self.id

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

    def getViewCount(self):
        return self.view_count

if __name__ == '__main__':
    post = Post(1, 'test', 'postingTest', 0)
    print(f'{post.getID()} {post.getTitle()} {post.getContent()} {post.getViewCount()}')

    post.setPost(1, 'test2', 'postingTest2', 0)
    print(f'{post.getID()} {post.getTitle()} {post.getContent()} {post.getViewCount()}')

    post.addViewCount()
    print(f'{post.getID()} {post.getTitle()} {post.getContent()} {post.getViewCount()}')