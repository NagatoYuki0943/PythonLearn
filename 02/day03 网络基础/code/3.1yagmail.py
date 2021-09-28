
# 导入邮件包
import yagmail

# 创建类对象(发件人,发件人授权码,发件的服务器)
# user: 账户
# password: 授权码
# host: 发送主机
# port: 端口号
mail = yagmail.SMTP(user='2487575080@qq.com', password='qgrikapxfkeldjbb', host='smtp.qq.com', port=465)

content = '你好'
# 使用yagmail对象发送邮件(指定收件人,邮件主题,发送的内容)
mail.send('1179913801@qq.com','测试一下' , content)

