# FirstWebStudy
륜희,지성쌤과 함께하는 행복한 스터디

### 2017-02-08 ###
스터디 첫 날!

- git
    - git은 하나의 핵심 기술 
    - 근데 쓰기가 넘나 힘들다(이유는? 눈에 안보이니까!)
    - 그래서 github, bitbucket 같은 툴이 있다. 웹으로 관리하기 쉽게
    - 우리는 github를 쓸거에요
    - git은 네가지 명령어를 알면 시작할 수 있어요 
        1. git clone 저장소주소 : 서버에 있는 저장소를 로컬로 복제
        2. git add . : 현재 디렉토리(폴더) 밑의 모든 파일을 추적(추가)
        3. git commit -m "comment" : 실제 작업을 한 것의 히스토리를 만든다. (아직까진 로컬)
        4. git push origin master : 작업물을 서버 저장소로 올린다. (실제 반영)

- web
    - 웹은 다음과 같이 생겼어요.

브라우저 - 서버 컴퓨터(웹서버-DB)

         ㄴDNS(Domain Name Server)


    - 우린 일단 웹서버를 만들거에요.
    - 뭐를 이용해서? python Flask를 이용해서.

- routes.py
    - 브라우저의 주소창을 해석할 수 있어야해요.
    - 예를 들어 14.63.88.216:5999 로 접속하면 / (최상위 주소)로 접근하는 것이고
    - 예를 들어 14.63.88.216:5999/jisung 으로 접속하면 /jisung으로 접근하는 거에요.
    - routes.py는 다음과 같이 생겼어요.

```
#!/usr/bin/python
#-*- coding:utf-8 -*-
from flask import Flask, url_for
from flask import render_template, flash, redirect, session, request, g, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jisung')
def jisung():
    return render_template('jisung.html')

if __name__ == '__main__':
    app.run(host='14.63.88.216',port=5999,debug=True,threaded=True)
```

    - 1~2번째 줄은 그냥 항상 써주세요! 모든 python파일에
        - 설명을 하자면 1번째 줄은 저 경로의 python을 쓴다는 소리에요(몰라도 됩니다)
        - 2번째줄은 utf-8이라는 문자 포멧을 쓴다는 말이에요(한글 쓰려면 써줘야해요)
    - 3~4번째 줄은 눈치학상 기분학상 통법상 flask라는 애를 내가 쓰기위해 추가하겠다!라는 의미에요
    - 5번째 줄은 Flask를 실제로 생성하는 거에요. app이라는 친구가 들고있어요.
    - 6번째 줄은 비었구여
    - 7번째 줄은 브라우저에서 / 라는 주소로 접근했을 때 아래 함수로 보내겠다는 의미에요.
    - 8번째 줄은 home 이라는 함수를 정의한건데, 함수란 것은 다음시간에 할게요.
    - 9번째 줄은 index.html이라는 템플릿 파일을 렌더링 해서 반환한다는 의미에요.
    - 11~13번째 줄은 위와 같구요!
    - 15번째 줄은 만약 routes.py를 실행했다면 이라는 의미에요
    - 16번째 줄은 flask웹서버를 실행할건데, 저 아이피 주소에 5999 포트를 가진 웹서버를 실행한다! 라는 의미에요.


### 2017-02-27 ###
1. @app.routes(‘/angkeun’)  얘로 들어왔을 때 바로 아래 함수라는 애를 호출했다.
2. 저 함수라는 애가 뭘까?
3. 함수는 수학에서 봤던 함수랑 똑같이 인풋이 있고 계산을 알아서 잘 해서 아웃풋을 돌려주는 친구이다.

def f(x):
    return x + 5

result = f(5)
print result 
출력되는 결과물 : 10

4. 게시판의 아티클들을 볼 때, domain.com/board/10 이런식으로 접근을 하는데, 저 숫자 10 이 의미하는 것은 10번째 아티클을 의미할텐데 .. 저걸 어떻게 라우팅하지?
5. @app.route(‘/board/1’), @app.route(‘/board/2’) 이런식으로 무제한 코드를 생성한다.
6. 어머 그러면 벌써 윈도우를 만들었겠다. 왜냐하면 2^30 줄을 작성했을 테니까!
7. 방법이 없을까?
8. 변수에다가 받아보자! 저 숫자를
9. @app.route(‘/board/<int:number>’) 아!~!! 이런식으로 저 숫자를 변수에다가 저장할 수 있구나!

@app.route('/sangkeun/<int:number>')
def sangkeun_detail(number):
    return render_template('sangkeun_detail.html',number=number)

10. 이런식으로 바로 밑의 함수의 인풋으로 값이 들어가고, template을 렌더링할 때, 변수에다가 넘겨주는 방식으로 할 수 있구나
11. number = number 가 의미하는 것은 (template 변수명이 왼쪽, 현재 routes.py의 변수명이 오른쪽) 이라는 뜻이다.
12. 자 그럼 우리 여태까지 배운 것을 잘 이용해서, 방문자수 출력 페이지를 만들어보자
13. 어 그러면,,, 방문자수를 저장하는 무언가가 필요하겠네!!
14. 그러면 파일에다가 방문자수를 적어놓자!
15. 그리고 사람이 이 페이지에 접속할 때마다 방문자수를 1씩 증가시켜주면 되겠네
16. 아 ! 그럼 파이썬 언어에서 파일 입출력을 어떻게 하는지만 알고있으면, 시나리오는 다음과 같겠다.
    1. 맨 처음에 방문자수를 기록할 텍스트 파일에다가 0을 적어놓는다.
    2. 사람이 들어왔을때 (route로 함수에 보낼 때)
    3. 바로 밑 함수가 호출이 될텐데
    4. 호출이 되면 일단 저 파일에서 숫자를 하나 읽어온다.
    5. 1 증가시키고
    6. 저 파일에다가 증가시킨 숫자를 다시 적는다.
    7. 렌더링한다.
17. 어 그러면 …. 파일에 쓰는건 어떻게해 ? 
18. 그리고 어디다가 쓸건데?
19. unix계열에서 주소는 두가지가 있더라
20. 절대경로 와 상대 경로가 있는데
21. 절대 경로는 / 로 시작하는 절대 주소이고
22. 상대 경로는 .과 /와 ..을 이용해서 나타내는 현재 나의 위치로부터의 주소를 의미한다.
23. 결국 오늘은 상대 경로를 1도 안썼지만 … 우리는 /home/sisobus/FirstWebStudy/Application/views.txt 여기에다 적기로 했다.
24. 파이썬 파일 입출력은 다음과 같이 한다.


with open('/home/sisobus/FirstWebStudy/Application/views.txt','r') as fp:
        a = int(fp.read())
    a += 1
    with open('/home/sisobus/FirstWebStudy/Application/views.txt','w') as fp:
        fp.write(str(a))










