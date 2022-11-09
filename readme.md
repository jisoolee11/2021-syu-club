# 🎊 2021-2학기 동아리 홍보전 🦁
<img src="https://user-images.githubusercontent.com/63850508/200763096-8b507101-82db-4727-9ad1-fa7247996b54.jpg" height="500" align="left"/>
<img src="https://user-images.githubusercontent.com/63850508/200764192-53faeedc-fd0b-4fd8-9237-005dc1d2d250.jpg" height="500" align="right"/>
<p align="center"><img src="https://user-images.githubusercontent.com/63850508/200763743-0ac11804-8586-4ba8-85e0-82a32f959700.jpg" height="500"/></p>

> 교내 동아리를 가입하고 싶지만 어떤 동아리가 있는지 잘 모르는 학우들을 위해 삼육대 중앙동아리를 모두 모아 소개하고 지원까지 가능한 서비스를  Likelion at SYU 9기와 삼육대 동아리연합회가 함께 기획하여 서비스를 제작했습니다.

## 📁 디렉토리 구조
```
2021-syu-club
├── accounts  # 동아리 관리자 회원가입
├── base # 인트로 화면
├── club # 메인
├── media 
├── onlineclub # 프로젝트 폴더
├── post # 동아리 게시판
└── static
```

## 💻 세팅 방법
0. 본인의 ```branch```에서 맡은 기능 작업
1. 필요 패키지 설치 ```pip install -r requirements.txt```
2. 2021-syu-club 폴더에 ```secrets.json``` 파일 등록
3. DB 설정 ```python3 manage.py migrate```
4. 프로젝트 실행 ```python3 manage.py runserver```

## ⚙️ 개발 환경
**Backend**: Django, sqlite3<br>
**Frontend**: HTML, CSS, JavaScript

## 👍 구현 기능
**메인**
- 동아리검색
- 전체 동아리 순위 순/랜덤 순 정렬
- 동아리 분과 별 보기
- 각 동아리 관리자 로그인<br>

**상세**
- 동아리 SNS 연동
- 동아리 사진/게시글 업로드

## ❗️ 사용 방법
1. 각 동아리 관리자는 로그인하면 각 동아리 페이지에 사진, 게시물을 업로드, 동아리 지원 폼 링크, SNS 링크를 등록 할 수 있다.
2. 일반 사용자는 회원가입 없이 동아리 순위, 분과 별 또는 검색을 통해 동아리 페이지를 볼 수 있다.
3. 동아리 페이지 별 지원 링크로 바로 동아리 지원이 가능하다. 

## 🦁 개발 참여자
LIKELION 9th at SYU<br>
Backend : 박미란, 박현서, 이지수, 최정은, 함승우, 황한슬<br>
Frontend : 김지연, 박세연, 이민주, 이보람, 주미진<br>
Design : 윤예빈, 성에지
