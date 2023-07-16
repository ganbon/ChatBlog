import win32com.client
import os

def authmail(mailadress,number):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.to = mailadress
    # mail.cc = 'onpu@mahodo.com'
    mail.bcc = os.getenv("EMAIL_ADRESS")
    mail.subject = 'ChatBlogの認証コード送信'
    mail.bodyFormat = 1
    mail.body = f'''ChatBlogの送信コードは

                {number}

                です。'''
    mail.Send()
    

if __name__ == '__main__':
    mailadress = ''
    number = "123"
    authmail(mailadress,number)
