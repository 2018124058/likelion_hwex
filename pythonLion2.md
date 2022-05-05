코드라이언 강의 메모2  
## 크롤링  
- Web crawler: 웹페이지의 데이터를 모아주는 소프트웨어  
- Web Crawling: 크롤러를 사용해 웹페이지의 데이터를 추출해내는 행위  

# 함수

함수: 자주 사용하는 코드를 묶음. 반복 작업 간결하게.  
```
def function_name(parameter) 
```

## 파일 생성하기: open 함수  
`open(파일, 모드)`  
- 모드: 파일의 상태 r(read: 읽기 전용), w(write: 내용 써넣을 수 있음, 기존 내용 덮어씀), a(append: 기존 내용에 추가 가능)
- 파일로 생성, 저장하기 
    ```
    file = open("daum.html","w")
    file.close() 
    ```
- `open("file_name", "mode", encoding="UTF-8")` 파일의 한글깨짐을 막을 수 있다
- `file.write(response.text)` 파일에 쓰기: 파라미터로 쓰고싶은 내용 - string 타입, +로 연결하기 
    - string이 아니면 str()로 타입 변환 해주기  

# 모듈  
모듈: 파이썬에서 자주 쓰이는 함수, 클래스, 변수 등을 모아둔 파일  
- 모듈을 직접 만들 수도, 다른 사람이 만든 것을 가져다 쓸 수도 있다  
- 모듈을 사용할 것이라고 `import module_name` 명시하기  
- `module_name.function_name()`

## requests 모듈  
- 터미널에 `pip install requests` 
    - pip라는 도구가 requests라는 모듈을 찾아 설치함  
    ```
    import requests
    print(requests) // 모듈의 경로 나옴
    ```  
- 요청과 응답  
    - 요청: client가 server에 어떤 정보를 요청  
        - put, get, post, delete 등 다양  
    - 응답: server가 client에게 결과값 return  
- get 함수 
    - `requests.get(url)`  
    - url: 요청을 보낸 서버의 주소 
    - GET 요청을 보내는 기능  
    - 서버의 응답값(requests.response)을 return 
    - https://docs.python-requests.org/en/master/api/#requests.Response  

```
import requests
url = "http://www.daum.net"
response = requests.get(url)
print(response) #Response [200] 200은 성공했다는 뜻
print(response.text) #text 형태로 응답 내용(html 문서)를 모두 가져옴. type string 
print(response.text[:500]) #string이라 index 활용 가능 
print(response.url) #url 주소 리턴
print(response.content) #응답의 content 리턴 
print(response.encoding) #encoding 방식 리턴
print(response.headers) #헤더
print(response.json)  #응답 값을 json으로 표기해달라
print(response.links) #html의 link 태그 값 리턴 
print(response.ok) #응답이 잘 되었는지 boolean 값 리턴
print(response.status_code) #200 #웹 상태코드 리턴 
```  
- 웹크롤링을 금지해둔 사이트의 경우 요청을 보낼 때 로봇이 아니라는 사용자 정보를 같이 보낸다  
```
headers = {~~}
response = requests.get(url, headers=headers)
```

## bs4 모듈의 BeautifulSoup 함수
`from bs4 import BeautifulSoup`  
- 의미있는 데이터로 변경  
`BeautifulSoup(데이터, 파싱방법)`  
- 데이터: html, xml이 올 수 있음  
- parsing: 문서(데이터)를 의미있게 변경하는 것  
- html.parser: 파이썬에 내장된 기본 파서   
`BeautifulSoup(response.text, 'html.parser')`  
- response.text: html, string  
- type이 string이 아닌 bs4.BeautifulSoup  
- BeautifulSoup라는 통에 데이터(string 한 덩어리)를 정리해줌  

```
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) #<title>Daum</title> 타이틀 element 리턴
print(soup.title.string) #태그 없이 제목값(content)만
print(soup.span) #가장 상단의 span element만
print(soup.findAll('span')) #모든 span elements
print(soup.findAll("a","link_favorsch")) #a elements 중 class가 "link_favorsch"인 것들만

results = soup.findAll('a','link_favorsch')

for result in results:
    print(result.get_text(), "\n") #태그 정보 없이 하나씩 출력
```

## datetime 모듈  
```
from datetime import datetime
print(datetime.today()) # 현재 날짜, 시간 출력
print(datetime.today().strftime("%Y년 %m월 %d일)) # 원하는 정보, 원하는 형태로
```
## json 모듈  
`import json` 파이썬이 제공하는 모듈로 설치 필요X 
json: javascript object notation  
- 데이터를 주고받을 때 사용하는 포맷 종류  
- "key":"value"
- `json.loads(str)` 응답값을 json으로 변경, dictionary type이 됨 

## googletrans 모듈  
`import googletrans`
- 언어감지/번역 기능을 가지는 library  
    - library: 모듈을 큰 기능단위에서 묶은 것 
    - 언어감지: 작성한 문자가 어떤 언어인지 감지  
    - 번역: 다른 언어로 변경  
  
`from googletrans import Translator`  
- googletrans 모듈의 Translator 기능  
- 언어 감지하기 
    - 번역기 만들기 -> 언어 감지할 문장 설정 -> 언어 감지
    - `detect(str)` 언어 감지  
    ```
    from googletrans import Translator
    translator = Translator() # 번역기 만들기 
    sentence = "감지할 문장"   # 문장 설정 
    detected = translator.dectect(sentence) # 언어감지
    print(detected) # Dectected(lang=ko, confidence=1.0) # 언어 및 감지의 신뢰성 출력 (1.0은 100%)  
    print(dectected.lang) # ko # lang값만 출력   
    ```   
- 언어 번역하기  
    - 번역기 만들기 -> 번역할 문장 설정 -> 번역을 원하는 언어 설정 -> 번역  
    - `translate(text,dext,src)` 번역  
        - text: 번역할 문장 
        - dest: 목적지. 어떤 언어로 번역할지  
        - src: 소스. text의 언어. optional (감지 능력이 이미 있음)  
    ```
    from googletrans import Translator
    translator = Translator() # 번역기 만들기 
    sentence = "번역할 문장"   # 문장 설정
    result = translator.translate(sentence, 'en') 
    print(result) #Translated(src=ko, dest=en, text = 번역된 문장, pronunciation=None, extra_data =...) # 기본언어가 영어라 dest가 영어일 경우 prouniciation은 None  
    print(result.text)
    ```
- googletrans 모듈이 작동하지 않는 에러 해결  
    - `pip install googletrans==3.1.0a0`
    - https://github.com/ssut/py-googletrans/issues/299


# API   
- Application Programming Interface  
- interface: 두 대상을 연결해주는 것 (사람-사람, 사람-컴퓨터 등) 
- API: client와 server를 연결, 데이터를 주고받을 수 있도록 함(html이 아닌 다른 정보를 가져오고 싶을 때). 사용자의 프로그램과 기존에 있는 프로그램을 연결. 특정한 규약이 있음 
- api를 만든다/api를 사용한다  
- openAPI: 모두에게 공개  
- API key: 누가 API를 사용하는지 나타내는 것. 보통 문자열로 이루어짐  
- 응답을 원하는 api 주소로 요청을 보내는 것 = api를 call, 부른다 

## API 활용  
openweathermap 활용 https://openweathermap.org/current
- `api = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}"`요청을 보내는 api 서버의 주소  
    - api의 파라미터 값 지정하기: city name, your api key  
    - 주소의 `?` 앞쪽: 공통 url / 뒤쪽: 파라미터. &로 서로 이어짐  
    - optional parameter
        - 언어 설정 `lang = kr` 
        - 단위 변경 `units = metric # 섭씨` `units = imperial # 켈빈(K)`

    ```
    city = "seoul"  
    apikey = "####"
    lang = "kr"
    # f-string을 활용해 파라미터 값 넣기
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}"
    ```

- 서버에 요청 보내기  
    ```
    import requests
    result = requests.get(api) # get 함수 이용 
    print(result.text) # str 
    ```
- json으로 변경하여 필요한 데이터 출력하기  
    ```
    data = json.loads(result.text) # dict -> key를 이용해 정보 불러올 수 있다 
    print(data["weather"][0]["main"]) # list안에 dict이 있을 때

    ```

# SMTP
SMTP: simple mail transfer protocol (간단하게 메일을 보내기 위한 약속)   
- SMTP 서버을 이용해 원하는 곳으로 메일을 보낼 수 있다
- email client - SMTP -> email server  
    - smtp에 맞추어 client가 자신의 email server에 메일 전송
    - 이메일 server가 다른 이메일 server로 smtp에 맞추어 메일 전송
- email client <- IMAP - email server  
    - IMAP: 이메일 server가 client에게 메일 전송할 때 사용  
- SMTP 서버도 주소(Address)를 가짐(메일 주소)
- Port: 접속할 때 이용하는 포트(문)  

## smtplib library
- 파이썬 내장 library 
- 메일 전송
    1. SMTP 메일 서버를 연결
        - `import smtplib`  
        - `smtplib.SMTP(SMTP_SERVER, SMTP_PORT)` 원하는 메일 서버와 연결  (`smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)`)
    2. SMTP 메일 서버에 로그인  
        - `smtp_object.login("id","password")` 
    3. SMTP 메일 서버로 메일 전송  
        - `smtp_object.send_message(message)`  
        - `smtp_object.quit()` 서버와의 연결 끊기  
    - MIME: 표준 (SMTP는 영어 외 지원X, MIME로 변환 필요) 

```
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # gmail에서 지정한 포트 

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #SSL(보안문제) 함께 처리하는 함수 #smtp 객체  

smtp.login("###","####") # 계정 존재하면 accepted
```
## email.message 모듈  
- MIME 형태로 변환
1. 이메일 만들기
    - MIME에 담기
2. 이메일에 내용 담기  
3. header(제목, 발신자, 수신자) 설정  
    - MIME의 HEADER: subject, From(발신자), To(수신자) 가짐  

```
from email.message import EmailMessage

message = EmailMessage() # Mime 형태로 변경해줌 

# 이메일 본문 내용 담기
message.set_content("메일 본문 내용") 

# HEADER 설정
message["subject"] = "제목"
message["From"] = "2018124058@yonsei.ac.kr"
message["TO"] = "수신할 주소"
```

## 메일 보내기 코드 정리 
```
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com" # 서버 이름 (개인 메일 주소x)
SMTP_PORT = 465

message = EmailMessage()
message.set_content("메일 내용")

message["Subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com"
message["To"] = "###@gmail.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###@gmail.com","######")
smtp.send_message()
smtp.quit()
```  

## 메일에 사진 첨부하기  
- 파일 모드 rb(read binary), wb, ab: binary-컴퓨터가 읽고 이해하기 편한 문자(이미지, 영상 파일 대체로 이런 모드)  

```
image = open("image.jpg", "rb") #rb 모드 
print(image.read()) # 파일 읽기
```
```
# close 없이 안전하게 파일을 열고 실행 후 닫기 
with open("image.jpg", "rb") as image: # 파일 = image
    image_file = image.read()  
```  
- 텍스트가 아닌 포맷 첨부하기
    - mixed format: text 외에 다른 타입도 섞여있음  
    - `add_attachment(image, maintype, subtype)  
        - image: 첨부할 내용  
        - maintype: 첨부한 내용의 타입  
        - subtype: 확장자   
        `message.add_attachment(image_file, maintype='image', subtype=jpg)`  
    - 확장자가 변경되어도 알 수 있게   
        - `import imghdr` 내장 모듈. 이미지 타입 알려줌  
        - `imgdr.what('filename', image_file)` 타입 리턴
        ```
        image_type = imgdr.what("image", image_file)
        message.add_attachment(image_file, maintype='image', subtype = image_type)
        ```  

## 이메일 주소의 유효성 체크  
### 정규표현식  
`import re` re 모듈 
- 문자열의 패턴 표현 
`^` 정규표현식의 시작
`$` 정규표현식의 끝  
`[a-zA-Z0-9.+_-]+` a부터z, A부터z, 0부터 9, . + _ - 가 1번 이상 반복  
`\.` 문자로서의 .을 의미 (\가 없으면 모든 문자 지칭)
`{2,3}` 최소 2번, 최대 3번 반복  

이메일 정규식과 검사 
```
# 이메일 정규식
reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
# 검사
# 맞지 않으면 None
re.match(reg,"abcd@gmail.com")
```  
이메일 유효성 검사 함수  
```
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)) # None이 아니면 true
        smtp.send_message(message)
        print("메일 전송")
    else:
        print("유효한 이메일 주소가 아닙니다.")
```


