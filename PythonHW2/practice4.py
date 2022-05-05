import smtplib
from email.message import EmailMessage
import imghdr
import re

# 서버 연결 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# 로그인
smtp.login("sojeong9916@gmail.com", "~~~") # ~~~에 password 입력 

# 메일 생성 
message = EmailMessage()
message.set_content("좋은 하루 보내세용") 

message["Subject"] = "멋사 이소정입니다"
message["From"] = "sojeong9916@gmail.com"
message["To"] = "sojeong9916@gmail.com"

# 메일 전송 
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        message["To"] = addr
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

sendEmail("sojeong9916@gmail.com")
smtp.quit()