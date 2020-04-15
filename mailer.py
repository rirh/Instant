
#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'huibikuile@qq.com'    # 发件人邮箱账号
my_pass = 'pjwhtafgjmgmbcia'              # 发件人邮箱密码
my_user = 'only_tigerhu@163.com'      # 收件人邮箱账号，我这边发送给自己
def_content = """
        <h1 >
          <a href="https://api.huzhihui.org.cn" >欢迎访问</a>
        </h1>     
            """


def mail(content=def_content, subject=''):
    ret = True
    try:
        msg = MIMEText(content, 'html', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["tigerzh", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["tigerzh", my_user])
        msg['Subject'] = subject               # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
