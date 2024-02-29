import hashlib
# ----- 코드 정의 ------
class Member:
    members = []

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        #sha-256 해시함수 -> 비밀번호 해시화.
        hash_password = hashlib.sha256(password.encode())
        password_hash = hash_password.hexdigest()
        return password_hash

    # TODO : 코드 구현이 필요합니다.
    def display(self):
        print(f"Name: {self.name}, Username: {self.username}, Password Hash: {self.password_hash}")
    def display_name(self):
        print(f"Name: {self.name}")


class Post:
    posts = []

    def __init__(self,title,content,author):
    # TODO : 코드 구현이 필요합니다.
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------
members = []
posts = []
#회원 인스턴스 3명 생성
member1 = Member('Lee','awjdgh1111', 'fldeldehd1')
member2 = Member('Kim','austronaut1', 'hwaseongogo')
member3 = Member('Park', 'Lunar', 'Letsgo')
members.append(member1)
members.append(member2)
members.append(member3)

#게시글 인스턴스 3개씩 생성
post1_1 = Post('Hello', 'hellofromLee', member1)
post2_1 = Post('Hello', 'hellofromKim', member2)
post3_1 = Post('Hello', 'hellofromPark', member3)
posts.append(post1_1)
posts.append(post2_1)
posts.append(post3_1)


def create_member():
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    member = Member(name, username, password)
    members.append(member)

def create_post():
    title = input("제목을 입력하세요: ")
    content = input("내용을 입력하세요: ")
    print("회원 목록: ")
    for i, member in enumerate(members, start=1):
        print(f"{i}. {member.name}")
    author_index = int(input("멤버번호를 입력하세요: ")) - 1 #0부터시작하는거 까먹어서 오류생긴줄...
    author = members[author_index]
    post = Post(title, content, author)
    posts.append(post)

def search_user():
    specific_user = input("검색하실 유저를 입력하세요: ")
    found = False
    for member in members:
        if specific_user == member.name:
            member.display_name()
            found = True
            break
    if not found:
        print("해당 유저를 찾을 수 없습니다.")

def search_post():
    specific_word = input("검색할 단어를 입력하세요: ")
    found = False
    print(f"'{specific_word}'가 포함된 글: ")
    for post in posts:
        if specific_word in post.content:
            print(post.content)
            found = True
            break
    if not found:
        print("해당 게시글을 찾을 수 없습니다.")

while True:
    choice = input("어떤 활동을 할까요?(신규멤버/신규포스트/인물검색/게시글검색) ")
    if choice == "신규멤버":
        create_member()
    elif choice == "신규포스트":
        create_post()
    elif choice == "인물검색":
        search_user()
    elif choice == "게시글검색":
        search_post()
    elif choice == "종료":
        break
    else:
        print("다시 선택해주세요.")

