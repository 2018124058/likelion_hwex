# 코드라이언 강의 메모2  
# 크롤링  
- Web crawler: 웹페이지의 데이터를 모아주는 소프트웨어  
- Web Crawling: 크롤러를 사용해 웹페이지의 데이터를 추출해내는 행위  

## 함수

함수: 자주 사용하는 코드를 묶음. 반복 작업 간결하게.  
```
def function_name(parameter) 
```

### open 함수  
`open(파일, 모드)`  
- 모드: 파일의 상태 r(read: 읽기 전용), w(write: 내용 써넣을 수 있음, 기존 내용 덮어씀), a(append: 기존 내용에 추가 가능)
- 파일로 생성, 저장하기 
    ```
    file = open("daum.html","w")
    file.write(response.text) #파라미터로 쓰고싶은 내용
    file.close() 
    ```

## 모듈  
모듈: 파이썬에서 자주 쓰이는 함수, 클래스, 변수 등을 모아둔 파일  
- 모듈을 직접 만들 수도, 다른 사람이 만든 것을 가져다 쓸 수도 있다  
- 모듈을 사용할 것이라고 `import module_name` 명시하기  
- `module_name.function_name()`

### requests 모듈  
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
response = requests.get(url)) 
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

### bs4 모듈의 BeautifulSoup 함수
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

### datetime 모듈  
```
from datetime import datetime
print(datetime.today()) # 현재 날짜, 시간 출력
print(datetime.today().strftime("%Y년 %m월 %d일)) # 원하는 정보, 원하는 형태로
```


