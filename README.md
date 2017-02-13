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
