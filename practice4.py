import smtplib
import re
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

smtp.login("judy01@yonsei.ac.kr", "비밀번호") #로그인

message = EmailMessage()
message.set_content("week 5 과제 제출 메일입니다.")
message["Subject"] = "멋사 10기 김지안입니다."
message["From"] = "judy01@yonsei.ac.kr"
message["To"] = "ksjoon28@naver.com"

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 메일 주소가 아닙니다.")

sendEmail("ksjoon28@naver.com")
smtp.quit()