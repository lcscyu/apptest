#coding=utf-8
import HTMLTestRunner
import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#定义发送邮件
def sentmail(file_new):
#发信邮箱
    mail_from = 'sendmail@shi-ke.cn'
#收信邮箱
    mail_to = 'sangchengyu@shi-ke.cn'
#定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['from'] = mail_from
    msg['to'] = mail_to
    #定义标题
    msg['Subject']=u"发送邮件测试"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接SMTP 服务器
    smtp.connect('smtp.shi-ke.cn')
    #用户名密码
    smtp.login('sendmail@shi-ke.cn','Coship7000?')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'E:\\PythonCode\\phone_project\\result'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print (file_new)
    #调用发邮件模块
    sentmail(file_new)

if __name__ == "__main__":
    #执行发邮件
    sendreport()